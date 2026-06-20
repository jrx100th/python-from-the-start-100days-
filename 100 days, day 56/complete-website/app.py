from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Landing page - Retro DOOM themed personal intro + entry to the game."""
    return render_template('index.html')

@app.route('/doom')
def doom():
    """The actual playable DOOM clone."""
    return render_template('doom.html')

@app.route('/about')
def about():
    """Optional simple about using Jinja."""
    return render_template('about.html')

if __name__ == '__main__':
    # Run on 0.0.0.0 so it's accessible, debug on for development
    app.run(host='0.0.0.0', port=5000, debug=True)