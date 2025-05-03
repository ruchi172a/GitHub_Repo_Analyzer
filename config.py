import os
from dotenv import load_dotenv
import yaml

# Load from .env
load_dotenv()
GITHUB_TOKEN = os.getenv("MY_GITHUB_PAT")

# Load from config.yaml
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

ORG_NAME = config["org_name"]
OUTPUT_CSV = config["output_csv"]
