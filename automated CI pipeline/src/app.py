from flask import Flask
from routes.main import main_blueprint

app = Flask(__name__)
app.register_blueprint(main_blueprint)

@app.route("/health")
def health_check():
    return {"status": "OK", "message": "App is healthy"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
