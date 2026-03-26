import random
a=input("enter player1 name:")
b=input("enter player2 name:")
d1=random.randint(1,25)
d2=random.randint(1,25)
s1=25
s2=25
while True:
   g=int(input("enter ur guess num:"))
   s1=s1-1
   if d1==g:
       print("ur num is correct")
       break
   elif d1<g:
        print("ur guess is more")
   else:
       print("ur guess is less")
while True:
   g=int(input("enter ur guess num:"))
   s2=s2-1
   if d2==g:
       print("ur num is correct")
       break
   elif d2<g:
        print("ur guess is more")
   else:
       print("ur guess is less")
if s1>s2:
    print("player 1 is winner.format(name1)")
elif s2>s1:
     print("player 2 is winner.format(name2)")
else:
    print("draw")
