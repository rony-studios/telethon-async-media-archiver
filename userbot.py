import os
import re
from telethon import TelegramClient, events

# ==========================================
# Secure Environment Configuration
# ==========================================
# Fetches credentials securely via system environment variables.
# NEVER hardcode production tokens or private API hashes directly into source control.
API_ID = int(os.getenv("TG_API_ID", 12345678))  # Replace 12345678 with your actual API_ID locally
API_HASH = os.getenv("TG_API_HASH", "YOUR_API_HASH_HERE")  # Replace with your actual API_HASH locally
SESSION_NAME = "userbot"
DOWNLOAD_FOLDER = "Downloads"

# Initialize local tracking persistence storage structure
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

def parse_message_link(link: str):
    """
    Regex parsing engine designed for robust token validation and routing.
    Supports standard tracking patterns:
    - Public: https://t.me
    - Private: https://t.me
    """
    username_pattern = r"https?://t\.me/([A-Za-z0-9_]+)/(\d+)"
    private_pattern = r"https?://t\.me/c/(\d+)/(\d+)"

    m = re.match(username_pattern, link)
    if m:
        username = m.group(1)
        message_id = int(m.group(2))
        return username, message_id

    m = re.match(private_pattern, link)
    if m:
        internal_id = m.group(1)
        message_id = int(m.group(2))
        # Structural conversion to resolve MTProto peer entities safely
        chat_id = int("-100" + internal_id)
        return chat_id, message_id

    return None, None

@client.on(events.NewMessage(chats="me"))
async def handler(event):
    """
    Event-driven asynchronous execution controller.
    Restricts ingestion triggers strictly to verified console instances ("me").
    """
    text = event.raw_text.strip()
    if not text.startswith("/getmedia"):
        return

    parts = text.split(maxsplit=1)
    if len(parts) != 2:
        await event.reply("Usage:\n/getmedia <telegram_message_link>")
        return

    link = parts[1]
    entity, message_id = parse_message_link(link)
    
    if entity is None:
        await event.reply("Invalid Telegram message link schema configuration.")
        return

    try:
        message = await client.get_messages(entity, ids=message_id)
        if message is None:
            await event.reply("Error: Remote message packet entity not found.")
            return

        if not message.media:
            await event.reply("Error: Target state stream contains zero download media payloads.")
            return

        await event.reply("Asynchronous network download pipeline initialized...")
        
        file_path = await client.download_media(
            message, 
            file=DOWNLOAD_FOLDER
        )
        
        await event.reply(f"Data stream serialized successfully:\nPath: {file_path}")
        
    except Exception as e:
        await event.reply(f"Runtime Exception Intercepted:\n{e}")

async def main():
    print("Userbot core engine initializing successfully...")
    print("Awaiting input events in your Saved Messages interface:")
    print("/getmedia https://t.me...")
    await client.start()
    await client.run_until_disconnected()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
