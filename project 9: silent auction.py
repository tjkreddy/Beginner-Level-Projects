logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
total_list = {}
key = True

while key:
  name = input("what is your name? :\n")
  bid = input("what is your bid? :\n")
  total_list[name] = bid
  still_bids = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if still_bids == "yes":
    key = True
  elif still_bids == "no":
    key = False
  else:
    print("You have entered invalid input")
    break

max = 0
for dict in total_list:
  bid = int(total_list[dict])
  if bid > max:
    max = bid
    max_bidder = dict
  
print(f"the winner of this auction is {max_bidder}")


"link for the replit"

#https://replit.com/@pythonlearnin15/blind-auction-start#main.py