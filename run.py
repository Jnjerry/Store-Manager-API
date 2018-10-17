#serves as an entry point to our application
#it gets a copy of the app package and runs it

import os

from app import create_app

config = os.getenv('APP_SETTINGS')
app = create_app(config)

if __name__ == "__main__":
    app.run(debug=True)
