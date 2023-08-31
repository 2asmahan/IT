
import Time

Name = input("What Is Your Name  ^_^ ? ")

print ("Hello ^_^ " + Name, "Time to Play Hang !")

Time.sleep(1)

print ("Start guess..")
Time.sleep(0.5)

Word =("Hang ")

Gue = ''

Tur = 5


while Tur > 0:         

    Fail = 0             

    for Char in Word:      

        if Char in Gue:    
    
            print (Char,end=""),    

        else:
    
            print ("_",end=""),     
       
            Fail+= 1    


    if Fail == 0:        
        print ("You won ^_^")
        break            
    Guess = input("Guess aCharacter :") 


    Gue += Guess  
                  
    if Guess not in Word:  
        Tur -= 1        
        print ("Wrong")  
        print ("You Have", + Tur, 'More Than One Guesses' )

        if Tur == 0:           
    
            print ("You Lose *_*"  )