from flask import Flask
app = Flask(__name__)
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
else if app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

@app.route('/')
def hello():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
