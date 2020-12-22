import os

from dotenv import load_dotenv
# полдгружаем переменные , которые прописаны в файле .env
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

admins = [
    os.getenv("ADMIN_ID"),
]

ip = os.getenv("ip")
