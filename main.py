from flask import Flask, render_template, request
import requests
from oauthlib.oauth2 import WebApplicationClient
import datetime
from pytrends.request import TrendReq

app = Flask(__name__)

@app.route('/', methods=["GET"])
def hello_world():
 prefix_google = """
 <!-- Google tag (gtag.js) -->
<script async
src="https://www.googletagmanager.com/gtag/js?id=UA-250914721-1"></script>
<script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){dataLayer.push(arguments);}
 gtag('js', new Date());
 gtag('config', ' UA-250914721-1');
</script>
 """
 return prefix_google + "Hello World"


@app.route('/Logger', methods=["GET"])
def logger() :
    print('echo')
    return 'Check your console !' + render_template('log.html')

@app.route('/requestGoogle')
def reqGA():
    req = requests.get("https://www.google.com/")
    print(req)
    return req.cookies.get_dict()

@app.route('/requestGA')
def myreqGA():
    req = requests.get('https://analytics.google.com/analytics/web/#/a250914721w345009383p281161749')
    print(req)
    return req.text

@app.route('/pytrends')
def googletrendchart():
    pytrends = TrendReq()
    pytrends.build_payload(kw_list=["Lebron James", "Devin Booker"], timeframe='today 90-d', geo='FR')
    df = pytrends.interest_over_time()
    data_1 = df['Lebron James'].tolist()
    data_2 = df['Devin Booker'].tolist()
    data_date = df.index.values.tolist()
    timestamp_in_seconds = [element/1e9 for element in data_date]
    date = [datetime.fromtimestamp(element)for element in timestamp_in_seconds]
    days = [element.date() for element in date]
    months = [element.isoformat() for element in days]
    params = {
        "type": 'line',
        "data": {
            "labels": months,
            "datasets": [{
                "label": 'Lionel Messi',
                "data": data_1,
                "borderColor": '#3e95cd',
                "fill": 'false',
            },
                {
                "label": 'Cristiano Ronaldo',
                "data": data_2,
                "borderColor": '#ffce56',
                "fill": 'false',
            }
            ]
        },
        "options": {
            "title": {
                "text": 'Comparaison'
            },
            "scales": {
                "yAxes": [{
                    "ticks": {
                        "beginAtZero": 'true'
                    }
                }]
            }
        }
    }

    prefix_chartjs = """
        <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.5.0/Chart.min.js"></script>
         <canvas id="myChart" width="1200px" height="700px"></canvas>""" + f"""
        <script>
        var ctx = document.getElementById('myChart');
        var myChart = new Chart(ctx, {params});
        </script>
        """

    return prefix_chartjs
