from random import randint
import copy



story = (
    "One day my {} fiend i decided to go to the {} game in {}. " +
    "We really wanted to see the {} play the {}. " +
    "So, we {} our down to the {} and bought some {}s. " +
    "We got into the galsme and it was alot of fun. " + 
    "We ate some {} {} and drank some {} {}. " +
    "We had a great time! We plan to go ahead next year!"
)
    # come up with a dictionary to lookup words by type
word_dict = {
        'adjective':['greed','abrasive','grubby','rich','harsh','tasty'],
        'city name':['Tororo','Mbale','Budaka','Iganga','Mukono','Kampala'],
        'noun':['people','map','music','dog','hamster','ball','hotdog','salad'],
        'action verb':['run','fall','crawl','scurry','cry','watch','swim','jump','bounce'],
        'sports noun':['ball','mit','puck','uniform','helmet','scoreborad','player'],
        'place':['park','desert','forest','store','restuarant','waterfall']
}

def get_word(type,local_dict):
    words = local_dict[type]
    count = len(words)-1
    index = randint(0,count)
    return local_dict[type].pop(index)

def create_story():
    local_dict = copy.deepcopy(word_dict)
    return story.format(
        get_word('adjective',local_dict),
        get_word('city name',local_dict), 
        get_word('noun',local_dict), 
        get_word('action verb',local_dict), 
        get_word('sports noun',local_dict), 
        get_word('place',local_dict),
        get_word('adjective',local_dict),
        get_word('city name',local_dict), 
        get_word('noun',local_dict), 
        get_word('action verb',local_dict), 
        get_word('sports noun',local_dict), 
        get_word('place',local_dict)   
    ) 

print("STORY 1: ")
print(create_story())
print()
print("STORY 2: ")
print(create_story())
