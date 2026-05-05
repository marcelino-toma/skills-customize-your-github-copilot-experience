# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a REST API using FastAPI, including defining endpoints, handling JSON requests and responses, and running a local API server.

## 📝 Tasks

### 🛠️ Setup FastAPI and Create API Endpoints

#### Description
Set up a FastAPI application and add routes for basic API functionality.

#### Requirements
Completed program should:

- Import `FastAPI` and create an application instance
- Define a root endpoint (`/`) that returns a welcome message in JSON format
- Define at least two additional endpoints that return JSON responses

### 🛠️ Request Handling and Validation

#### Description
Handle incoming request data and validate it using Pydantic models.

#### Requirements
Completed program should:

- Define a Pydantic model for request payloads
- Implement an endpoint that accepts POST requests with JSON data
- Return a JSON response that includes values from the request

### 🛠️ Run and Test the API

#### Description
Run the FastAPI app locally and verify that the endpoints work as expected.

#### Requirements
Completed program should:

- Start the app with Uvicorn or the built-in FastAPI development server
- Provide example URLs or request bodies for testing each endpoint
- Confirm responses are returned with correct JSON structure and status codes
