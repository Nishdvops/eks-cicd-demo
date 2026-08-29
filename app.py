from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <html>
        <head>
            <title>EKS CI/CD Demo</title>
        </head>
        <body>
            <h1>Hello from AWS EKS!</h1>
            <p>
                This application was deployed using GitHub Actions,
                Docker, Helm and Kubernetes.
            </p>
        </body>
    </html>
    """


@app.route("/health")
def health():
    return jsonify(status="healthy"), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
