from flask import Flask, render_template, request

app = Flask(__name__)

lines = []

@app.route('/')
def home():
    # with open("companysuffixfile.txt", "a+") as file_object:
    #     lines = file_object.read().splitlines()
    lines = ["First", "Second", "Third"]
    choosefile = request.form.get('exampleFormControlFile1')
    print(choosefile)
    return render_template("index.html", data = lines, file = choosefile)

if __name__ == '__main__':
    app.run()