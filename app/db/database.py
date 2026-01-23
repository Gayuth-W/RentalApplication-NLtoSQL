from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = "root"
DB_PASSWORD = "Gayuth12345!"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "rental_db"

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine)