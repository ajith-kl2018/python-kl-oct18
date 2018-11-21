from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "<b>Hello World!</b>"

@app.route("/goodbye")
def goodbye():
    return "<strong>Goodbye World!</strong>"

@app.route("/")
def formPage():
    return render_template('formPage.html')

@app.route("/submit",methods=['POST'])
def submitPage():
    txtValue = request.form['txtName']
    print ("recieved:" + txtValue);
    #return "<h1>Thank you for </h1>, : <strong>" + txtValue + "</strong>"
    return render_template('submitPage.html',inputName=txtValue)

if __name__ == "__main__":
    app.run()



