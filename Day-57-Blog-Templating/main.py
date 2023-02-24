from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/post/<blog_id>')
def get_blog_post(blog_id):
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blog_url)
    post_data = response.json()[int(blog_id)-1]
    post = Post(title=post_data["title"], subtitle=post_data["subtitle"], body=post_data["body"])
    return render_template("post.html", title=post.title, subtitle=post.subtitle, body=post.body)

if __name__ == "__main__":
    app.run(debug=True)