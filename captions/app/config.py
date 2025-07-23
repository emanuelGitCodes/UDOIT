import os


class Config:
    # Construct MySQL URI from individual env vars, with a fallback to SQLite for local dev
    mysql_user = os.getenv("MYSQL_USER", "")
    mysql_pass = os.getenv("MYSQL_PASSWORD", "")
    mysql_host = os.getenv("MYSQL_HOST", "localhost")
    mysql_port = os.getenv("MYSQL_PORT", "3306")
    mysql_db = os.getenv("MYSQL_DATABASE", "")
    default_sqlite = "sqlite:///app.db"

    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URI") or (
        f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}:{mysql_port}/{mysql_db}"
        if all([mysql_user, mysql_pass, mysql_db])
        else default_sqlite
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER", "uploads")
