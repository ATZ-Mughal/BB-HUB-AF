import re
from os import environ, getenv
from Script import script

id_pattern = re.compile(r"^.\d+$")


def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# ---------------------------------------------------------------
# ---------------------------------------------------------------         ,
SESSION = environ.get("SESSION", "𝚉𝙰𝙲𝙺-𝚁𝙾𝚇-Bot")
API_ID = int(environ.get("API_ID", ""))
API_HASH = environ.get("API_HASH", "")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
# ---------------------------------------------------------------
# ---------------------------------------------------------------
ADMINS = [
    int(admin) if id_pattern.search(admin) else admin
    for admin in environ.get("ADMINS", "").split()
]
USERNAME = environ.get("USERNAME", "https://t.me/The_ZackRox")  # ADMIN USERNAME
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", ""))  # LOG CHANNEL
MOVIE_GROUP_LINK = environ.get("MOVIE_GROUP_LINK", "https://t.me/") # MOVIE GROUP
CHANNELS = [
    int(ch) if id_pattern.search(ch) else ch
    for ch in environ.get("CHANNELS", "").split() # DATABASE CHANNEL
]
# ---------------------------------------------------------------
# ---------------------------------------------------------------F
DATABASE_URI = environ.get(
    "DATABASE_URI",
    "",     # ADD YOUR DB URI
)
DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0") #REPLACE WITH YOURS DB NAME
COLLECTION_NAME = environ.get("COLLECTION_NAME", "BB_Telegram_files")
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ----------- There will be channel id add in all these ---------
LOG_API_CHANNEL = int(environ.get("LOG_API_CHANNEL", "")) #LOG CHANNEL ID
BIN_CHANNEL = int(environ.get("BIN_CHANNEL", "")) #DATABASE CHANNEL ID
DELETE_CHANNELS = int(environ.get("DELETE_CHANNELS", "")) #DELETE CHANNEL ID
LOG_VR_CHANNEL = int(environ.get("LOG_VR_CHANNEL", "")) #SHORTENER LOG CHANNEL ID
auth_channel = environ.get("AUTH_CHANNEL", "") # FORCE SUB CHANNEL ID
SUPPORT_GROUP = int(environ.get("SUPPORT_GROUP", ""))   #SUPPORT GROUP ID
request_channel = environ.get("REQUEST_CHANNEL", "")    #REQUEST CHANNEL ID
MOVIE_UPDATE_CHANNEL = int(environ.get("MOVIE_UPDATE_CHANNEL", "")) # MOVIE UPDATES CHANNEL ID
SUPPORT_CHAT = environ.get(
    "SUPPORT_CHAT", "https://t.me/" #REPLACE WITH YOUR SUPPORT GROUP URL
)  # Support group link ( make sure bot is admin )
# ---------------------------------------------------------------
# ---------------------------------------------------------------
IS_VERIFY = is_enabled("IS_VERIFY", False)
# ---------------------------------------------------------------
TUTORIAL = environ.get("TUTORIAL", "") #VERIFICATION TUTORIAL VIDEO URL, REPLACE ALL WITH YOURS
VERIFY_IMG = environ.get(
    "VERIFY_IMG", "https://graph.org/file/9266bb9610db7076db83e-daa28a55664d281cdd.jpg"
)
SHORTENER_API = environ.get("SHORTENER_API", "305c04c718a750820c9ca376a86999139757fb88") #REPLACE WITH YOURS
SHORTENER_WEBSITE = environ.get("SHORTENER_WEBSITE", "onylinks.com")    #REPLACE WITH YOURS
SHORTENER_API2 = environ.get(
    "SHORTENER_API2", "305c04c718a750820c9ca376a86999139757fb88"    #REPLACE WITH YOURS
)
SHORTENER_WEBSITE2 = environ.get("SHORTENER_WEBSITE2", "onylinks.com")  #REPLACE WITH YOURS
SHORTENER_API3 = environ.get(
    "SHORTENER_API3", "305c04c718a750820c9ca376a86999139757fb88"    #REPLACE WITH YOURS
)
SHORTENER_WEBSITE3 = environ.get("SHORTENER_WEBSITE3", "onylinks.com")  #REPLACE WITH YOURS
TWO_VERIFY_GAP = int(environ.get("TWO_VERIFY_GAP", "43200")) #ACCORDING TO YOUR NEEDS
THREE_VERIFY_GAP = int(environ.get("THREE_VERIFY_GAP", "43200"))
# ---------------------------------------------------------------
# ---------------------------------------------------------------
LANGUAGES = [
    "hindi",
    "english",
    "telugu",
    "tamil",
    "kannada",
    "malayalam",
    "bengali",
    "marathi",
    "gujarati",
    "punjabi",
]
QUALITIES = [
    "HdRip",
    "web-dl",
    "bluray",
    "hdr",
    "fhd",
    "240p",
    "360p",
    "480p",
    "540p",
    "720p",
    "960p",
    "1080p",
    "1440p",
    "2K",
    "2160p",
    "4k",
    "5K",
    "8K",
]
YEARS = [f"{i}" for i in range(2024, 2002, -1)]
SEASONS = [f"season {i}" for i in range(1, 23)]
REF_PREMIUM = 30
PREMIUM_POINT = 1500
# ---------------------------------------------------------------
AUTH_CHANNEL = (
    int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
)
REQUEST_CHANNEL = (
    int(request_channel)
    if request_channel and id_pattern.search(request_channel)
    else None
)
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
START_IMG = (
    environ.get(
        "START_IMG",
        "https://graph.org/file/32b9bf755081904ce1a24-8a2e0bbfb0f6aecf74.jpg",
    )
).split()
FORCESUB_IMG = environ.get(
    "FORCESUB_IMG",
    "https://graph.org/file/b1719b0e381734807346f-52c6cd31fb2a45ae69.jpg",
)
REFER_PICS = (
    environ.get(
        "REFER_PICS",
        "https://graph.org/file/1c4cf372ce1109e0f6ff5-da5c97f19c9b3b4d9a.jpg",
    )
).split()
PAYPICS = (
    environ.get(
        "PAYPICS", "https://graph.org/file/5ff54b7c9fc1df3a740c9-79096e249ec76eaf71.jpg"
    )
).split()
SUBSCRIPTION = environ.get(
    "SUBSCRIPTION",
    "https://graph.org/file/ad4e09300d7ea6a5c3690-bac51e292c523fa327.jpg",
)
REACTIONS = ["👀", "😱", "🔥", "😍", "🎉", "🥰", "😇", "⚡"]
# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
FILE_AUTO_DEL_TIMER = int(environ.get("FILE_AUTO_DEL_TIMER", "300"))
AUTO_FILTER = is_enabled("AUTO_FILTER", True)
IS_PM_SEARCH = is_enabled("IS_PM_SEARCH", True)
PORT = environ.get("PORT", "5000")
MAX_BTN = int(environ.get("MAX_BTN", "8"))
AUTO_DELETE = is_enabled("AUTO_DELETE", True)
DELETE_TIME = int(environ.get("DELETE_TIME", 300))
IMDB = is_enabled("IMDB", False)
FILE_CAPTION = environ.get("FILE_CAPTION", f"{script.FILE_CAPTION}")
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", f"{script.IMDB_TEMPLATE_TXT}")
LONG_IMDB_DESCRIPTION = is_enabled("LONG_IMDB_DESCRIPTION", False)
PROTECT_CONTENT = is_enabled("PROTECT_CONTENT", False)
SPELL_CHECK = is_enabled("SPELL_CHECK", True)
LINK_MODE = is_enabled("LINK_MODE", False)

# ---------------------------------------------------------------
# ---------------------------------------------------------------
# ---------------------------------------------------------------
STREAM_MODE = bool(environ.get("STREAM_MODE", True))  # Set True or Flase
# Online Stream and Download

MULTI_CLIENT = True
SLEEP_THRESHOLD = int(environ.get("SLEEP_THRESHOLD", "60"))
PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
if "DYNO" in environ:
    ON_HEROKU = True
else:
    ON_HEROKU = False
URL = environ.get("FQDN", "https://cloudy-drucie-bbhub-896535c0.koyeb.app/")

# ---------------------------------------------------------------
# ---------------------------------------------------------------
SETTINGS = {
    "spell_check": SPELL_CHECK,
    "auto_filter": AUTO_FILTER,
    "file_secure": PROTECT_CONTENT,
    "auto_delete": AUTO_DELETE,
    "template": IMDB_TEMPLATE,
    "caption": FILE_CAPTION,
    "tutorial": TUTORIAL,
    "shortner": SHORTENER_WEBSITE,
    "api": SHORTENER_API,
    "shortner_two": SHORTENER_WEBSITE2,
    "api_two": SHORTENER_API2,
    "log": LOG_VR_CHANNEL,
    "imdb": IMDB,
    "link": LINK_MODE,
    "is_verify": IS_VERIFY,
    "verify_time": TWO_VERIFY_GAP,
    "shortner_three": SHORTENER_WEBSITE3,
    "api_three": SHORTENER_API3,
    "third_verify_time": THREE_VERIFY_GAP,
}
