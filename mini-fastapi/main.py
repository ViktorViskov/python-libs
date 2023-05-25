from sys import argv

from web_app import WebApp

# init modules
#
#

# init web app
app = WebApp(host_addr="0.0.0.0", port=3000)

# run web server
if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage")
        print("main.py dev - for development")
        print("main.py prod - for production")
        exit(0)

    if "dev" in argv:
        app.start("main:app.server", development=True)
    elif "prod":
        app.start("main:app.server")

