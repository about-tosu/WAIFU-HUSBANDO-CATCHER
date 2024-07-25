class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6848223695"
    sudo_users = "6848223695"
    GROUP_ID = -1002023182491
    TOKEN = "7483313486:AAFcCLC28lL5I16Y3XrAAkcb9UVUpQ3hsqI"
    mongo_url = "mongodb+srv://botmaker9675208:botmaker9675208@cluster0.sc9mq8b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://graph.org/file/a436ca4a5af069d400f9d.jpg", "https://graph.org/file/47039f027d6b95345b29d.jpg"]
    SUPPORT_CHAT = "Nothing_waifu_support"
    UPDATE_CHAT = "Nothing_waifu_support"
    BOT_USERNAME = "Nothing_waifu_bot"
    CHARA_CHANNEL_ID = "-1002236086617"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
