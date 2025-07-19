from flask import Flask, render_template, request, redirect
from utils import sheet_handler
from utils.zoning import categorize_postcode
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        phone = request.form["phone"]
        postcode = request.form["postcode"]
        service = request.form["service"]
        date = request.form["date"]
        time = request.form["time"]
        zone = categorize_postcode(postcode)

        if sheet_handler.is_slot_available(date, time, zone, service):
            sheet_handler.save_booking(name, phone, postcode, service, date, time, zone)
            return redirect("/success")
        else:
            return render_template("index.html", error="Slot unavailable", zone=zone)

    return render_template("index.html")

@app.route("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
