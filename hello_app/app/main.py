from flask import Flask

app = Flask(__name__)

@app.route("/argocd")
def argocd_msg():
    return "Isn't ArgoCD pretty amazing?"

@app.route("/")
def home():
    return "Hello World! Deployed using Argo CD!"

if __name__ == "__main__":
    app.run(host='0.0.0.0')