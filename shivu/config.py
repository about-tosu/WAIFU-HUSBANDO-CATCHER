class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6848223695"
    sudo_users = "6968763387"
    GROUP_ID = -1002023182491
    TOKEN = "6850137736:AAGBOBgnxK6SV2LhDNE0HvweCmgOS1Bc9o4"
    mongo_url = "mongodb+srv://botmaker9675208:botmaker9675208@cluster0.sc9mq8b.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    PHOTO_URL = ["https://graph.org/file/a436ca4a5af069d400f9d.jpg", "https://graph.org/file/47039f027d6b95345b29d.jpg"]
    SUPPORT_CHAT = "waifu_catcher_support_pills"
    UPDATE_CHAT = "waifu_catcher_support_pills"
    BOT_USERNAME = "waifu_catcher_pills_bot"
    CHARA_CHANNEL_ID = "-1002023182491"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
