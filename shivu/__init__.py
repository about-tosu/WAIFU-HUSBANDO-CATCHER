import logging  


logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID =["6965147961","6848223695"]
SUDO_USERS = ["6848223695","6965147961","5458968679","6864672519"]
GROUP_ID = -1002332668271
TOKEN = "7633847547:AAHSOz3bzzx8iyX61kg8-RSnMHPNxGTPgpM" 
mongo_url = "postgres://koyeb-adm:yZubkimC56DR@ep-rapid-poetry-a2nmt031.eu-central-1.pg.koyeb.app/koyebdb"
PHOTO_URL = ["https://envs.sh/nJo.jpg", "https://envs.sh/nJs.jpg"]
SUPPORT_CHAT = "-1002332668271"
UPDATE_CHAT = "-1002332668271"
BOT_USERNAME = "@SNATCH_YOURR_WAIFU_BOT"
CHARA_CHANNEL_ID = "-1002251479334"
api_id = "24835491"
api_hash = "04ee66f0079a9b11eefb33a89289899e" 


