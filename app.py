from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/enterprise")
def enterprise():
    return render_template("enterprise.html")

@app.route("/candidate")
def candidate():
    return render_template("candidate.html")

@app.route("/mentor")
def mentor():
    return render_template("mentor.html")

@app.route("/labadmin")
def lab_admin():
    return render_template("lab_admin.html")

@app.route("/systemadmin")
def system_admin():
    return render_template("system_admin.html")

if __name__ == "__main__":
    # host='0.0.0.0' cho phép truy cập qua địa chỉ IP của máy tính
    app.run(debug=True, host='0.0.0.0', port=1411)