from builtins import str

import pytest
from httpx import AsyncClient
from app.main import app
from app.models.user_model import User, UserRole
from app.utils.nickname_gen import generate_nickname
from app.utils.security import hash_password
from app.services.jwt_service import decode_token  # Import your FastAPI app
import logging
logger = logging.getLogger(__name__)

##LOGIN AS A ADMIN ROLE AND CHANGE THE ROLE OF ANOTHER ADMIN ACCOUNT
@pytest.mark.asyncio
async def test_update_admin_role_with_admin_role(async_client, admin_token,admin_user):
    updated_data = {'role' : 'MANAGER'}
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/users-role/{admin_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["role"] == updated_data["role"]

##LOGIN AS A ADMIN ROLE AND CHANGE THE ROLE OF A MANAGER ACCOUNT
@pytest.mark.asyncio
async def test_update_manager_role_with_admin_role(async_client, admin_token, manager_user):
    updated_data = {'role' : 'ADMIN'}
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/users-role/{manager_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["role"] == updated_data["role"]
\
##LOGIN AS A ADMIN ROLE AND CHANGE THE ROLE OF A USER ACCOUNT
@pytest.mark.asyncio
async def test_update_user_role_with_admin_role(async_client, admin_token,verified_user):
    updated_data = {'role' : 'ADMIN'}
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/users-role/{verified_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["role"] == updated_data["role"]




@pytest.mark.asyncio
async def test_update_admin_role_with_manager_role(async_client, manager_token,admin_user):
    updated_data = {'role' : 'ADMIN'}
    headers = {"Authorization": f"Bearer {manager_token}"}
    response = await async_client.put(f"/users-role/{admin_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["role"] == updated_data["role"]

@pytest.mark.asyncio
async def test_update_manager_role_with_manager_role(async_client, manager_token, manager_user):
    updated_data = {'role' : 'ADMIN'}
    headers = {"Authorization": f"Bearer {manager_token}"}
    response = await async_client.put(f"/users-role/{manager_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["role"] == updated_data["role"]

@pytest.mark.asyncio
async def test_update_user_role_with_manager_role(async_client, manager_token,verified_user):
    updated_data = {'role' : 'ADMIN'}
    headers = {"Authorization": f"Bearer {manager_token}"}
    response = await async_client.put(f"/users-role/{verified_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 200
    assert response.json()["role"] == updated_data["role"]






@pytest.mark.asyncio
async def test_update_admin_role_with_user_role(async_client, admin_user, user_token):
    updated_data = {'role' : 'ADMIN'}
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.put(f"/users-role/{admin_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 403
    assert response.json()["detail"] == "Operation not permitted"

@pytest.mark.asyncio
async def test_update_manager_role_with_user_role(async_client, manager_user, user_token):
    updated_data = {'role' : 'ADMIN'}
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.put(f"/users-role/{manager_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 403
    assert response.json()["detail"] == "Operation not permitted"

@pytest.mark.asyncio
async def test_update_user_role_with_user_role(async_client, verified_user, user_token):
    updated_data = {'role' : 'ADMIN'}
    headers = {"Authorization": f"Bearer {user_token}"}
    response = await async_client.put(f"/users-role/{verified_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 403
    assert response.json()["detail"] == "Operation not permitted"



@pytest.mark.asyncio
async def test_update_role_with_invalid_input(async_client, verified_user, admin_token):
    updated_data = {'notRole' : 'no_role'}
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = await async_client.put(f"/users-role/{verified_user.id}", json=updated_data, headers=headers)
    assert response.status_code == 400
    assert response.json()["detail"] == "Role is required"