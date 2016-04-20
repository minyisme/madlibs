from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']


@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    player = request.args.get("person")

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=player,
                           compliment=compliment)


@app.route('/game')
def show_game_form():
    """Redirects player based on play_response."""

    play_response = request.args.get("play_game")

    if play_response == "no":
        return render_template("goodbye.html")
    else:
        return render_template("game.html")


@app.route('/madlib')
def show_madlib():
    """Show madlib.html."""

    # binding variables to passed parameters from form input 
    player = request.args.get("firstname")
    color_word = request.args.get("color")
    noun_word = request.args.get("noun")
    adjective_word = request.args.get("adjective")
    place_word = request.args.get("place")
    # request.args.getlist used to get lists from form input
    famous_people = request.args.getlist("people")

    # below is an alternate solution that solves for extra comma but
    # doesn't use jinja2
    # # create an empty string to populate later
    # famous_people_str = ""

    # # run through list of famous people and add their names to string
    # if famous_people:
    #     for person in famous_people:
    #         famous_people_str = famous_people_str + ", " + person
    #         famous_people_str = famous_people_str.lstrip(", ")
    # else: 
    #     famous_people_str = "No one"

    # a list to hold different madlibs
    madlib_version = ["madlib.html", "madlib2.html", "madlib3.html"]
    chosen_madlib = choice(madlib_version)

    return render_template(chosen_madlib,
                            person=player,
                            color=color_word,
                            noun=noun_word,
                            adjective=adjective_word,
                            place=place_word,
                            people=famous_people)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

