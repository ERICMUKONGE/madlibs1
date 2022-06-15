import json
import os

class Madlibs:
    path = "./templates"
    def __init__(self,word_descriptions,template):
        self.template = template
        self.word_description = word_descriptions
        self.user_input = []
        self.story = None
     
    @classmethod
    def from_json(cls,name,path="./templates"):
        if not path:
            path = cls.path
        fpath = os.path.join(path, name)
        with open(fpath, "r") as f:
            data = json.load(f)
        mad_lib = cls(**data)
        return mad_lib


def get_words_from_user(self):
        print("Please provide the following words:")
        for desc in self.word_descriptions:
            ui = input(desc + " ")
            self.user_input.append(ui)  
        return self.user_input
 
def build_story(template,words):
        story = template.format(*words)
        return story

def show_story(self):
    print(story)
    

def select_template():
    print("Select a Madlib from the following list:")
    templates = os.listdir(Madlibs.path)
    template = input(str(templates) + " ")
    return template   


temp_name = select_template
#temp_name = "research.json"
mad_lib = Madlibs.from_json(temp_name)
words = mad_lib.get_words_from_user()
story = mad_lib.build_story()
mad_lib.show_story()                                          