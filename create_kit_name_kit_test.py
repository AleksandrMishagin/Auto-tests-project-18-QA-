import sender_stand_request
import data

def get_new_user_token():
    user_response = sender_stand_request.post_new_user(data.user_body)
    auth_token = user_response.json()["authToken"]
    return auth_token

def get_kit_body(name): #функция для обновления данных после копирования
    current_kit_body = data.kit_body.copy()
    current_kit_body["name"] = name
    return current_kit_body

def positive_assert(name): #функция для позитивных тестов
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body,auth_token)
    assert kit_response.json()["name"] == name
    assert kit_response.status_code == 201

def negative_assert_code_400(name): #функция для негативных тестов
    kit_body = get_kit_body(name)
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

def negative_assert_no_name(kit_body): #функция для отсутствия имени
    auth_token = get_new_user_token()
    kit_response = sender_stand_request.post_new_client_kit(kit_body, auth_token)
    assert kit_response.status_code == 400

def test_create_kit_1_letter_in_name_get_success_response(): #name из 1 буквы
    positive_assert("a")

def test_create_kit_511_letter_in_name_get_success_response(): #name из 511 символов
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def test_create_kit_empty_name_get_error_response(): #name пустой
    negative_assert_code_400("")

def test_create_kit_512_letter_in_name_get_error_response(): #name из 512 символов
    negative_assert_code_400("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def test_create_kit_english_letter_in_name_get_success_response(): #name с английскими буквами в тексте
    positive_assert("QWErty")

def test_create_kit_russian_in_name_get_success_response(): #name с русскими буквами в тексте
    positive_assert("Мария")

def test_create_kit_special_symbols_in_name_get_success_response(): #name со спец. символами в тексте
    positive_assert("\"№%@\",")

def test_create_kit_spaces_in_name_get_success_response(): #name с пробелами в тексте
    positive_assert(" Человек и КО ")

def test_create_kit_figures_str_in_name_get_success_response(): #name из строки "123"
    positive_assert("123")

def test_create_kit_no_name_get_error_response(): #name отсутствует
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_no_name(kit_body)

def test_create_kit_symbols_in_name_get_error_response(): #name из цифр 123
    negative_assert_code_400(123)