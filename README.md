# Books API

A FastAPI-based REST API for managing a library of books, using SQLite for storage and Docker for deployment.

## Setup

1. **Clone the repository**
2. **Install dependencies**
   - For production:
     ```bash
     pip install -r requirements.txt
     ```
   - For development/testing:
     ```bash
     pip install -r requirements.txt -r requirements-dev.txt
     ```
3. **Database**
   - To manually create or reset the example database, use the scripts in `database/`.

## Workflow

- **Build Docker image:**
  - Run the VS Code task "Build Docker Container" or:
    ```bash
    ./bin/build.sh
    ```
- **Run the API in Docker:**
  - Run the VS Code task "Run Docker Container" or:
    ```bash
    ./bin/up.sh
    ```
- **Stop the Docker container:**
  - Run the VS Code task "Down Docker Container" or:
    ```bash
    ./bin/down.sh
    ```

## Testing


- **Development dependencies:**
  - Install from `requirements-dev.txt` for local testing.
- **Unit tests:**
  - Run all tests:
    ```bash
    python3 -m unittest discover -s test
    ```

## Project Structure

- `main.py` — FastAPI app entry point
- `api/` — API routes and routers
- `database/` — SQLite connector and scripts
- `test/` — Unit and integration tests
- `bin/` — Shell scripts for Docker workflow

---

For more details, see comments in the code and test files.
