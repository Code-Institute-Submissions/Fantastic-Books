import os
from datetime import date
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


mongo = PyMongo(app)


date = date.today()


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


# Register user in the db
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        # check if email already exists in db
        existing_email = mongo.db.users.find_one(
            {"email": request.form.get("email").lower()})

        if existing_email:
            flash("Email already registered")
            return redirect(url_for("register"))

        register = {
            "firstname": request.form.get("firstname").lower(),
            "lastname": request.form.get("lastname").lower(),
            "username": request.form.get("username").lower(),
            "email": request.form.get("email").lower(),
            "password": generate_password_hash(request.form.get("password")),
            "favourites": [],
            "date_created": date.strftime("%d %b %Y")
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Log existing user into site
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        my_reviews = list(mongo.db.reviews.find(
            {"created_by": session["user"]}).sort("title", 1))
        user = mongo.db.users.find_one(
            {"username": session["user"]})
        return render_template(
            "profile.html", username=username, reviews=my_reviews, user=user)

    return redirect(url_for("login"))


@app.route("/reviews")
def reviews():
    reviews = list(mongo.db.reviews.find())
    return render_template("reviews.html", reviews=reviews)


@app.route("/add_review", methods=["GET", "POST"])
def add_review():
    if request.method == "POST":
        default_url = ("https://www.bookdepository.com/")
        default_img = "static/images/no_cover.png"
        review = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "published": request.form.get("published"),
            "cover": request.form.get("cover") or default_img,
            "buy": request.form.get("buy") or default_url,
            "synopsis": request.form.get("synopsis"),
            "review": request.form.get("review"),
            "created_by": session["user"],
            "rating": request.form.get("star"),
            "date_created": date.strftime("%d %b %Y")
        }
        mongo.db.reviews.insert_one(review)
        flash("Your Review Has Been Added")
        return redirect(url_for("reviews"))

    reviews = mongo.db.reviews.find().sort("title", 1)
    return render_template("add_review.html", reviews=reviews)


@app.route("/edit_review/<review_id>", methods=["GET", "POST"])
def edit_review(review_id):
    if request.method == "POST":
        update = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "published": request.form.get("published"),
            "cover": request.form.get("cover"),
            "buy": request.form.get("buy"),
            "synopsis": request.form.get("synopsis"),
            "review": request.form.get("review"),
            "created_by": session["user"]
        }
        mongo.db.reviews.update({"_id": ObjectId(review_id)}, update)
        flash("")
        return redirect(url_for("reviews"))

    review = mongo.db.reviews.find_one({"_id": ObjectId(review_id)})
    reviews = mongo.db.reviews.find().sort("title", 1)
    return render_template("edit_review.html", review=review, reviews=reviews)


@app.route("/add_favourite/<review_id>", methods=["GET", "POST"])
def add_favourite(review_id):
    if request.method == "POST":
        user = mongo.db.users.find_one({"username": session["user"].lower()})
        favourites = mongo.db.users.find_one(user)["favourites"]
        if ObjectId(review_id) in favourites:
            flash("Review Already Saved")
            return redirect(url_for("reviews"))
        mongo.db.users.update_one(
             user, {"$push": {
                "favourites": ObjectId(review_id)}})
        flash("Review added to favourites")
        return redirect(url_for("reviews"))


@app.route("/get_favourites")
def get_favourites():
    user = mongo.db.users.find_one(
        {"username": session["user"].lower()})
    user_favourites = mongo.db.users.find(user["favourites"])
    favourite_reviews = []


@app.route("/remove_favourite/<review_id>")
def remove_favourite(review_id):
    user = mongo.db.users.find_one({"username": session["user"].lower()})
    mongo.db.users.update_one(user, {
        "$pull": ObjectId(review_id)})
    flash("Removed from favourites")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/delete_review/<review_id>")
def delete_review(review_id):
    mongo.db.reviews.remove({"_id": ObjectId(review_id)})
    return redirect(url_for("profile", username=session["user"]))


@app.route("/search", methods=["GET", "POST"])
def search():
    search = request.form.get("search")
    reviews = list(mongo.db.reviews.find({"$text": {"$search": search}}))
    return render_template("reviews.html", reviews=reviews)


@app.route("/search_mobile")
def search_mobile():
    return render_template("search_mobile.html")


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/delete_profile/<user_id>")
def delete_profile(user_id):
    mongo.db.reviews.remove({"created_by": session['user']})
    mongo.db.users.remove({"_id": ObjectId(user_id)})
    flash("Your Profile has been deleted")
    session.clear()
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', title='404'), 404


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
