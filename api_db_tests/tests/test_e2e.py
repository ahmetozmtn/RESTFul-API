import request_handler
import requirements_for_test
import json

def send_request(endpoint_factory, endpoint,request_type, **kwargs):
    url = endpoint_factory(endpoint)
    response = request_type(url, **kwargs)
    return response



class TestUserFlowE2E:

    def test_user_crud_operations(self,endpoint_factory,db_connection,logger):
        with open("api_db_tests/data/add_users.json") as file:
            users = json.load(file)
        for user in users:
            logger.info(f"{user['username']} ekleniyor...")
            user_creation_result = send_request(endpoint_factory,requirements_for_test.add_data,request_handler.post_request,json = user)
            assert user_creation_result.status_code == 200 , "Kayıt başarısız."
            assert user_creation_result.json()["message"] == 'the data was successfully added to the database' , "Kayıt başarısız veya mesajda hata var."
            logger.info(f"{user['username']} isimli kullanıcı başarıyla kaydedildi")

            #check db
            logger.info("Eklenen kullanıcıların kontrolü için veritabanı bağlantı işlemi başlatılıyor")
            cursor = db_connection.cursor()
            cursor.execute(requirements_for_test.SELECT_BY_NAME,(user["username"],))
            found_user = cursor.fetchone()
            assert found_user is not None, f"{user['username']} veritabanında bulunamadı."
            assert found_user["username"] == user["username"], "Eklenen kullanıcı adı ve db de bulunan eşleşmiyor."
            assert found_user["password"] != user["password"], "Şifre hash'lenmemiş görünüyor ya da aynı şekilde saklanıyor."
            logger.info(f"{user['username']} isimli kullaıcının db kontrolü tamamlandı.")


        

        #get created users
        logger.info("DB de bulunan tüm kullanıcıların alınması işlemi başlatılıyor")
        get_user_result = send_request(endpoint_factory,requirements_for_test.get_data,request_handler.get_request)
        assert get_user_result.status_code == 200, "Kullanıcıları alma işlemi başarısız"
        checked_user_json = get_user_result.json()
        assert len(checked_user_json) > 0 , "DB de kullanıcı bulunmuyor."
        assert len(checked_user_json) == 3, "Kullanıcı sayısında bir sorun var."
        for user in checked_user_json:
            assert "id" in user , "Kullanıcıların id bilgisi bulunmuyor"
        logger.info("Tüm kullanıcılar eksiksiz alındı.")
        
        
        #update user
        logger.info("Güncelleme işlemi başlatılıyor.")
        data_for_update = {
             "username": "username-update",
             "password": "password-update",
             "email": "example1@example.com",
             "phone": "0555555555",
             "address": "example example-update",
             "city": "City-update",
             "state": "State-update",
             "product_name": "Product Name-update"
         }
        user_update_result = send_request(endpoint_factory,requirements_for_test.update_data.format(id= checked_user_json[-1]["id"]),request_handler.put_request, json =data_for_update )
        assert user_update_result.status_code == 200 ,"Güncelleme başarısız"
        updated_user_json= user_update_result.json()
        assert updated_user_json["message"] == 'the data was successfully updated in the database', "Güncelleme başarsız veya mesajda bir sorun var."
        logger.info(f"{checked_user_json[-1]['username']} isimli kullanıcının bilgileri güncellendi.")


        #check db again
        logger.info("Güncellenen kullanıcı bilgilerini kontrol için db bağlantısı başlatılıyor.")
        cursor.execute(requirements_for_test.SELECT_BY_NAME,(data_for_update["username"],))
        user_new_info = cursor.fetchone()
        assert user_new_info["username"] == data_for_update["username"], "Günellenen kullanıcı adı ve db de bulunan kullanıcı adı uyuşmuyor."
        assert user_new_info["password"] != data_for_update["password"], "Şifre hash'lenmemiş görünüyor ya da aynı şekilde saklanıyor."
        logger.info("Güncellenen bilgiler ve db de bulunan bilgiler eşleşiyor")
        
        #delete user
        logger.info(f"{checked_user_json[-1]['username']} isimli kullanıcıyı silme işlemi başlatılıyor.")
        delete_user_result = send_request(endpoint_factory,requirements_for_test.delete_data.format(id= checked_user_json[-1]["id"]),request_handler.delete_request)
        assert delete_user_result.status_code == 200, "Kullanıcı silinemedi"
        assert delete_user_result.json()["message"] == 'the data was successfully deleted from the database' ,"Kullanıcı silinemedi veya mesaj hatalı."
        logger.info(f"{checked_user_json[-1]['username']} isimli kullanıcı silindi.")

        #check deleted user in db
        logger.info("Silinen kullanıcıyı kontol etmek için db ye bağlanılıyor.")
        cursor.execute(requirements_for_test.SELECT_BY_NAME,(data_for_update["username"],))
        new_db_status = cursor.fetchone()
        assert new_db_status is None , "Kullanıcı db de mevcut, silme işlemi başarısız."
        logger.info("Silinen kullanıcı db de bulunmuyor.")
        

        #delete all users
        logger.info("Tüm kullanıcıları silme işlemi başlatılıyor.")
        dalete_all_users_result= send_request(endpoint_factory,requirements_for_test.allDelete,request_handler.delete_request)
        assert dalete_all_users_result.status_code == 200 , "Tüm kullanıcıları silme işlemi başarısız."
        assert dalete_all_users_result.json()["message"] == "all data was successfully deleted from the database" , "Tüm kullanıcıları silme işlemi başarısız veya mesaj hatalı."
        logger.info("Tüm kullanıcılar silindi.")

        #check empty db
        logger.info("Kullanıcıların tamamının silindiğini doğrulamak için db ye bağlanılıyor.")
        cursor.execute("SELECT COUNT(*) FROM users")
        count = cursor.fetchone()[0]
        assert count == 0 ,"DB de hala kullanıcı bulunuyor."
        logger.info("DB de hiç kullanıcı bulunmuyor.")