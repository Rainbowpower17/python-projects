score=0
import time
print("🎯Welcome to the ultimate Python Game🎯")
player_name=input("Enter Your name")
print("/nHi", player_name+"! Lets test your knowledge.")
print("You will get 10 points for each correct answer./n")
time.sleep(1)

quetions = [
    {
        "question":"1. What is the color of the sky?",
        "options" : ["A. red", "B.green", "C.blue", "D.purple"],
        "answer" : "C"
    },
    
    {
        "question":"2. What is a pillow made out of?",
        "options" : ["A.rocks", "B.wood", "C.metal", "D.cotton or feather"],
        "answer" : "D"
    },

    {
       "question":"3.Where do eggs come from?",
        "options" : ["A. dog", "B.horse", "C.cat", "D.chicken"],
        "answer"  : "D"
    },

    {
        "question":"4. What is 12*2?",
        "options" : ["A. 36", "B.23", "C.24", "D.93"],
        "answer"  : "C"
    },

    {
        "question":"5. What is 19*3?",
        "options" : ["A. 57", "B.32", "C.81", "D.90"],
        "answer"  : "A" 
    }
]
