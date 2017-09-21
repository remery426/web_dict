import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in '%s': %s" % (cwd, files))
data = open('apps/main/data.json')
def translate(postData):
    response = {}

    data = json.load(open('apps/main/data.json'))
    word =postData['word']
    response ['word'] = word
    word = word.lower()
    if word in data:
        response["status"] = True
        response['definition'] = (data[word])

    else:
        response["status"]=False
        list_1 = get_close_matches(word,data.keys())
        response["suggestions"]= list_1

    return response
