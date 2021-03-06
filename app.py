from flask import Flask, render_template, request, json
import requests
from time import strftime
from time import gmtime

app = Flask(__name__)
r = requests
@app.route("/", methods = ["post", "get"])
def index():

    if(request.form.get('search') == None or request.form.get('search') == ""):
        data = {}
        data['cod'] = 401
        return render_template("index.html", data=data)
    else:
        location = request.form.get('search')
        link = "http://api.openweathermap.org/data/2.5/weather?q={},gb&appid=241d84ab30d60c4945a77350032fc958" . format(location)
        res = r.get(link)
        data = json.loads(res.text)
        data['main']['temp'] = round(data['main']['temp'] - 273.15, 2)
        data['main']['feels_like'] = round(data['main']['feels_like'] - 273.15, 2)
        data['sys']['sunset'] = strftime("%H:%M", gmtime(data['sys']['sunset']))
        data['sys']['sunrise'] = strftime("%H:%M", gmtime(data['sys']['sunrise']))
        if not data:
            return render_template("index.html", result="empty", data=data)
        else:
            return render_template("index.html", result="success", data=data)


