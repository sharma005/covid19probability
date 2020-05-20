from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def hello_world():
    if request.method == "POST":
        print(request.form)
    
    return render_template('index.html')


def getData(url):
    r = requests.get(url)
    return r.text

@app.route('/coronaupdate.html')
def coronaupdate():

    myHtmlData = getData('https://www.mohfw.gov.in/')
    soup = BeautifulSoup(myHtmlData,'html.parser')
    html_text = str(soup.prettify())
   
    soupset = soup.find_all('tbody')
    table_data  = str(soupset[0])
    
    f = open("templates/coronaupdate.html","w") 
    f.write('''<html> 
<head> 
    <title> Corona latest update</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
    <style>
        *{margin: 0; padding: 0; box-sizing: border-box;font-family: 'Muli', sans-serif; scroll-behavior: smooth;}

        .nav_style
        {
            background-color: #a29bfe!important;
            position: absolute;
            
        }

        .nav_style a{
            color: #f1f1f1;
            
        
        }
    </style>
</head> 
<body>
   
    <table class="table table-bordered"  style="font-weight:bold>
    <table  stylefont-weight:bold">
    <thead>
	<tr>
	<th><strong>S. No.</strong></th>
	<th><strong>Name of State / UT</strong></th>
	<th><strong>Total Confirmed cases (Including 51 foreign Nationals) </strong></th>                              
	<th><strong>Cured/Discharged/<br>Migrated</strong></th>
	<th><strong>Death</strong></th>
	</tr>
</thead>
    '''
                    + table_data + 
    '''</table>
    
    </body> 
</html>''')
    f.close()
    return render_template('coronaupdate.html')

if __name__ == '__main__':
    app.run(debug=True)
   
