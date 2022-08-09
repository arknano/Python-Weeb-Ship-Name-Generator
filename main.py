import random
from flask import Flask, render_template, request, redirect
from threading import Thread

app = Flask(__name__)

adjDesc = "adjectivesDescriptive.txt"
adjCol = "adjectivesColours.txt"
nounAbs = "nounsAbstract.txt"
noun = "nouns.txt"
name = "nounsJapaneseGirls.txt"
prep = "prepositions.txt"


def gw(filename):
    with open(filename) as fr:
        lines = fr.readlines()
        return random.choice(lines).rstrip() if lines else None


nameTypes = [
    # Name
    lambda: "{}".format(gw(name)),

    # Name's Abstract
    lambda: "{}'s {}".format(gw(name), gw(nounAbs)),

    # Name's Descriptive Noun
    lambda: "{}'s {} {}".format(gw(name), gw(adjDesc), gw(noun)),

    # Descriptive Name
    lambda: "{} {}".format(gw(adjDesc), gw(name)),

    # Colour Name
    lambda: "{} {}".format(gw(adjCol), gw(name)),

    # Name Preposition Noun
    lambda: "{} {} {}".format(gw(name), gw(prep), gw(noun)),

    # Abstract Preposition Name
    lambda: "{} {} {}".format(gw(nounAbs), gw(prep), gw(name)),
]

#for x in range(0, 20):
#    print(nameTypes[random.randrange(0, len(nameTypes))]())

#Set up website with index.html
app = Flask('app')


@app.route('/')
def hello_world():
    return render_template('index.html')

prefix: str = ""
#When the button is clicked on html, execute the function
@app.route('/submit', methods=['GET','POST'])
def submit():
    displayWord: str = ""
    for x in range(0, 10):
        displayWord += "\n{} {}".format(prefix, nameTypes[random.randrange(0, len(nameTypes))]())
    

    return render_template('index.html', display_word=displayWord, prefix=prefix)


#When the button is clicked on html, execute the function
@app.route('/prefix', methods=['POST'])
def prefix():
    global prefix
    prefix = request.form.get("prefix")
    return render_template('index.html', prefix=prefix)

def keep_alive():
    server = Thread(target=run)
    server.start()

def setPrefix():
    global prefix
    prefix = ""

def run():
    app.run(host='0.0.0.0', port=8080)

keep_alive()
setPrefix()