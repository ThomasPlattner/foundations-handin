from flask import Blueprint, render_template
from .models import Article

blueprint = Blueprint('articles', __name__)

@blueprint.route('/blog/<slug>')
def blog(slug):
    blogs = Article.query.all()
    for article in blogs:
        if slug.title() == article.title:
            url = "articles/" + slug.lower() + ".html"
            return render_template(url)
            break
    else:
        message = "Sorry, we couldn't find the article about " + slug + " :( "
        return render_template('/base.html', message=message) 

@blueprint.route('/run-seed')
def run_seed():
    import app.scripts.seed
    return 'Database seed completed'