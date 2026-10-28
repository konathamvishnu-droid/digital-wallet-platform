# Digital Wallet & Transaction Processing Platform

A secure backend application for managing digital wallets and processing financial transactions using **FastAPI, Python, and PostgreSQL**.

## Overview

The Digital Wallet Platform is designed to support wallet management, secure money transfers, transaction tracking, and role-based access control through REST APIs.

## Tech Stack

- **Language:** Python
- **Framework:** FastAPI
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Database Migrations:** Alembic
- **Validation:** Pydantic
- **Authentication:** JWT
- **Testing:** Pytest

## Core Features

- User registration and authentication
- JWT-based access control
- Role-based authorization
- Digital wallet management
- Deposits and withdrawals
- Wallet-to-wallet transfers
- Transaction history and ledger tracking
- Transaction validation and error handling
- Database schema migrations
- Automated API testing

*Note: Features should be marked as implemented only after they are completed and tested.*

## Project Structure

```text
digital-wallet-platform/
├── alembic/
├── app/
│   ├── api/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   └── services/
├── tests/
├── .env.example
├── .gitignore
├── alembic.ini
├── test_db.py
└── README.md
```

## Prerequisites

- Python 3.11 or later
- PostgreSQL
- Git
- Visual Studio Code (recommended)

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/konathamvishnu-droid/digital-wallet-platform.git
cd digital-wallet-platform
```

### 2. Create a Virtual Environment

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Install the packages required by the project:

```powershell
pip install fastapi "uvicorn[standard]" sqlalchemy alembic "psycopg[binary]" pydantic pydantic-settings python-dotenv "pwdlib[argon2]" pyjwt pytest httpx python-multipart
```

### 4. Configure Environment Variables

Create a `.env` file in the project root and configure your local settings:

```env
APP_NAME=Digital Wallet Platform
APP_ENV=development
DEBUG=True
DATABASE_URL=postgresql+psycopg://postgres:YOUR_PASSWORD@localhost:5432/digital_wallet_db
JWT_SECRET_KEY=YOUR_SECRET_KEY
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
REFRESH_TOKEN_EXPIRE_DAYS=7
```

Replace the placeholder values with your local PostgreSQL password and a securely generated JWT secret. Never commit `.env` or expose credentials in source control.

### 5. Create the Database

Open PostgreSQL and execute:

```sql
CREATE DATABASE digital_wallet_db;
```

If the database already exists, you do not need to create it again.

### 6. Run Database Migrations

```powershell
alembic upgrade head
```

### 7. Start the API Server

```powershell
uvicorn app.main:app --reload
```

Once the application is configured and running, open:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

The application entry point and API routes must exist before these endpoints will work.

## Running Tests

Run the automated tests with:

```powershell
pytest
```

## Security Considerations

- Store secrets in environment variables.
- Hash passwords before saving them.
- Validate and authorize all sensitive operations.
- Use database transactions for financial operations.
- Prevent duplicate transaction processing.
- Maintain reliable transaction records.
- Never store raw passwords or expose secret keys.

## Current Development Status

This project is under development. Features and setup instructions may change as implementation and testing progress.

## Author

**Vishnu**

GitHub: https://github.com/konathamvishnu-droid
