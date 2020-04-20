from flask import Flask
from default_endpoints import default_endpoints

app = Flask(__name__)

# Configuration
if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "testing":
    app.config.from_object("config.TestingConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

# Endpoints
app.register_blueprint(default_endpoints)


# Start the application
if __name__ == '__main__':
    app.run(host='0.0.0.0')
