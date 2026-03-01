from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "CI Advanced - DockerHub Auto Push with SHA Tagging 🚀"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
