import os
from dotenv import load_dotenv
from vnexpress import VnExpress
from const import *

# Load environment variables from .env file
load_dotenv()

if __name__ == "__main__":
    # Get all the constants with the "VNEXPRESS_" prefix
    vnexpress_items = {key: value for key, value in globals().items() if key.startswith("VNEXPRESS_")}

    # Get database configuration from environment variables
    db_host = os.getenv("DB_HOST")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    db_table = os.getenv("DB_TABLE")
    vnexpress = VnExpress("")

    for key, value in vnexpress_items.items():
        # Exclude the item with value 'VNEXPRESS_TINNOIBAT'
        if value == VNEXPRESS_TINNOIBAT:
            vnexpress.check_and_process_hotnews(db_host, db_user, db_password, db_name, db_table)
            continue

        # Call save_to_mysql for each item
        vnexpress.rss_url = value
        vnexpress.save_to_mysql(db_host, db_user, db_password, db_name, db_table)