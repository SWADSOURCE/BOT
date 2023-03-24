from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID","13277434"))
API_HASH = getenv("API_HASH","8444bed3061cda264cd6874de8fa45cc")

BOT_TOKEN = getenv("BOT_TOKEN","5628899181:AAHSLZoVU55UwpBhT1-m6z87nijZ-XDBMDw")
OWNER_ID = int(getenv("OWNER_ID","5566753847"))

MONGO_DB_URI = getenv("MONGO_DB_URI","mongodb+srv://szein:szein@cluster0.mw3zpgd.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN","t.me/S_325")
