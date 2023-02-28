from flask import Flask, render_template
import requests

blog_url = "https://api.npoint.io/3a99207ce70b558d517d"
response = requests.get(blog_url)
all_posts = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts=all_posts)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

@app.route('/post/<blog_id>')
def post(blog_id):
    post_data = response.json()[int(blog_id)-1]
    return render_template("post.html", post=post_data)

if __name__ == "__main__":
    app.run(debug=True)