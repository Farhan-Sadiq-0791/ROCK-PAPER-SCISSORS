import random

user_score = int(0)
pc_score = int(0)
score_limit = 5


while user_score != score_limit or pc_score != score_limit:

    user_guess: str = input(str("pls enter your guess, rock/paper/scissors: ")).lower()

    my_list = "rock", "paper", "scissors"
    pc_guess = random.choice(my_list)
    

    if pc_guess == user_guess:
        print ( "Both have choosen " + pc_guess + ". So it's a Tie!!" )

    if pc_guess == "rock" and user_guess =="scissors" :
        print ( "The computer have choosen ROCK. So it got a point" )

        pc_score = pc_score + 1
        print ( "the pc score is:", pc_score )

    if pc_guess == "scissors" and user_guess == "rock" :
        print ( "The computer have choosen SCISSORS. So you got a point" )

        user_score = user_score + 1
        print ( "the user score is:", user_score )

    if pc_guess == "paper" and user_guess == "rock" :
        print ( "The computer have choosen PAPER. So it got a point")

        pc_score = int ( pc_score ) + 1
        print ( "the pc score is:", pc_score )

    if pc_guess == "rock" and user_guess == "paper" :
        print ("The computer have choosen ROCK. So you got a point"  )

        user_score = user_score + 1
        print ( "the user score is:", user_score )

    if pc_guess == "paper"  and user_guess == "scissors" :
        print ( "The computer have choosen  PAPER. So you got a point"  )

        user_score = user_score + 1
        print ( "the user score is:", user_score )

    if pc_guess == "scissors" and user_guess == "paper" :
        print ( "The computer have choosen SCISSORS. So it got a point" )

        pc_score = int ( pc_score ) + 1
        print ( "the pc score is:", pc_score )

    if user_score == score_limit:
            print("Congratulation! u won."
		  " This game is made by Farhan Sadiq. For advice feel free to contact at farhansadiq077@gmail.com")
    elif pc_score == score_limit:
            print("OPS, the computer won, better luck next time."
		 " This game is made by Farhan Sadiq. For advice feel free to contact at farhansadiq077@gmail.com" )
            break
