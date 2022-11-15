from flask import Flask, render_template
import requests

fake_blogs = "https://api.npoint.io/c790b4d5cab58020d391"

response = requests.get(fake_blogs)
blog_posts = response.json()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", posts = blog_posts)

@app.route('/<int:id>')
def post_body(id):
    return render_template("post.html", post = blog_posts[id - 1])

if __name__ == "__main__":
    app.run(debug=True)
