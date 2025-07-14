BASE_URL = "http://127.0.0.1:5000"


#api endpoints
add_data = '/api/addData'
delete_data = '/api/deleteData/{id}'
get_data = '/api/getData'
allDelete = "/api/allDelete"
update_data = '/api/updateData/{id}'

#database commands
SELECT_BY_NAME = "SELECT * FROM users WHERE username = ?"