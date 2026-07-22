# Asynchronous Media Archival Client (AMAC)

An event-driven, non-blocking Python client built on top of the MTProto protocol using the Telethon framework. This utility is designed to handle high-performance, asynchronous media extraction and local data serialization directly from verified user network sessions.

## 🚀 Core Features

- **Asynchronous Architecture:** Utilizing Python's `asyncio` engine for non-blocking I/O operations and optimized asset streaming.
- **Event-Driven Execution:** Real-time event listeners targeting explicit secure chat states.
- **Regex Parsing Engine:** Advanced pattern matching for robust URL sanitation and extraction validation.
- **Session Persistence:** Secure, local state management via MTProto session keys, eliminating recurring authorization overhead.

## 🛠️ Technical Stack

- **Language:** Python 3.10+
- **Protocol:** Telegram MTProto API
- **Primary Framework:** Telethon (Asynchronous Client Library)
- **Data Handling:** Regular Expressions (`re`), OS File Stream Serialization

## 📦 Installation & Setup

### 1. Environment Initialization
Clone this repository or download the source code locally, then install the required protocol dependencies:
```bash
pip install telethon
```

### 2. Credential Configuration
Acquire your development application authorization keys from the official API portal at [my.telegram.org](https://telegram.org). Update the configuration block at the root level of `userbot.py`:

```python
API_ID = 11111111  # Enforced unique identifier
API_HASH = "YOUR_SECURE_API_HASH"  # Encrypted transport key
```

### 3. Execution
Launch the asynchronous runtime loop via your local terminal:
```bash
python userbot.py
```
*Note: Upon initial execution, the terminal will prompt for multi-factor authentication (Phone/OTP) to securely provision your local `.session` persistence file layer.*

## 📖 Usage Implementation

Once the background client event loop goes live, interface with the engine by issuing a parse instruction from your personal account console:

```text
/getmedia https://t.me[target_channel_id]/[message_id]
```

Extracted binaries will automatically stream and serialize into the designated `/Downloads` directory path.

## 🔒 Security & Scope Disclaimer

This project is engineered strictly for educational, personal archival, and automated data recovery research purposes. The user assumes full structural compliance responsibility regarding platform-specific Terms of Service (ToS) and digital asset access rights.
