from .whosYourAgent import updateAll, getAgent
import os
from pathlib import Path
import time

browsersPath = Path(__file__).parent/'browserVersions.json'
try:
    if time.time() - os.stat(str(browsersPath)).st_mtime > 604800: #1week
        updateAll()
except Exception as e:
    print(f'Error updating browser versions for whosYourAgent:')
    print(e)
