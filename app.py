from flask import Flask, render_template   

app = Flask(__name__)    



@app.route('/')
def index():
    return render_template('index.html')  

@app.route('/dynamic/<num>/<num2>/<color1>/<color2>')
def dynamic(num,num2,color1,color2):
    return render_template('dynamic.html',num=int(num),num2=int(num2),color1=color1,color2=color2)

if __name__=="__main__":   
    app.run(debug=True)    