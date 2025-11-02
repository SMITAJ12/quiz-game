print("welcome to my computer quiz!")
playing = input("do you want to play? yes/no ")
n = playing.lower()    # changing the input into lower letters
if n != "yes":
    quit("thank you for replying")
print("okay, let's play:) ")
questions = [                                          # multiline list(list in list)
    { " question ": "color of the hair? " , "answer": "black"},
    { " question ": "national bird? ","answer":"peacock" },
    { " question ": "national animal? ","answer":"lion"},
    { " question ": "national game ? ","answer":"hockey"},
    { " question ": "prime minister of india? ","answer":"narendra modi"},
    { " question ": "capital of india? ","answer":"delhi"}       
]
score = 0
for q in questions:
    ans = input(q[" question "] + " ").strip().lower() #take the input and clean it .
    if ans == q["answer"]:
        print("correct!")
        score += 1 # adding the score 
    else:
        print("wrong answer!, thanks for the playing")
        break #breaking the if loop
print(f" your final score is : {score}/{len(questions)}","congratulations!!")