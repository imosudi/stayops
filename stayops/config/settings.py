# stayops/config/settings.py

import os

from stayops.config.app_secrets import stayops_dbuser, stayops_dbpassword, stayops_dbhost, stayops_dbport, stayops_dbname


DATABASE_URI = os.getenv(
    "DATABASE_URI",
    f"postgresql://{stayops_dbuser}:{stayops_dbpassword}@{stayops_dbhost}:{stayops_dbport}/{stayops_dbname}"
    #"sqlite:///stayops.db"

)

'''print(stayops_dbuser)
print(stayops_dbpassword)
print(stayops_dbhost)
print(stayops_dbport)
print(stayops_dbname)'''