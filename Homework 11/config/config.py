import pathlib
from dotenv import dotenv_values


BASE_DIR = pathlib.Path(__file__).parent.parent
print(BASE_DIR)
config = dotenv_values(".env")


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + str(BASE_DIR / 'data' / 'helper.sqlite3')
    print(SQLALCHEMY_DATABASE_URI)
    # SECRET_KEY = config['SECRET_KEY']
    SECRET_KEY = "1234"