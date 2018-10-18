#serves as an entry point to our application
#it gets a copy of the app package and runs it

from .app import create_app


CONFIG_NAME="development"
app = create_app(CONFIG_NAME)
# method to run the flask app
if __name__ == '__main__':
    app.run()
