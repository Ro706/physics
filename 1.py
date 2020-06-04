#studyphysics program
#NO CODE IS RUN HERE,IT IS TELLING US WHAT WE WILL DO LATER
#HERE WE WILL DEFINE OUR FUNCTIONS
#THIS PRINT THE MAIN MENU AND PROMPTS FOR A CHOICE

def menu():
   #print what options you have
   print "welcome to physics.py"
   print "your options are:"
   print ""
   print "1)power"
   print "2)electrical potential"
   print "3)pressure"
   print "4)surface tension"
   print "5)Quit physics.py"
   print  ""
   return input("choose your option:")

#THIS DIVISION TWO NUMBERS GIVEN
def div(a,b):
    print a,"/",b,"=",a/b

#NOW THE PROGRAM REALLY STARTS,AS CODE IS RUN
loop = 1
choice = 0
while loop == 1:
  choice = menu()
  if choice == 1:
      div(input("watt:"),input("time:"))
  elif choice == 2:
      div(input("work:"),input("charge:"))
  elif choice == 3:
      div(input("Froce:"),input("Area:"))
  elif choice == 4:
      div(input("Froce:"),input("length:"))
  elif choice == 5:
      loop = 0
print "thank u for using studyphysics.py!"
print "made by Ro706"

#NOW THE PROGRAM REALLY FINISHES
