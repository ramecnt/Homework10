from flask import Flask
import utils

app = Flask(__name__)

@app.route('/')
def page_main():

    candidates = utils.get_all()
    result = utils.format_candidates(candidates)
    return result

@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = utils.get_by_pk(uid)
    result = f'<img src="{candidate["picture"]}">'
    result += utils.format_candidates([candidate])
    return result

@app.route("/skills/<uid>")
def page_skill(uid):
    candidate = utils.get_by_skill(uid.lower())
    return utils.format_candidates(candidate)
app.run()

