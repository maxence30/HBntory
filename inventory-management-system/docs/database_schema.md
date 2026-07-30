# Database Schema

## Users

Stores authentication and user information.

Fields:

- id
- username
- password_hash
- role
- branch_id
- is_deleted


## Branches

Stores company branches.

Fields:

- id
- name


## Stock

Stores stock quantities by branch and external product identifier.

Fields:

- id
- branch_id
- product_id
- quantity


## Relationships

- One branch can have many users.
- One branch can have many stock entries.
- A common user must belong to one branch.
- The admin user has no branch.
- Product information is not stored locally.