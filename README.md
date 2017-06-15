For windows users:

Delete line 7 and add this lines:

import os<br>
phantomjs_path = "C:\YOUR_PATH\phantomjs.exe"<br>
driver = webdriver.PhantomJS(executable_path=phantomjs_path, service_log_path=os.path.devnull)
