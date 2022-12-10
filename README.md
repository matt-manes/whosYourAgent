# whosYourAgent
Install with<br>
<pre>python -m pip install git+https://github.com/matt-manes/whosYourAgent</pre>
Git must be installed and in your PATH.<br><br>

Simple module to generate random useragent strings.<br>
Contains an auto-updater that will periodically update the browser version data to the latest version numbers.<br>
<br>
Usage:
<pre>
from whosYourAgent import getAgent
print(getAgent())
</pre>
produces:
<pre>
Mozilla/5.0 (Windows NT 11.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.5359.98 Safari/537.36 Vivaldi/5.6
</pre>

