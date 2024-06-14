import os
from dotenv import load_dotenv
load_dotenv()

BOT_TOKEN = str(os.getenv('BOT_TOKEN'))
TEST_PAY = str(os.getenv('TEST_PAY'))

