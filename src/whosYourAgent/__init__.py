from .whosYourAgent import updateAll, getAgent
import os
from pathlib import Path
import time

browsersPath = Path(__file__).parent/'browserVersions.json'
try:
    if not browsersPath.exists()\
    or time.time() - os.stat(str(browsersPath)).st_mtime > 1440: #1day
        updateAll()
except Exception as e:
    print(f'Error updating browser versions for whosYourAgent:')
    print(e)
