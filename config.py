from os import getenv

from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))
OWNER_ID = int(getenv("OWNER_ID"))
PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://graph.org/file/30d989cb03ffada2a49bb-8cc714127957f1366c.jpg")
SESSION = getenv("SESSION", None)
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Ranzzsupport")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ranzstre")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1475365115").split()))
FAILED = "https://graph.org/file/18a407f83530f053b8df9-dbe14a4178926e4105.jpg"
