import os

OFFICIAL_BSCCS_DC_WEBHOOK = os.environ.get("OFFICIAL_BSCCS_DC_WEBHOOK")
UNOFFICIAL_BSCCS_DC_WEBHOOK = os.environ.get("UNOFFICIAL_BSCCS_DC_WEBHOOK")

HEADERS = {"content-type": "application/json"}
MAX_SEND_TRIES = 3

IGNORE_TITLES = ["WhatsApp"]
