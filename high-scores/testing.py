def personal_top_three(scores):
    sort_scores = sorted(scores, reverse=True)
    top_scores = []
    i = 0
    while i < len(sort_scores):
        top_scores.append(sort_scores(i)
    return top_scores[0:2]
        
mytop3[] = personal_top_three(10,20,30,40)
print str(mytop3)[1:-1]
