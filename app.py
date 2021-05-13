from flask import Flask, render_template
import requests
import json


app = Flask(__name__)

@app.route("/", methods=['GET'])
def load_data():
    req_categories = requests.get('https://run.mocky.io/v3/522a71cd-e4bf-4906-8277-893233d8abc9')
    categories_data = req_categories.content.decode('utf-8')
    categories_data= categories_data.replace("payload:", "\"payload\":\n")
    categories_data = json.loads(categories_data)
    print(categories_data['payload'][0]['name']) 

    req_product = requests.get('https://run.mocky.io/v3/89f9993c-bb88-4270-ac82-62cae14ae9bd')
    product_data = req_product.content.decode('utf-8')
    product_data= product_data.replace("payload:", "\"payload\":\n")
    product_data = json.loads(product_data)
    print(product_data['payload'][0]['name']) 


    
    return render_template('index.html', categories=categories_data['payload'],products=product_data['payload'])