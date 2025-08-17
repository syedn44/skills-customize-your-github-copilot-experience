# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and test RESTful APIs using the FastAPI framework in Python. You will create endpoints, handle requests and responses, and understand basic API concepts such as CRUD operations.

## 📝 Tasks

### 🛠️	Basic FastAPI Setup

#### Description
Set up a FastAPI project and create a simple API endpoint that returns a welcome message.

#### Requirements
Completed program should:

- Install and import FastAPI
- Create an app instance
- Define a GET endpoint `/` that returns a JSON welcome message
- Run the server locally

### 🛠️	CRUD Operations for a Resource

#### Description
Implement CRUD (Create, Read, Update, Delete) operations for a resource (e.g., `items` or `users`) using FastAPI endpoints.

#### Requirements
Completed program should:

- Define a data model using Pydantic
- Implement endpoints for:
  - Creating a new resource (POST)
  - Reading all resources (GET)
  - Reading a single resource by ID (GET)
  - Updating a resource by ID (PUT)
  - Deleting a resource by ID (DELETE)
- Store data in an in-memory list or dictionary
- Return appropriate status codes and messages

### 🛠️	API Testing and Documentation

#### Description
Explore FastAPI's automatic documentation and test your endpoints using the interactive Swagger UI.

#### Requirements
Completed program should:

- Access the API docs at `/docs`
- Test all endpoints using the Swagger UI
- Ensure all endpoints have clear request/response models and descriptions
