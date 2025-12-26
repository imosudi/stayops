# stayops/config/settings.py

import os

DATABASE_URI = os.getenv(
    "DATABASE_URI",
    "postgresql://stayops:stayops@localhost:5432/stayops"
)
