import sender_stand_request
import data


def get_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_kit_assert(kit_body):
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

def negative_assert_code_400(kit_body):
    token = sender_stand_request.get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)
    assert response.status_code == 400

# Tests para "name" al crear un kit
# Test 1. Validación campo name permite 1 caracter.
def test_create_kit_1_letter_in_name_get_success_response():
    positive_kit_assert(data.one_letter)

#Test 2. Validación campo name permite 511 caracteres.
def test_create_kit_511_letter_in_name_get_success_response():
    positive_kit_assert(data.allowed_letter)

#Test 3. Validación campo name no permite estar vacio.
def test_create_kit_no_letter_in_name_get_negative_response():
    negative_assert_code_400(data.no_letter)

#Test 4. Validación campo name no permite 512 caracteres.
def test_create_kit_512_letter_in_name_get_negative_response():
    negative_assert_code_400(data.not_allowed_letter)

#Test 5. Validación campo name permite caracteres especiales.
def test_create_kit_special_characters_in_name_get_success_response():
    positive_kit_assert(data.special_characters)

#Test 6. Validación campo name permite espacios.
def test_create_kit_space_in_name_get_success_response():
    positive_kit_assert(data.space_allowed)

#Test 7. Validación campo name permite números en el string.
def test_create_kit_numbers_in_name_get_success_response():
    positive_kit_assert(data.numbers_allowed)

#Test 8. Validación campo kit_body no permite no tener parámetros
def test_create_kit_without_parameter_in_name_get_negative_response():
    negative_assert_code_400(data.not_parameter_allowed)

#Test 9. Validación campo name no permite caracter numérico
def test_create_kit_number_character_in_name_get_negative_response():
    negative_assert_code_400(data.number_parameter)