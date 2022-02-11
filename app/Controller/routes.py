from __future__ import print_function
import sys
from flask import Blueprint
from flask import render_template, flash, redirect, url_for, request
#from flask.cli import routes_command
from config import Config
from flask_login import current_user, login_required

#Other routes
from app import db
from app.Model.models import Post, Tag
from app.Controller.forms import PostForm, SortForm

bp_routes = Blueprint('routes', __name__)
bp_routes.template_folder = Config.TEMPLATE_FOLDER #'..\\View\\templates'


@bp_routes.route('/', methods=['GET'])
@bp_routes.route('/index', methods=['GET'])
@login_required
def index():
    sform= SortForm()
    posts = Post.query.order_by(Post.timestamp.desc())
    if sform.validate_on_submit():
        if sform.sort.filter.data == 'title':
            posts = Post.order_by (Post.title.desc())
        elif sform.sort.filter.data == 'likes':
            posts = Post.query.order_by(Post.likes.desc())
        elif sform.sort.filter.data == 'tags':
            posts = Post.query.order_by(Post.tags.desec())
        else: 
            posts = Post.query.order_by(Post.happiness_level.desc())
    return render_template('index.html', title="Smile Portal", posts=posts.all(), smile_cout= Post.query.count(), form=sform)

@bp_routes.route('/postsmile/', methods=['GET','POST'])
@login_required
def postsmile():
    pform = PostForm()
    if request.method == 'POST':
        if pform.validate_on_submit():
            current_user = Post(title = pform.title.data, body = pform.body.data, happiness_level = pform.happiness_level.data)
            for t in pform.tag.data:
                current_user.tags.append(t)
            db.session.add(current_user)
            db.session.commit()
            flash("The new smile post is created")
            return redirect(url_for('routes.index')) 
    else:
        return render_template('create.html', form = pform)

@bp_routes.route('/like/<post_id>',methods = ['POST'])
@login_required
def like(post_id):
    thepost = Post.query.filter_by(id = post_id).first()
    thepost.likes = thepost.likes+1
    db.session.commit()
    return redirect(url_for('routes.index'))

@bp_routes.route('/postags/<tag_id>', methods= ['POST'])
@login_required
def postags(tag_id):
    post_tags = Tag.query.get(id=tag_id).first()
    return render_template(
        '_post.html', 
        title='PhotoTags',
        message='Your application description page.',
        post_tags = post_tags
    )

@bp_routes.route('/delete/<post_id>', methods = ["DELETE",'POST'])
@login_required
def delete(post_id):
    thepost=Post.query.filter_by(id=post_id).first()
    t=thepost.tags
    if request.method == 'POST':
        for t in thepost.tags:
            thepost.tags.remove(t)
        db.session.delete(thepost)
        db.session.commit()
    flash('Your smile post'+thepost.title+'is delted')
    return redirect(url_for('routes.index'))
      






    



