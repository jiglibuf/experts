from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def get_database_url(self):
        return f"DRIVER={{SQL Server}};SERVER={self.DB_HOST};DATABASE={self.DB_NAME};UID={self.DB_USER};PWD={self.DB_PASS}"
    

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
# print(settings.get_database_url)