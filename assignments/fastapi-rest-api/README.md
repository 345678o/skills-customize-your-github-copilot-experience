# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Implement a REST API using FastAPI to manage a simple resource collection. This assignment focuses on API routing, request handling, JSON responses, and basic CRUD operations.

## 📝 Tasks

### 🛠️ Create the FastAPI application

#### Description
Set up a FastAPI app and add an initial endpoint that returns a JSON welcome message.

#### Requirements
Completed program should:

- Import FastAPI and create a FastAPI application instance.
- Define a root `GET /` endpoint returning a JSON object with a welcome message.
- Include a `main` block that can start the app with `uvicorn` when executed directly.
- Document how to install `fastapi` and `uvicorn` in a short note.

### 🛠️ Implement resource CRUD endpoints

#### Description
Build a collection endpoint for a simple resource and add create, read, update, and delete operations.

#### Requirements
Completed program should:

- Use an in-memory list as the data store for the resource.
- Provide `GET /items` to return all items.
- Provide `GET /items/{item_id}` to return a single item or raise a 404 error.
- Provide `POST /items` to accept JSON body data and add a new item.
- Provide `PUT /items/{item_id}` to update an existing item.
- Provide `DELETE /items/{item_id}` to remove an item.
- Return JSON responses for success and error conditions.

## Starter code

Use `starter-code.py` as a starting point for the FastAPI application. It includes the app skeleton, model definitions, and placeholder endpoints.

## Notes

- This assignment is designed to run in a local Python environment with FastAPI installed.
- Recommended install command:

```bash
pip install fastapi uvicorn
```
