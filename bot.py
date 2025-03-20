import os
import logging
import pymongo
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# ✅ Load environment variables from .env file
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

# ✅ Check if environment variables are loaded
if not all([BOT_TOKEN, MONGO_URI, DB_NAME, COLLECTION_NAME]):
    raise ValueError("❌ ERROR: Missing environment variables. Check your .env file.")

# ✅ Setup logging for debugging
logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

# ✅ Connect to MongoDB
try:
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    logging.info("✅ Connected to MongoDB successfully!")
except Exception as e:
    logging.error(f"❌ MongoDB Connection Error: {e}")
    raise

# ✅ Start command
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text("👋 Welcome! Send a mobile number to search in the database.")

# ✅ Search database by mobile number (_id)
async def search_db(update: Update, context: CallbackContext) -> None:
    mobile_number = update.message.text.strip()

    # ✅ Ensure input is a valid number
    if not mobile_number.isdigit():
        await update.message.reply_text("⚠️ Please enter a valid mobile number.")
        return

    try:
        # ✅ Search MongoDB where _id is the mobile number (stored as string)
        result = collection.find_one({"_id": mobile_number})

        if result:
            response = "✅ *Data Found:*\n\n"
            for key, value in result.items():
                response += f"🔹 *{key.capitalize()}:* {value}\n"
            await update.message.reply_text(response, parse_mode="Markdown")
        else:
            await update.message.reply_text("❌ Data not found.")

    except Exception as e:
        logging.error(f"❌ Database error: {e}")
        await update.message.reply_text(f"⚠️ Error: {e}")

# ✅ Error handler
async def error_handler(update: object, context: CallbackContext) -> None:
    logging.error(f"⚠️ Error: {context.error}")

# ✅ Main function to run the bot
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, search_db))
    app.add_error_handler(error_handler)

    logging.info("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
