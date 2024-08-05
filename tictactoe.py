Tic Tac Toe
#Tic Tac Toe
l=[[" "," "," "],[" "," "," "],[" "," "," "]]
print(l[0],"\n",l[1],"\n",l[2])
def chance(l,n):
    
    
    while True:
        if n%2==0:
            s="x "
        else:
            s="o "
        w=int(input("Block number: "))
        if w==1:
            if l[0][0]==" ":
                l[0][0]+=s
                break
            else:
                print("Choose again this is occupied")
        elif w==2:
            if l[0][1]==" ":
                l[0][1]+=s
                break
            else:
                print("Choose again this is occupied")
        elif w==3:
            if l[0][2]==" ":
                l[0][2]+=s
                break
            else:
                print("Choose again this is occupied")
        elif w==5:
            if l[1][1]==" ":
                l[1][1]+=s
                break
            else:
                print("Choose again this is occupied")
        elif w==4:
            if l[1][0]==" ":
                l[1][0]+=s
                break
            else:
                print("Choose again this is occupied")

        elif w==6:
            if l[1][2]==" ":
                l[1][2]+=s
                break
            else:
                print("Choose again this is occupied")

        elif w==7:
            if l[2][0]==" ":
                l[2][0]+=s
                break
            else:
                print("Choose again this is occupied")

        elif w==8:
            if l[2][1]==" ":
                l[2][1]+=s
                break
            else:
                print("Choose again this is occupied")

        elif w==9:
            if l[2][2]==" ":
                l[2][2]+=s
                break
            else:
                print("Choose again this is occupied")
    print("\n ",l[0],"\n",l[1],"\n",l[2])
    

        
        
win=0
turn=1     
    
while True:
    if turn>=9:
        print("Draw")
        break
    
    if turn>4:
        for i in l:
            if i[0]==i[2] and i[0]==i[1] and i[0]!=" ":
                win=1
        if l[0][0]==l[1][0] and l[1][0]==l[2][0] and l[0][0]!=" ":
            win=1
        if l[0][1]==l[1][1] and l[0][1]==l[2][1] and l[0][1]!=" ":
            win=1
        if l[0][2]==l[1][2] and l[0][2]==l[2][2] and l[0][2]!=" ":
            win=1
        if l[0][0]==l[1][1] and l[0][0]==l[2][2] and l[0][0]!=" ":
            win=1
        if l[0][2]==l[1][1] and l[0][0]==l[2][0] and l[0][0]!=" ":
            win=1
    if win==1:
        print("victory! \n")
        break
    chance(l,turn)
    turn+=1

