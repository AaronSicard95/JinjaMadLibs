from flask import Flask, request, render_template

from story import *

app = Flask(__name__)
answers = []
selectedStory = story
@app.route('/make-story')
def showForm():
    global story
    name = story.name
    if request.args:
        selected = request.args["stories"]
        for storySelect in stories:
            if storySelect.name == selected:
                story = Story(storySelect.name, storySelect.words, storySelect.story)
                name = storySelect.name
    return render_template("formTemplate.html", storyNames = stories, words=story.prompts, selectedName = name)

@app.route('/story')
def getForm():
    global story
    answers = story.generate(request.args)
    return render_template("storyTemplate.html", storyText = answers)