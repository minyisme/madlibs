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

    player = request.args.get("firstname")
    color_word = request.args.get("color")
    noun_word = request.args.get("noun")
    adjective_word = request.args.get("adjective")
    place_word = request.args.get("place")
    famous_people_str = ""
    famous_people = []
    if request.args.get("shakira"):
        shakira = request.args.get("shakira")
        famous_people.append(shakira)
    if request.args.get("madonna"):
        madonna = request.args.get("madonna")
        famous_people.append(madonna)
    if request.args.get("beyonce"):
        beyonce = request.args.get("beyonce")
        famous_people.append(beyonce)
    else:
        famous_people_str = "No one"

    if famous_people != "No one":
        for person in famous_people:
            famous_people_str = famous_people_str + ", " + person
            famous_people_str = famous_people_str.lstrip(", ")

#request.args.getlist() on a multidict

    return render_template("madlib.html",
                            person=player,
                            color=color_word,
                            noun=noun_word,
                            adjective=adjective_word,
                            place=place_word,
                            people=famous_people_str)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)

