# HBntory - Inventory Management Platform

## System Architecture

HBntory is an inventory management system for a fictional company with multiple branches.

The system is divided into several parts:

- Backoffice
- Database
- AI Query Service
- Product MCP Server
- Client Web Interface
- External Product API


## Services Responsibilities

### Backoffice

The Backoffice is used by internal users.

Common users can:
- Check stock.
- Add stock.
- Remove stock.

Users can only manage the branch they belong to.

The admin user can:
- Create users.
- Modify users.
- Delete users.
- Assign users to branches.

The admin does not manage stock.


### Database

The database stores only local information:

- Users.
- Branches.
- Stock quantities.

The database does not store product information.

Only the product ID is stored to link stock with external products.


### External Product API

The Product API provides product information.

It contains:

- Product names.
- Descriptions.
- Prices.
- Images.

Our application uses this API when product information is needed.


### Product MCP Server

The MCP server is a bridge between the AI system and the Product API.

It provides tools for the AI agent:

- List products.
- Get product details.


### AI Query Service

The AI service processes questions from users.

It uses:
- The MCP server to get product information.
- The database to get stock information.

The AI must not invent information if data is unavailable.


### Client Web Interface

The client interface allows anonymous users to ask questions about products and stock.

Example:

"Which branch has product X available?"


## Architecture Diagram

Client Web
|
|
AI Query Service
|
+-------------+
| |
v v
Product MCP Database
|
|
External Product API

Backoffice
|
|
Database



## Communication Choices

### Backoffice

Choice: Server-Side Rendering (SSR)

Reason:
- Easier to develop.
- Less JavaScript needed.

Limitation:
- Less interactive than a full frontend application.


### Client Web Interface

Choice: REST API

Reason:
- Each question is independent.
- Simple communication.

Limitation:
- No real-time streaming like WebSockets.


### AI and MCP Communication

Choice: MCP tools

Reason:
- Allows the AI to access external data safely.
- Separates AI logic from external services.


## MVP

The first version will include:

- User authentication.
- User roles.
- Stock management.
- Product API connection.
- MCP server.
- AI question answering.
- Simple client interface.

Later improvements:

- Better design.
- More advanced AI features.
- Additional functionalities.