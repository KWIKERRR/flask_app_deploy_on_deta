from flask import Flask, render_template

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
    print('simple echo')
    return 'Check your console !' + render_template('templates/log.html')