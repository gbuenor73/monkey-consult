from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_config = {
    'host': "localhost",
    'user': "monkey",
    'password': "monkey",
    'database': "monkey_consulting"
}


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = f"mysql+mysqlconnector://{db_config.get('user')}:{db_config.get('password')}@localhost/{db_config.get('database')}"
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

    def __enter__(self):
        session_make = sessionmaker(bind=self.__engine)
        self.session = session_make()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
