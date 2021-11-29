from os import getenv


c.NotebookApp.ip = "0.0.0.0"
c.NotebookApp.port = int(getenv("NOTEBOOK_PORT"))
c.NotebookApp.open_browser = False
c.NotebookApp.allow_root = True
