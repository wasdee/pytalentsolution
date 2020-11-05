from pydantic import BaseSettings


class Settings(BaseSettings):
    project_id: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        case_sensitive = False

    def set_projectId(self, value):
        self.project_id = value


settings = Settings()
