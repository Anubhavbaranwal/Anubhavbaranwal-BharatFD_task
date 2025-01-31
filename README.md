# FastAPI FAQ Application

This is a FastAPI application for managing FAQs with multilingual support and caching using Redis.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/Anubhavbaranwal/fastapi-faq.git
   cd fastapi-faq
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the Application

1. Start the Redis server:
   ```sh
   redis-server
   ```

2. Run the FastAPI application:
   ```sh
   uvicorn app.main:app --reload
   ```

3. The application will be available at `http://127.0.0.1:8000`.

## API Endpoints

- `GET /faq/`: Retrieve all FAQs.
- `GET /faq/{faq_id}`: Retrieve a specific FAQ by ID.
- `POST /faq/`: Create a new FAQ.
- `PUT /faq/{faq_id}`: Update an existing FAQ by ID.
- `DELETE /faq/{faq_id}`: Delete an FAQ by ID.

## Running Tests

1. Install the test dependencies:
   ```sh
   pip install -r requirements.txt
   ```

2. Run the tests:
   ```sh
   pytest
   ```

## License

This project is licensed under the MIT License.