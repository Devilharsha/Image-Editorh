# By @Damantha_Jasinghe
from pyrogram import Client
import os

if bool(os.environ.get("WEBHOOK", False)):

if __name__ == "__main__":
    plugins = dict(root="plugins")

    app = Client(
        "TroJanz",
        bot_token=Config.TG_BOT_TOKEN,
        api_id=Config.APP_ID,
        api_hash=Config.API_HASH,
        plugins=plugins,
        workers=300,
    )
    app.run()
