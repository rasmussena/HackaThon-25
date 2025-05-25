# Backend Directory

This directory contains the FastAPI backend service that powers the textbook chat application. It handles API requests, integrates with AI services, and manages data persistence.

## Architecture

The backend follows a modular architecture with the following components:

- **API Routes**: FastAPI endpoints for handling client requests
- **Services**: Business logic and AI integration
- **Models**: Data models and schemas
- **Utils**: Helper functions and utilities
- **Config**: Configuration and environment settings

## API Documentation

The API documentation is available at `/docs` when running the server locally. This provides:
- Interactive API documentation
- Request/response schemas
- Authentication requirements
- Example requests

## Key Features

1. **AI Integration**
   - OpenAI API integration for chat responses
   - LangChain for enhanced AI capabilities
   - Caching with Redis for improved performance

2. **Authentication**
   - User registration and login
   - JWT token-based authentication
   - Session management

3. **Data Management**
   - Textbook content processing
   - Chat history storage
   - User data management

## Development

1. **Setup**
   - Create a virtual environment
   - Install dependencies from requirements.txt
   - Configure environment variables

2. **Running the Server**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

3. **Testing**
   - Unit tests for core functionality
   - Integration tests for API endpoints
   - AI service integration tests

## Environment Variables

Required environment variables:
- `OPENAI_API_KEY`: OpenAI API key
- `LANGCHAIN_API_KEY`: LangChain API key
- Additional configuration as needed

## Error Handling

The backend implements comprehensive error handling:
- Input validation
- API error responses
- Logging and monitoring
- Rate limiting 