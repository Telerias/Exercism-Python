'''
Use list to hold scores
list.pop() - removes and returns last item in list - note that it removes! templist = list does not copy, only pointer!







'''

def latest(scores):
    tempscore = scores  # doesn't copy, still removes last added
    last_added = tempscore.pop() # get the last added score
    return last_added



def personal_best(scores):
    pass


def personal_top_three(scores):
    pass
