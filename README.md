# Ecommerce-Test

An automated test suite using Selenium and pytest for an E-commerce application. 

## Prerequisites

- Python 3.8 or higher
- Chrome browser installed
- Google ChromeDriver (or use `webdriver_manager` for automatic driver management)


## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Ecommerce-Test.git
cd Ecommerce-Test
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 3. Install the dependencies

```bash
pip install -r requirements.txt
pip install -r test-requirements.txt 
```

### 4. Setup the database

Ensure you have PostgreSQL installed and running. Then set up your database with the following environment variables:

- POSTGRES_USER
- POSTGRES_PASSWORD
- POSTGRES_DB
- DATABASE_URL


Ex:
```bash
export POSTGRES_USER=your_user
export POSTGRES_PASSWORD=your_password
export POSTGRES_DB=your_database
export DATABASE_URL=postgresql://your_user:your_password@localhost/your_database
```
<br/>
Then run the following commands to initalize and migrate the database:

```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

### 5. Run the application

```bash
python app.py
```

### 6. Run the tests

```bash
pytest tests
```

<br/>

## Extra

### CI/CD Integration

This project includes a GitHub Actions workflow for continuous integration. The workflow is defined in .github/workflows/ci.yml and is triggered on pushes and pull requests to the main branch.

#### GitHub Secrets
Ensure you have the following secrets set up in your GitHub repository:

```bash
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_DB
DATABASE_URL
```

The CI workflow currently performs the following steps:
<br/>
- Check out the repository
- Set-up Python
- Install dependencies
- Set up the database
- Run database migrations
- Execute the test suite
