import random

print("Welcome to Basketball Game Simulator")
player_name = input(("What's your full name? "))
player_age = int(input("What's your age? "))

'''
while True:
    player_age = int(input("What's your age? "))
    while player_age.isnumeric() == False:
        print("Not an int")
        break
'''


#def getAge():
    #player_age = input("What's your age? ")
    #while player_age.isnumeric() == False:
        #print("Not an int. ")
        #getAge()
        #break
     

#while age.isnumeric() == False:
     #print("Not an int.")
     #getAge()
     #break 




list_of_teams = ['Hawks', ' Celtics', ' Nets', 'Hornets', 'Bulls', 'Cavaliers', 
        'Mavericks', 'Nuggets', 'Pistons', 'Warriors', 'Rockets', 'Pacers', 'Clippers', 'Lakers',
        'Grizzlies', 'Heat', 'Bucks', 'Timberwolves', 'Pelicans', 'Knicks', 'Thunder', 'Magic',
        '76ers', 'Suns', 'Blazers', 'Kings', 'Spurs', 'Raptors', 'Jazz', 'Wizards']

points = 0
assists = 0
turnovers = 0
fg_attempted = 0
fg_made = 0


points_box_score = []
assists_box_score = []
rebounds_box_score = []
steals_box_score = []
blocks_box_score = []



if player_age <= 21 and player_age >= 18:
    team_drafted = random.choice(list_of_teams)
    print(player_name, "was drafted by the", team_drafted)
    n = input("Enter number of games played: ")
    for i in range(1, int(n)+1):
        print("Enter stats for game", i)
        stats_points = int(input("Please enter your points: "))
        stats_assists = int(input("Please enter your assists: "))
        stats_rebounds = int(input("Please enter your rebounds: "))
        stats_steals = int(input("Please enter your steals: "))
        stats_blocks = int(input("Please enter your blocks: "))
        points_box_score.append(stats_points)
        assists_box_score.append(stats_assists)
        rebounds_box_score.append(stats_rebounds)
        steals_box_score.append(stats_steals)
        blocks_box_score.append(stats_blocks)
  

    averagePoints = sum(points_box_score)/int(n)
    averageAssists = sum(assists_box_score)/int(n)
    averageRebounds = sum(rebounds_box_score)/int(n)
    averageSteals = sum(steals_box_score)/int(n)
    averageBlocks = sum(blocks_box_score)/int(n)

    print("Season Averages: ")
    print("Points:", round(averagePoints, 2))
    print("Assists:", round(averageAssists, 2))
    print("Rebounds:", round(averageRebounds, 2))
    print("Steals:", round(averageSteals, 2))
    print("Blocks:", round(averageBlocks, 2))

    if float(averagePoints + averageAssists + averageRebounds) >= 30:
        print("Congratatulations! You've won Rookie of the Year")
    elif float(averagePoints + averageAssists + averageRebounds) >=17:
        print("Great Job! You've made an All-Rookie Team")
    else:
        print("You need to continue to develop")

elif player_age >= 22 and player_age <= 43:
    player_team = input("What team are you on? ")
    team_playing = random.choice(list_of_teams)
    print("You are the star of the", player_team, "playing against the", team_playing, "in the NBA Finals")
    first_possession = input("On the first possession, you get the ball in the corner (shoot/pass): ")
    while True:
        if first_possession.lower() == "shoot":
            print("You splashed the three!")
            points += 3
            fg_attempted += 1
            fg_made += 1
            break
        elif first_possession.lower() == "pass":
            print("You passed it to your teammate who made the mid-range jumper!")
            assists += 1
            break
        else:
            print("Not an option, try again")
            break

    second_possession = input("You get the ball in the corner again; Do you drive baseline or pass it to the cutting man (drive/pass): ")
    while True:
        if second_possession.lower() == "drive":
            print("You got bodied by the defender and went out of bounds")
            turnovers += 1
            break
        elif second_possession.lower() == "pass":
            print("You hit your cutting teammate who made the layup")
            assists += 1
            break
        else:
            print("Not an option, try again")

    print("You made 2/4 threes and had an assist to end the quarter")
    points += 6
    fg_made += 2
    fg_attempted += 4
    assists += 1
    print("End of first quarter  ", player_team, ": 27", team_playing, ": 30")
    print("End of 1st quarter stats: ", points, "points", assists, "assists", turnovers, "turnovers")

    third_possession = input("You get the ball on the wing with a defender closing out on you;\n"
                              "Do you pump fake and drive in, pass it the open man in the corner, or shoot it (drive/pass/shoot): ")
    while True:
        if third_possession.lower() == "drive":
            print("You drive in and make the up and under layup!")
            points += 2
            fg_made += 1
            fg_attempted += 1
            break
        elif third_possession.lower() == "pass":
            print("You hit the open man in the corner, but he misses the wide open three!")
            break
        elif third_possession.lower() == "shoot":
            print("You shoot the contested shot and miss the shot")
            fg_attempted += 1
            break
        else:
            print("Not an option, try again")
    
    fourth_possession = input("You get the ball on a fastbreak; Do you pass it to the corner or take it up yourself (pass/layup): ")

    while True:
        if fourth_possession.lower() == "pass":
            print("He makes the three this time!")
            assists += 1
            break
        elif fourth_possession.lower() == "shoot":
            print("A player chases you down and blocks the shot off the glass!")
            fg_attempted += 1
            break
        else:
            print("Not an option, try again")

    print("You slowed down in the second quarter, missing your next three shots, but you got another assist")
    fg_attempted += 3
    assists += 1
    print("End of half  ", player_team, ": 55", team_playing, ": 60")
    print("End of 1st half stats: ", points, "points", assists, "assists", turnovers, "turnovers")
    
    fifth_possession = input("You're sizing up your defender, while driving on him he opens up his hips; Do you snatch back and shoot the middy or drive while you have the step on him (snatch/drive): ")

    while True:
        if fifth_possession.lower() == "snatch":
            print("You snatch the ball back and your defender falls to the ground and hit the open middy!")
            points += 2
            fg_attempted += 1
            fg_made += 1
            break
        elif fourth_possession.lower() == "drive":
            print("A defender comes in to help and strips the ball out of your hand!")
            turnovers += 1
            break
        else:
            print("Not an option, try again")

    sixth_possession = input("You get the ball in the post against a smaller defender; You see a man open in the corner for a split second; Do you pass or shoot it (pass/shoot): ")

    while True:
        if sixth_possession.lower() == "pass":
            print("A defender out of nowhere intercepts the pass!")
            turnovers += 1
            break
        elif sixth_possession.lower() == "shoot":
            print("You make a smooth fadeaway over the smaller player")
            fg_attempted += 1
            fg_made += 1
            points += 2
            break
        else:
            print("Not an option, try again")

    print("You started to heat up towards the end of the third quarter making you next 3/4 shots!")
    points += 6
    fg_attempted += 3
    fg_made += 4
    print("End of third quarter  ", player_team, ": 80", team_playing, ": 79")
    print("End of 3rd quarter stats: ", points, "points", assists, "assists", turnovers, "turnovers")

    seventh_possession = input("You get the ball in the post again, and see a defender coming to double team you; Do you still shoot it or pass it to the help defender's man? (pass/shoot): ")

    while True:
        if sixth_possession.lower() == "pass":
            print("You pass it to the help defender's man in the corner and he makes the three!")
            assists += 1
            break
        elif sixth_possession.lower() == "shoot":
            print("The help defender gets there in time and you miss the heavily contested shot")
            fg_attempted += 1
            break
        else:
            print("Not an option, try again")

    print("There's seven seconds left on the clock, the", player_team, "is down 102-101 to the", team_playing, ". Your coach runs a play that gives you the ball to begin with and they run an off-ball screen to get an open three with your teammate")

    final_possession = input("You're isolated against the defender, and your teammate gets open from the screen; Do you pass it to the wide open teammate or shoot it over the defender? (pass/shoot): ")
    while True:
        if final_possession.lower() == "pass":
            fg_percentage = round((float(fg_made/fg_attempted)*100), 1)
            print("You hit the open man on the wing, but he misses the wide open three to win the game!")
            print("The", player_team, "lost to the", team_playing, "in heartbreaking fashion! Should", player_name, "taken the last shot?")
            print(player_name, "ended the game with", points, "points", assists, "assists", "and", turnovers, "turnovers! He shot ", fg_percentage, "% from the field")
            break
        elif final_possession.lower() == "shoot":
            print("You shoot the mid-range shot over the defender and make it for the game!!")
            fg_attempted += 1
            fg_made += 1
            points += 2
            fg_percentage = round(float(fg_made/fg_attempted),1)
            print("The", player_team, "won against", team_playing, "in one of the most exciting finishes in NBA history!" ,player_name, "won Finals MVP after hitting one of the greatest shots in NBA history!")
            print(player_name, "ended the game with", points, "points", assists, "assists", "and", turnovers, "turnovers! He shot ", fg_percentage, "% from the field in his MVP performance!")
            break
        else:
            print("Not an option, try again")  
else:
    if  player_age >= 0 and player_age < 18:
        print("You're too young to be in the NBA!")
    elif player_age >= 44 and player_age < 999:
        print("You're too old to be in the NBA!")
    elif type(player_age) == str is True:
        print("Invalid input")
    else:
        print("Invalid input")




     
                        



    

        



