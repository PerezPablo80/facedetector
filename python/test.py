import os
from dotenv import load_dotenv
load_dotenv()

test= os.getenv("TEST")
print(test)