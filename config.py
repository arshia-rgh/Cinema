from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    DB_USER = 'root'
    DB_PASSWORD = ''
    DB_HOST = '127.0.0.1'
    DB_PORT = '3306'
    DB_NAME = 'cinema_tickets'