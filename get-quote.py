import random
last = 13
rnd = random.randint(0,last)

def awesome():
  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()
  
  last = len(quotes) - 1
  print(quotes[0:rnd])

if __name__== "__main__":
  main()
