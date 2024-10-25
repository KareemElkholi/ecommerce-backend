# Ecommerce Backend

A containerized ecommerce backend built with FastAPI, MySQL, SQLAlchemy and Docker

## Prerequisites

- Docker and Docker Compose installed on your system
- Git for cloning the repository

## Quick Start

1. Clone the repository
```bash
git clone https://github.com/KareemElkholi/ecommerce-backend
```

2. Navigate to the project directory
```bash
cd ecommerce-backend
```

3. Set up environment variables
```bash
cp .env.example .env
```
> **Note**: Make sure to update the environment variables in your `.env` file

4. Start the application
```bash
docker compose up
```

Swagger documentation: `http://localhost:{APP_PORT}/docs`

## Environment Variables

The following environment variables can be configured in your `.env` file:

```plaintext
DB_USER=user
DB_PASS=pass
DB_HOST=db
DB_NAME=ecommerce
DB_URI=mysql+mysqldb://${DB_USER}:${DB_PASS}@${DB_HOST}/${DB_NAME}
SECRET_KEY=6046220e37015fc11748c76b04455f9f7fd4efcc98823b05191e8e224cff967f
ALGORITHM=HS256
EXPIRE=60
SCHEME=bcrypt
APP_PORT=8000
```

To get a secret key like this run:
```bash
openssl rand -hex 32
```

## Project Structure

```
├── app/
│   ├── api/
│   │   ├── v1/
│   │   └── api.py
│   ├── config/
│   ├── crud/
│   ├── models/
│   ├── schemas/
│   └── __main__.py
├── .env.example
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── init.py
├── init.sh
├── README.md
└── requirements.txt
```

## API Features

- User authentication and authorization
- Product management
- Cart functionality
- Order processing

## Development

To run the development environment with hot reload:

```bash
docker compose -f docker-compose.dev.yml up
```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request