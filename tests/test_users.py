import pytest
from jose import jwt
from app import schemas
from app.config import settings



# def test_root(client):
#     res = client.get("/")
#     print(res.json().get('message'))
#     assert (res.json().get('message')) == 'My api is working -moving to win'
#     assert res.status_code == 200

def test_create_user(client):
    res = client.post("/users/", json={"email":"pippa@user.com", "password":"secret"})
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "pippa@user.com"
    assert res.status_code == 201

def test_login_user(client, test_user):
    res = client.post("/login", data={"username":test_user['email'], "password":test_user['password']})
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token, settings.secret_key, algorithms=[settings.algorithm])
    id= payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == 'bearer'
    assert res.status_code == 200

# def test_create_user_success(mocker):
#     # Mock the database session and user model
#     mock_db = mocker.Mock()
#     mocker.patch("app.routers.user.get_db", return_value=mock_db)
#     mocker.patch("app.routers.user.utils.hash", return_value="hashedpassword")
#     mock_db.query.return_value.filter.return_value.first.return_value = None
#     mock_db.add.return_value = None
#     mock_db.commit.return_value = None
#     mock_db.refresh.return_value = None

#     user_data = {"email": "test@example.com", "password": "password123"}

#     response = client.post("/users/", json=user_data)
#     assert response.status_code == 201


# def test_create_user_fail_existing_email(mocker):
#     mock_db = mocker.Mock()
#     mocker.patch("app.routers.user.get_db", return_value=mock_db)
#     mock_db.query.return_value.filter.return_value.first.return_value = (
#         True  # User exists
#     )

#     user_data = {"email": "test@example.com", "password": "password123"}

#     response = client.post("/users/", json=user_data)
#     assert response.status_code == 400
#     assert "already exists" in response.json()["detail"]


# def test_get_user_not_found(mocker):
#     mock_db = mocker.Mock()
#     mocker.patch("app.routers.user.get_db", return_value=mock_db)
#     mock_db.query.return_value.filter.return_value.first.return_value = None

#     response = client.get("/users/999")
#     assert response.status_code == 404
#     assert "does not exist" in response.json()["detail"]
