from flask import Flask, render_template, request
from datetime import date, time, datetime
from summarisation import invoke_llm
  
now = datetime.now()
app = Flask(__name__)
@app.route('/', methods=['GET', 'POST'])

def create_app():
    if request.method == 'POST':
        print('POSTING Entered')
        completion = invoke_llm()
        return render_template('single.html', data=completion, current_timestamp = now)
        #return render_template('single.html')
    else:    
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

