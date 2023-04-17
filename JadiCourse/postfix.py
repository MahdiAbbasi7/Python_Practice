PRIORITY = {'+':1, '-':1, '*':2, '/':2, '^':3} # dictionary having priorities 
def isoprand(x):
   if x == '+' or x == '*' or x == '-' or x == '/':
      return False 
   else:
       return True

def infix_to_postfix(expression): #input expression

    stack =[] # initially stack empty
    output ="" # initially output empty
    for ch in expression:
        if isoprand(ch): 

            output += ch
        else:
            while stack and PRIORITY[ch]<=PRIORITY[stack[-1]]:

                output+=" " +stack.pop()
            output+=" "
            stack.append(ch)

    while stack:

        output+=" "+stack.pop()
    return output
def postfix (experssion2):
       Stack =[]
       for o in experssion2:
          if  isoprand(o):
              Stack.append(o)
          else:
               Num1= Stack.pop()
               Num2= Stack.pop()
               Stack.append("(" +Num2 +o+Num1 + ")")
       return Stack[0]

Ex=input()
print(infix_to_postfix(Ex))
print(postfix(infix_to_postfix(Ex).split(" ")))






