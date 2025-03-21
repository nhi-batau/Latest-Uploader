import os

API_ID = os.environ.get("API_ID", "20114039")

API_HASH = os.environ.get("API_HASH", "87297b8f3cc8fc9bbce591ad30da5896")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7822801684:AAE4y0ETMqA12Y8xakRofTfWIsEG3IGXhYw")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 8172163893))

LOG = -1002159628443,

# UPDATE_GRP = , # bot sat group

# auth_chats = []

try:
    ADMINS=[7827463899]
    for x in (os.environ.get("ADMINS", "8172163893").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)
