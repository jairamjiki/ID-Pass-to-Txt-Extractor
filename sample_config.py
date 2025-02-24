import os

api_id = 21705536
api_hash = os.environ.get("API_HASH", "c5bb241f6e3ecf33fe68a444e288de2d")
bot_token = os.environ.get("BOT_TOKEN")
auth_users = os.environ.get("AUTH_USERS", "5591734243,1369808729,5957208798")
sudo_users = [int(num) for num in auth_users.split(",")]
osowner_users = os.environ.get("OWNER_USERS", "5591734243,1369808729,5957208798")
owner_users = [int(num) for num in osowner_users.split(",")]
