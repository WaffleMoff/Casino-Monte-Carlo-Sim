#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 23 11:26:57 2022

@author: shenlu
"""
#Erik Ely
#1/23/22
#OMH

#In this project, I started by figuring out how to sort people into various demographics.
#Next I tackled how to sort each demographic into various games.
#I did this by tackling one demographic first, then changing my code so it looped for all 4 demographics

#https://www.lasvegasadvisor.com/question/stratosphere-tower-visitor-statistics/
#I used this information to find out the average number of visitors to a Las Vegas casino
#This was the best source I could find since casinos prefer to keep this information secret

#https://repository.usfca.edu/cgi/viewcontent.cgi?article=1008&context=hosp
#Men tend to be more risky, women are less risky, old people play slots more, young people play blackjack

#https://pynative.com/python-weighted-random-choices-with-probability/
#I learned how to use make a random sample here

#https://get-reinvented.com/qa/how-much-does-the-average-person-spend-in-a-casino.html
#$100 is a baseline for what people bring to a casino

#https://www.businessinsider.com/house-advantage-for-casino-games-2013-5
#house advantage

#For the sake of this simulation, we are going to make it an average day.
#Season isn't going to be considered because it will be averaged out for this sim.

#This is the function that takes players and determines which game they play at the casino
#Then it adds them up to determine how many people are playing each game
def choosegame():
    global i, stage, youngmen, oldmen, oldmen, youngwomen, oldwomen, Games, youngmengames, oldmengames, youngwomengames, oldwomengames, tempholder
    if stage == 1:
        people = youngmen
    elif stage == 2:
        people = oldmen
    elif stage == 3:
        people = youngwomen
    elif stage == 4:
        people = oldwomen
    #print(people)
    tempholder = [0,0,0,0,0]
    
    #Here are the weighted odds I used, in order to reflect the fact that men were more risky,
    #I made it so more men played slots and roulette over blackjack. Younger men also played roulette the most.
    #Women tended to play blackjack more since the most skilled players can actually get favorable odds
    #Blackjack can be one of the least risky games if played properly
    while i < people:
        if stage == 1:
           gamechoice = random.choices(Games, weights=(44, 26, 14, 6, 10), k=1)
           #print("stage 1 rn")
        elif stage == 2:
           gamechoice = random.choices(Games, weights=(50, 16, 18, 6, 10), k=1)
           #print("stage 2 rn")
        elif stage == 3:
           gamechoice = random.choices(Games, weights=(39, 16, 29, 6, 10), k=1)
           #print("stage 3 rn")
        elif stage == 4:
           gamechoice = random.choices(Games, weights=(46, 16, 22, 6, 10), k=1)
           #print("stage 4 rn")       
        
        if gamechoice[0] == "Roulette":
             tempholder[0] += 1
        elif gamechoice[0] == "Blackjack":
             tempholder[1] += 1
        elif gamechoice[0] == "Slots":
             tempholder[2] += 1
        elif gamechoice[0] == "Craps":
             tempholder[3] += 1               
        elif gamechoice[0] == "Baccarat":
             tempholder[4] += 1
        i += 1
        #print(tempholder)
    
    #print(tempholder) #TEST
    
    if stage == 1:
        youngmengames = tempholder
        #print(tempholder)
        tempholder = [0,0,0,0,0]
    if stage == 2:
        oldmengames = tempholder
        #print(tempholder)
        tempholder = [0,0,0,0,0]
    if stage == 3:
        youngwomengames = tempholder
        #print(tempholder)
        tempholder = [0,0,0,0,0]
    if stage == 4:
        oldwomengames = tempholder
        #print(tempholder)
        tempholder = [0,0,0,0,0]
    tempholder = [0,0,0,0,0]
    #print(tempholder)
    
#This function simulates people betting against the house in various games and calculates the profit at the end
def playgames():
    global i, stage, youngmen, oldmen, oldmen, youngwomen, oldwomen, Games, youngmengames, oldmengames, youngwomengames, oldwomengames, Profit, Gameodds, tempholder 
    
    if stage == 1:
        tempholder = youngmengames
        #print(tempholder)
    elif stage == 2:
        tempholder = oldmengames
        #print(tempholder)
    elif stage == 3:
        tempholder = youngwomengames
        #print(tempholder)
    elif stage == 4:
        tempholder = oldwomengames
        #print(tempholder)
        
    i = 0
    game = 0
    while i < tempholder[game]:
        #people typically bring around 100-500 dollars with them
        playercash = random.randint(100,500)
        #There is an average of 12 rounds per hour, so people usually spend around 4 hours gambling.
        #We use weighted probablity here to calculate how much time someone will spend at the casino.
        num = random.random()
        if num > 0.35:
            rounds = 48
        elif num > 0.175:
            rounds = 24
        else:
            rounds = 72
        q = 0
        #Then we play out those rounds. If the player runs out of cash, they stop.
        while q < rounds:
            num = random.random()
            if num > 0.5:
                bet = int(0.1*playercash)
            elif num > 0.15:
                bet = int(0.15*playercash)
            elif num > 0.05:
                bet = int(0.2*playercash)
            else:
                bet = int(0.3*playercash)
            num = random.random()
            if num > Gameodds[game]:
                playercash += bet
                Profit -= bet
            else:
                playercash -= bet
                Profit += bet
            
            if playercash <= 0:
                q = rounds
            q += 1
        i += 1
    game += 1

#This is the overall loop for the simulation that lets us run it 1000 times
totalprofit = 0
counter = 0
while counter <1000:

    import random
    
    Games = ['Roulette', 'Blackjack', 'Slots', 'Craps', 'Baccarat']
    Gameodds = [0.553, 0.52, 0.6, 0.514, 0.512]
    tempholder = [0,0,0,0,0]
    
    Profit = 0
    #There are an average of around 5400 visitors per day
    #Since the number of actual visitors varies somewhat per day, we'll make it somewhat random
    PotentialVisitors = [5000, 5200, 5400, 5600, 5800]
    #Weights are based on normal distribution percentages
    #It gives each number in the list a probability and then picks based on that
    #print(random.choices(PotentialVisitors, weights=(1, 15, 68, 15, 1), k=1))
    Visitors = random.choices(PotentialVisitors, weights=(1, 15, 68, 15, 1), k=1)
    #print(Visitors)
    #Visitors = int(Visitors)
    
    #nearly 65 percent are men, 35 percent are women
    men = int(Visitors[0] * 0.649)
    women = Visitors[0] - men
    #print(men)
    #print(women)
    
    #32 percent of visitors are young (21 - 35 years), the rest are old
    youngmen = int(men*0.32)
    oldmen = men - youngmen
    youngwomen = int(women*0.32)
    oldwomen = women - youngwomen
    
    
    youngmengames = [0,0,0,0,0]
    oldmengames = [0,0,0,0,0]
    youngwomengames = [0,0,0,0,0]
    oldwomengames = [0,0,0,0,0]
    
    i = 0
    stage = 1
    
    
    
    
    #This loop goes through each demographic one by one doing all the calculations necessary
    while stage < 5:    
        i = 0
        choosegame()
        #print(youngmengames)
        #print(oldmengames)
        #print(youngwomengames)
        #print(oldwomengames)
        #print(stage)
        i = 0
        #print(youngmengames)
        playgames()
        stage += 1
    
    
    #print(youngmengames)
    #print(oldmengames)
    #print(youngwomengames)
    #print(oldwomengames)
    #print(Profit)
    totalprofit += Profit
    counter += 1
meanprofit = totalprofit/1000
print("The mean profit after 1000 iterations is ", meanprofit)

#I sought out feedback from a friend who had taken a course on python before
#he helped me think about the best way to plan out the coding
#he also helped me brainstorm what factors I needed to take account of in this simulation

#I also talked to a couple classmates on how to improve my project





































