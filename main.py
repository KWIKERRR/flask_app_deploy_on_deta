from flask import Flask, render_template, request
import requests

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