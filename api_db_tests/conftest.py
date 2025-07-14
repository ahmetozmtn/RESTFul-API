import pytest
import sqlite3
from requirements_for_test import BASE_URL,allDelete
import os
import logging
import requests

@pytest.fixture(scope='session')
def logger():
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)
    
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        console_handler.setFormatter(console_format)
        logger.addHandler(console_handler)

        file_handler = logging.FileHandler("test_logs.log", mode='w', encoding='utf-8')
        file_handler.setLevel(logging.INFO)
        file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(file_format)
        logger.addHandler(file_handler)

    return logger

@pytest.fixture(scope='session')
def base_url():
    return BASE_URL

@pytest.fixture
def endpoint_factory(base_url):
    def make_endpoint(path):
        return f"{base_url}{path}"
    return make_endpoint

@pytest.fixture
def db_connection():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    db_path = os.path.join(base_dir,"instance","database.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    yield conn
    conn.close()

@pytest.fixture(autouse=True)
def cleanup_before_and_after_tests():
    url = f"{BASE_URL}{allDelete}"
    response = requests.delete(url)
    assert response.status_code == 200 , "Test öncesi silme işlemi başarısız."

    yield

    response = requests.delete(f"{BASE_URL}{allDelete}")
    assert response.status_code == 200 , "Test sonrası temizleme işlemi başarısız."