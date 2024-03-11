#This Program was created to create an accurate simulation of a coin flipping experiment.
#When the program detects 6 of the same face value in a row in a trial that trial is tallied and weighed against the whole sample size.
#By seth ayun
def coin_flip(number):                  #define coin_flip properties
        newlist=[]                      #empty list
        for item in range(number):      #repeat based on chosen list size
                import random              #random 50/50
                flip=random.randint(1,2)
                if  flip == 1:
                        newlist.append('H') #heads flip
                else:                       #both add on to the list 1 ata time based on random number
                        newlist.append('T') #tails flip
        return newlist
def six_row(experiment):                #survey the trial
        heads=0
        tails=0               #empty variables for sorting
        result=0
        for value in experiment:                #repeat based on number of trials
                if tails == 6 or heads == 6:    #return if tails or heads reach the value 6 
                        result=True             #return true to add to the tally
                        return result
                elif value == 'H':      #check for heads
                        heads=heads+1   #add 1 for every repeating value   
                        tails=0         #reset tails value due to break in streak
                elif value == 'T':      #check for tails
                        tails=tails+1
                        heads=0
                elif tails <= 6 and heads <= 6: #if neither heads nor tails reach 6 return 0
                        result=False            #return false to leave tally unaffected
                        return result
def getpositiveint(user_input):         #get positive whole number
        while True:                     #repeat until user gets it right
                try:
                        if int(user_input) < 1:  #check for negative
                                user_input=int(input('Negative integers are not allowed please try again. \n'))
                        elif int(user_input) >= 1:                      #if value is okay return it
                                return int(user_input)
                except ValueError:                                      #check for error
                        user_input=input('ERROR please try again. \n')
print('This Program will simulates an experiment in which a coin will be \nflipped however many time youd like in however many trials youd like')
print('The program will then automatically calculate the average \nnumber of trials containing the same value 6 times in a row ')
print('You may decide on the following properties of the experiment')
flip=[]                 #empty list to store coin flip results
flipcount=getpositiveint(input('how many times would you like to flip a coin in a single trial? \n'))           #get positive user input for number of flips in a trial
while flipcount < 6:
        if flipcount > 0 and flipcount < 6:                                                                             #check for less than 6 flips ina single trial
                flipcount=getpositiveint(input('You may not flip a coin less than 6 times in a single trial please try again. \n'))
experiments=getpositiveint(input('how many trials would your like run for this experiment? \n'))                #get positive user input for number of trials to repeat
print('calculating...')
count=0
for x in range(experiments):                    #repeat for however many trials there are
        flip=coin_flip(flipcount)               #call coin_flip and store results in flip[]
        ifsix=six_row(flip)                     #call six_row to check flip[] for 6 in a row
        if ifsix == True:                       #add 1 to the total for every six_row check that returns true
                count=count+1     
print('this experiment resulted in ' + str(count) + ' total trials containing 6 heads or tails in a row')
print('resulting in a ' + str(((count / experiments)*100)) + '% average')
