from utils.gpt import askGPT
from utils.scrap import scrape_all_pages, estimate_tokens

from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


## init

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def gpt3():
    response = []
    if request.method == 'POST':
        url = request.form['url']
        prompt = request.form['prompt']
        website_content = scrape_all_pages(url)
        website_content = website_content[:7000]
        response = askGPT(website_content, prompt)
        return render_template('index.html', response=response)
    else:
        return redirect(url_for('index'))
    


if __name__ == '__main__':
    app.run(debug=True)

