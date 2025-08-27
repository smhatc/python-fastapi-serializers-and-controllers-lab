from sqlalchemy.orm import Session, sessionmaker
from data.tea_data import teas_list, comments_list
from data.user_data import user_list
from config.environment import db_URI
from sqlalchemy import create_engine
from models.base import Base

engine = create_engine(db_URI)
SessionLocal = sessionmaker(bind=engine)

try:
    print("Recreating database...")
    # Drop and recreate tables to ensure a clean slate
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    print("Seeding the database...")
    db = SessionLocal()

    # Seed users after teas
    db.add_all(user_list)
    db.commit()

    # Seed teas first, as comments depend on them
    db.add_all(teas_list)
    db.commit()

    # Seed comments after teas
    db.add_all(comments_list)
    db.commit()

    db.close()

    print("Database seeding complete! 👋")
except Exception as e:
    print("An error occurred:", e)
