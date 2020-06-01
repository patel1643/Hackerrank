def breakingRecords(scores):
    highScoreCounter = 0
    lowScoreCounter = 0
    high = scores[0]
    low = scores[0]
    for i in scores[1:]:
        if i > high:
            high = i
            highScoreCounter+=1
        if i < low:
            low = i
            lowScoreCounter+=1
            
    print(highScoreCounter, lowScoreCounter)
    
#breakingRecords([10, 5, 20, 20, 4, 5, 2, 25, 1]) --> 2 4