class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6848223695"
    sudo_users = "6848223695"
    GROUP_ID = -1002332668271
    TOKEN = "7633847547:AAHSOz3bzzx8iyX61kg8-RSnMHPNxGTPgpM"
    mongo_url = "postgres://koyeb-adm:yZubkimC56DR@ep-rapid-poetry-a2nmt031.eu-central-1.pg.koyeb.app/koyebdb"
    PHOTO_URL = ["https://graph.org/file/a436ca4a5af069d400f9d.jpg", "https://graph.org/file/47039f027d6b95345b29d.jpg"]
    SUPPORT_CHAT = "Nothing_waifu_support"
    UPDATE_CHAT = "Nothing_waifu_support"
    BOT_USERNAME = "waifu_12345_bot"
    CHARA_CHANNEL_ID = "-1002251479334"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
