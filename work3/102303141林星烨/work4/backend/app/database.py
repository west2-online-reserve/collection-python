# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


def get_db():
    # 获取数据库连接字符串（通常从环境变量或配置文件中）
    DATABASE_URL = "mysql+pymysql://root:123456@localhost:3308/star1"

    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(bind=engine)  # 创建所有表（仅在首次运行时需要）

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
