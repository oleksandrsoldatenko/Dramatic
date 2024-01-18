from flask import Flask, render_template, request, redirect, session
from api import get_upcoming, get_popular, get_movie_details, get_similar_movies, get_movie_trailer
from signupform import CommentForm
from database import User, Liked, Comment
from flask_login import LoginManager, login_user, login_required, current_user, logout_user
from datetime import timedelta
from extensions import db, login_manager

from auth import auth
app = Flask(__name__, static_url_path='/static')
app.config["SECRET_KEY"] = "12334"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.register_blueprint(auth)
db.init_app(app)

login_manager.init_app(app)
app.config["REMEMBER_COOKIE_DURATION"] = timedelta(days=3)
app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(minutes=30)

@app.route("/")
def index():
    upcoming = get_upcoming()
    popular = get_popular()
    
    
    return render_template('home.html', 
                           upcoming=upcoming[0:6], 
                           popular=popular[1:13], 
                           bannerMovie=popular[0])

users = []

@app.route("/popular")
def popularpage():
    page=request.args.get('page', 1)
    movies = get_popular(page)
    
    return render_template('popular.html', movies=movies)

@app.route("/upcoming")
def upcomingpage():
    page=request.args.get('page', 1)
    movies = get_upcoming(page)
    
    return render_template('upcoming.html', movies=movies)


@app.route("/profile")
@login_required
def profilepage():
    liked_movies = current_user.liked_movies

    return render_template('profile.html', liked_movies=liked_movies)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/login')

@app.route("/movie/<int:id>", methods=["GET", "POST"])
def show_movie_details(id):
    movie=get_movie_details(id)
    similar_movies=get_similar_movies(id)
    videos=get_movie_trailer(id)
    
    form = CommentForm()
    if form.validate_on_submit():
        comment = form.comment.data
        new_comment = Comment(comment=comment, movie_id=id, user_id=current_user.id)
        db.session.add(new_comment)
        db.session.commit()
        print(new_comment)

    
    liked = False
    if current_user.is_authenticated:
        sent_movie = Liked.query.filter_by(id=id, user_id = current_user.id).first()
        if sent_movie:
            liked = True
    video_key=None
    
    comments = Comment.query.filter_by(movie_id=id).all()
    print(comments)
    if len(videos) >= 1:
        video_key = videos[0].get('key')
    return render_template('details.html', liked=liked, movie=movie, similar_movies=similar_movies[0:6], videos_key=video_key, form=form, comments=comments)

@app.route("/like/<int:id>", methods=["GET", "POST"])
@login_required
def like(id):
    from flask import jsonify
    movie = get_movie_details(id)
    sent_movie = Liked.query.filter_by(title=movie.get('title'), user_id = current_user.id).first()
    if sent_movie:
        db.session.delete(sent_movie)
        db.session.commit()
    if not sent_movie:
        liked_movie = Liked(
            id = id,
            title = movie.get('title'),
            date = movie.get('release_date'),
            rate = movie.get('vote_average'),
            poster_path = f"https://image.tmdb.org/t/p/w200{ movie.get('poster_path') }",
            user_id = current_user.id
        )
        db.session.add(liked_movie)
        db.session.commit()
        print('liked movie id: ', id, "user liked:", current_user)
    return jsonify({'status': 'success'})

with app.app_context():
    # db.drop_all()
    db.create_all()
app.run(debug=True)

#User.query.all()
#User.get(1)