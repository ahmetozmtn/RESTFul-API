import request_handler
import requirements_for_test
import json
import pytest

def send_request(endpoint_factory, endpoint,request_type, **kwargs):
    url = endpoint_factory(endpoint)
    response = request_type(url, **kwargs)
    return response

def load_test_data(file):
    with open("api_db_tests/data/"+file) as f:
        return json.load(f)

class TestNegative:

    @pytest.mark.parametrize("user_credentials",load_test_data("invalid_data_for_add.json"))
    def test_add_user(self,endpoint_factory,user_credentials,logger):
        post_data= user_credentials["input"].copy()
        logger.info(f"[{user_credentials['scenario_name']}] Kullanıcı ekleme işlemi başlatılıyor (beklenen: başarısız).")
        user_creation_result = send_request(endpoint_factory,requirements_for_test.add_data,request_handler.post_request,json=post_data)
        logger.info(f"Status code: {user_creation_result.status_code}")
        logger.info(f"Yanıt içeriği: {user_creation_result.json()}")
        assert user_creation_result.status_code in [400,422,500] , (f"Senaryo: {user_credentials['scenario_name']} -> "
        f"Beklenen hata kodu (400,422,500), ama gelen: {user_creation_result.status_code}")

       
  
    def test_update_user_invalidID(self,endpoint_factory,logger):
         #delete all data
        logger.info("Tüm kullanıcılar siliniyor.")
        delete_all_users_result = send_request(endpoint_factory,requirements_for_test.allDelete,request_handler.delete_request)
        assert delete_all_users_result.status_code == 200, "Negatif senaryo, güncelleme işlemi öncesi kullanıcılar silinemedi."

        #add users
        logger.info("Test için kullanıcı ekleniyor.")
        users = load_test_data("add_users.json")
        for user in users:
            user_creation_result = send_request(endpoint_factory,requirements_for_test.add_data,request_handler.post_request,json=user)
            assert user_creation_result.status_code == 200
        
        #update invalid id
        logger.info("Geçersiz ID (id=9) ile güncelleme deneniyor. (beklenen: başarısız).")
        data_for_update = {
             "username": "username-update","password": "password-update",
             "email": "example1@example.com","phone": "0555555555",
             "address": "example example-update","city": "City-update",
             "state": "State-update","product_name": "Product Name-update"
         }
        user_update_result = send_request(endpoint_factory,requirements_for_test.update_data.format(id=9),request_handler.put_request, json =data_for_update )
        logger.info(f"Status code: {user_update_result.status_code}")
        logger.info(f"Yanıt: {user_update_result.json()}")
        assert user_update_result.status_code == 404
        updated_user_json= user_update_result.json()
        assert updated_user_json["message"] == 'the data does not exist in the database'

    
    def test_delete_user_invalidID(self,endpoint_factory,logger):
        logger.info("Geçersiz ID ile (id=11) silme işlemi deneniyor. (beklenen: başarısız).")
        delete_user_result = send_request(endpoint_factory,requirements_for_test.delete_data.format(id=11),request_handler.delete_request)
        logger.info(f"Status code: {delete_user_result.status_code}")
        logger.info(f"Yanıt: {delete_user_result.json()}")
        assert delete_user_result.status_code == 400 
        deleted_user_json = delete_user_result.json()
        assert deleted_user_json["message"] == "the data does not exist in the database"