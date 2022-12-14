import os
import time
from pathlib import Path

from .whosYourAgent import VersionUpdater, getAgent

browsersPath = Path(__file__).parent / "browserVersions.json"
try:
    if (
        not browsersPath.exists()
        or time.time() - os.stat(str(browsersPath)).st_mtime > 1440
    ):  # 1day
        updater = VersionUpdater()
        updater.updateAll()
except Exception as e:
    print(f"Error updating browser versions for whosYourAgent:")
    print(e)
