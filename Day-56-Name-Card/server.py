from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

# Checks app is in current file, not from an imported module
if __name__ == '__main__':
    # Activate debug mode, allows you to make changes and see it without you having to stop/start the file
    app.run(debug=True)