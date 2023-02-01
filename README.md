# tsoha-chat
## Requirements:

- Python
- Docker

## Installation:
1. Clone repository

```git clone https://github.com/nualn/tsoha-chat.git```

2. Create virtual environment for the application

```python3 -m venv venv ```

3. Activate the environment

```source venv/bin/activate```

4. Install dependencies

```pip install -r requirements.txt```

5. Create a postgresql database

```docker compose up -d```

5. Create .env file with variables `SECRET_KEY=` and `DATABASE_URL=` to the apps root directory
When using the provided docker-compose file, the database url is `postgresql://postgres:postgres@localhost:5432/postgres`

6. Initialize the database

```python3 init_db.py```

8. Start the program

```flask --app src/app.py run```