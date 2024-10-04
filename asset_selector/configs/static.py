"""Test file."""

import os

import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Date
TODAY = pd.Timestamp.today()

# Miscellaneous
SMILEY = "\N{GRINNING FACE}"


# ETL constants
positiv_liste_url = "https://skat.dk/erhverv/ekapital/vaerdipapirer/beviser-og-aktier-i-investeringsforeinger-og-selskaber-ifpa"

X_OPENFIGI_APIKEY = os.environ.get("X_OPENFIGI_APIKEY", False)
