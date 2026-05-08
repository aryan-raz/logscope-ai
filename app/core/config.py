from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    APP_NAME = os.getenv("APP_NAME", "Log Analysis Engine")
    DEBUG = os.getenv("DEBUG", "True")

settings = Settings()