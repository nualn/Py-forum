# ChatApp
**Note** 
This application is not deployed anywhere. You can run it locally by following the instructions below.

Welcome to the ChatApp! This is a simple forum type web app that enables you to chat with other users.

## Features

- **User authentication:** Create an account or log in with an existing one.
- **Forums:** Browse forums on topics of your interest. Only admins can create new forums.
- **Create posts:** Create new posts in forums. You have to be logged in to do this.
- **Comment posts:** Comment on posts. You have to be logged in to do this.
- **Check user profiles:** Check other users' profiles and see their posts and comments.

## Getting started

### Requirements:
- Python
- Docker
 
### Installation

1. Clone repository

```
git clone https://github.com/nualn/tsoha-chat.git
```

2. Create virtual environment for the application

```
python3 -m venv venv 
```

3. Activate the environment

```
source venv/bin/activate
```

4. Install dependencies

```
pip install -r requirements.txt
```

5. Create a postgresql database

```
docker compose up -d
```

5. Create .env file with the following variables to the apps root directory
```
SECRET_KEY=
DATABASE_URL=
``` 
If using the provided docker-compose file, the database url is 
```
postgresql://postgres:postgres@localhost:5432/postgres
```

6. Initialize the database

```
python3 init_db.py
```

8. Start the program

```
flask --app src/app.py run
```

9. Access the application at http://localhost:5000. You can register a new account or log in with the default user `admin` with password `admin`
