import random
attempts_lists=[]
def show_score():
    if len(attempts_lists) <=0:
        print("There is currently no high score, its yours for the taking!")
    else:
        print("The current high score is {} attempts".format(min (attempts_list)))    
def start_game():
    random_number=int(random.randint(1,10)) 
    print("Hey there wana play the game of geusses")
    player_name=input("Enter your name")
    wana_play=input("Hi, {}, would you like to play the guessing game? (Enter Yes/No)".format(player_name)) 
    attempts=0
    show_score()
    while wana_play.lower()=="yes":
        try:
            guess=input("pick a number beetween 1 and 10")
            if int(guess)<1 or int(guess)>10:
                raise ValueError("Please guess a number with  the given range")
            if int(guess)==random_number:
                print("Congrats you got it right")
                attempts+=1
                attempts_lists.append(attempts)
                print("It took you {} attempts".format(attempts))
                play_again=input('Would you like to play again? (enter Yes/No)')
                attempts=0
                show_score()
                random_number=int(random.randint(1,10))
                if play_again.lower()=='no':
                    print("Thats cool have a nice day")
                    break
                elif int(guess)<random_number:
                    print('Its lower')
                    attempts+=1
                elif int(guess)>random_number:
                    print("Its higher")
                    attempts+=1
            except ValueError as err:
                print("Oh this is not a valid value try again")