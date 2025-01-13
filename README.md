# Code Repository Backend

This document provides detailed instructions for setting up and running the backend and frontend servers for the code repository backend.

---

## Project Structure

```plaintext
code_repository_backend/
├── app/
│   ├── __init__.py            # Initializes the app
│   ├── models.py              # Database models
│   ├── database.py            # Database connection and initialization
│   ├── routes.py              # API routes
│   ├── schemas.py             # Data validation schemas
│   ├── utils.py               # Utility functions
├── main.py                    # Entry point for the backend
├── requirements.txt           # Python dependencies
├── config.py                  # Configuration settings
└── README.md                  # Documentation
```

---

## Prerequisites

- **Python 3.8 or later**
- **pip** (Python package manager)

---

## Setting Up the Environment

### Step 1: Clone the Repository

Clone the project repository to your local machine:

```bash
git clone https://github.com/eigengram/Internal_Code_Search.git
cd Internal_Code_Search
```

### Step 2: Create a Virtual Environment

Create and activate a virtual environment:

- **On macOS/Linux**:

  ```bash
  python3 -m venv env
  source env/bin/activate
  ```

- **On Windows (Command Prompt)**:

  ```bash
  python3 -m venv env
  .\env\Scripts\activate
  ```

### Step 3: Install Dependencies

Install the required libraries using the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

---

## Running the Backend Server

1. Ensure that the database is properly configured in `config.py`.
2. Run the backend server:

   ```bash
   cd code_repository_backend
   python3 main.py
   ```

3. The backend server should now be running.

---

## Running the Frontend Server

1. Navigate to the directory where the Streamlit app is located.
2. Run the frontend server:

   ```bash
   cd code_repository_frontend
   streamlit run app.py
   ```

3. Open your web browser and navigate to:

   ```
   http://localhost:8501
   ```

   The frontend application should now be running!

---

## Requirements

The dependencies required for this project are listed in `requirements.txt`. Install them using the command provided in the **Installation** section.

---

## Additional Notes

- Ensure all necessary configurations are set in `config.py`.
- If you encounter issues, verify the environment setup and dependencies.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
