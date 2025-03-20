# Teligram-bot
Telegram bot that is used to print data from the mango db database
📜 README.md
markdown
Copy code
# 📞 Telegram Bot with MongoDB Search

This is a Telegram bot that allows users to search a MongoDB database using a mobile number.  
If the number exists, the bot returns all associated details.  
If not, it replies with "❌ Data not found."

---

## 🚀 Features
- 🔍 Search MongoDB using a mobile number (_id)
- ✅ Handles errors gracefully
- 🛠 Easy to set up and deploy
- 🔄 Automatically reconnects to MongoDB

---

## 📌 Setup & Installation

## 1️⃣ Clone the Repository
```
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```


2️⃣ Install Dependencies##
```
pip install -r requirements.txt
```

3️⃣ Create a .env File
```
Create a .env file in the project directory and add your credentials:

BOT_TOKEN=your-telegram-bot-token
MONGO_URI=mongodb://localhost:27017/
DB_NAME=your_database_name
COLLECTION_NAME=your_collection_name
```
4️⃣ Run the Bot
```
Copy code
python bot.py
```
🎮 How to Use
1️⃣ Start the Bot
```
Send /start to see a welcome message.
```
2️⃣ Search a Number
```
Send a mobile number (e.g., 9692307299) to search in the database.
```
3️⃣ Response Examples
If found:

✅ Data Found:
🔹 Name: John Doe
🔹 Email: johndoe@example.com
🔹 City: New York
If not found:

Copy code
❌ Data not found.

###⚙️ Deployment (Optional)
Deploy on a Linux Server (Auto-Restart)
Run the bot using screen


Copy code
```
screen -S telegram-bot
python bot.py
Press CTRL + A, then D to detach.

To restart the bot automatically if it crashes, use:

while true; do python3 bot.py; sleep 5; done
```

🛠 Troubleshooting
Bot not responding?
Check if BOT_TOKEN is correct.
Ensure MongoDB is running (systemctl start mongod).
MongoDB connection error?
Verify MONGO_URI in .env file.

🤝 Contributing
Fork the repo
Create a new branch (git checkout -b feature-branch)
Commit changes (git commit -m "Added feature")
Push (git push origin feature-branch)
Open a Pull Request 🚀

📜 License
This project is open-source under the MIT License.

⭐️ Show Some Love!
If you found this project useful, give it a star ⭐️ on GitHub!


