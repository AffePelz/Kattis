friend_score = int(input())
my_answers = input()
friend_answers = input()
exam_length = len(my_answers)
matching = sum(a==b for a,b in zip(my_answers, friend_answers))

if matching >= friend_score:
    print(friend_score + (exam_length - matching))
else:
    print(matching + (exam_length - friend_score))
