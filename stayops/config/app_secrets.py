# stayops/config/app_secrets.py
import os, time

dotenv_path = '.env'
with open(dotenv_path) as f:
    for line in f:
        if line.strip() and not line.startswith('#'):
            key, value = line.strip().split('=', 1)
            globals()[key] = value

stayops_dbuser = globals().get("stayops_dbuser")
stayops_dbpassword = globals().get("stayops_dbpassword")
stayops_dbhost = globals().get("stayops_dbhost")
try:
    stayops_dbport = int(globals().get("stayops_dbport"))
except:
    stayops_dbport = globals().get("stayops_dbport")
stayops_dbname = globals().get("stayops_dbname")


