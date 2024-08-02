# Documentation for Pytests:
### test_update_admin_role_with_admin_role:

Tests updating the role of an admin user with another admin role, expecting a 200 status code and the role to be "MANAGER".

### test_update_manager_role_with_admin_role

Tests updating the role of a manager user with an admin role, expecting a 200 status code and the role to be "ADMIN".

### test_update_user_role_with_admin_role

Tests updating the role of a regular user with an admin role, expecting a 200 status code and the role to be "ADMIN".

### test_update_admin_role_with_manager_role

Tests updating the role of an admin user with a manager role, expecting a 200 status code and the role to be "ADMIN".

### test_update_manager_role_with_manager_role

Tests updating the role of a manager user with another manager role, expecting a 200 status code and the role to be "ADMIN".

### test_update_user_role_with_manager_role

Tests updating the role of a regular user with a manager role, expecting a 200 status code and the role to be "ADMIN".

### test_update_admin_role_with_user_role

Tests updating the role of an admin user with a regular user role, expecting a 403 status code and an "Operation not permitted" detail message.

### test_update_manager_role_with_user_role

Tests updating the role of a manager user with a regular user role, expecting a 403 status code and an "Operation not permitted" detail message.

### test_update_user_role_with_user_role

Tests updating the role of a regular user with another regular user role, expecting a 403 status code and an "Operation not permitted" detail message.

### test_update_role_with_invalid_input

Tests updating a role with invalid input, expecting a 400 status code and a "Role is required" detail message.