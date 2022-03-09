import nltk
from nltk.corpus import wordnet as wn
import tempfile


root_folder = tempfile.gettempdir()
nltk.download('wordnet', download_dir=root_folder)
nltk.data.path.append(root_folder)

# add code 
# add code 2
# code for branch test
def compute(test):

    return {"result": [i.name() for i in wn.synsets("same")]}
