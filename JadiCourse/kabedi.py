
num_player =int( input("Enter number of player : "))
num_play=input("Enter numbers of games : ")
list_numplay = num_play.split(" ")
list_numplay.sort()
list_baghi=[]
list_ezafi=[]

#print(list_numplay)
if num_player == len(list_numplay):



   # print(len(list_numplay))
    #print(list_numplay)
  for i in list_numplay:
    if "0"in i :
      list_baghi.append(i)   
    elif "1"in i: 
      list_baghi.append(i) 
    elif "2"in i: 
      list_baghi.append(i)
    else:
      list_ezafi.append(i)
    
  print(len(list_baghi)//3)
  
  
else :
    print("Something was wrong")


