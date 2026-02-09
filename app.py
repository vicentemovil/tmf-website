from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)


@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}


@app.before_request
def redirect_www():
    host = request.host
    if host.startswith("www."):
        return redirect(
            request.url.replace(host, host[4:], 1),
            code=301
        )


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
