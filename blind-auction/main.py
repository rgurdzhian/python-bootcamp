from art import logo
print(logo)
print("Welcome to the secret auction program.")
bid_dictionary = {}
should_continue = True
while should_continue:
  name = input("What is your name? ")
  bid = int(input("What's your bid?: $"))
  bid_dictionary[name] = bid
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if other_bidders == 'no':
    should_continue = False

winner = max(bid_dictionary, key=bid_dictionary.get)

print(f"The winner is {winner} with a bid of ${bid_dictionary[winner]}.")
