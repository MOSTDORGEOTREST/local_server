from pydantic import BaseSettings


customers = "/databases/customers/"
#customers = "/home/tnick/databases/customers/"

class Settings(BaseSettings):
    server_host: str = "0.0.0.0"
    server_port: int = 9000

    photo_path: str = f'{customers}photos'
    excel_file: str = f'{customers}customers.xlsx'
    database_url: str = f"sqlite:///{customers}database.sqlite3"

settings = Settings()
