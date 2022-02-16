player_1=0
player_2=0
X=True
y=0
switch="player1"
x=[1,2,3,2,1]
i=0
while X:
    if i<len(x):
        if x[i]%2==0:
            if switch=="player1":
                y=x[i]
                player_1=player_1+y
            
                y=0
            else:
                y=x[i]
                player_2=player_2+y
                y=0
            
                
        elif (x[i]%2)!=0:
            if switch=="player1":
                y=x[i]
                player_1=player_1+y
                switch="player2"
                
                y=0
            else:
                y=x[i]
                player_2=player_2+y
                switch="player1"
                
                y=0
        i+=1
    else:
        X=False
     
print("Player 1: "+str(player_1)+" , "+"Player 2: "+str(player_2))            
        
    
