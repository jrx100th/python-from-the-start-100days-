from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()


# static folder for images, css js videos and all static files
# templates for html etc



# DAY 57

# is flask is something similar to node js
# jinja is something similar to ejs files

# jinja comes along with flask, so extra pip install