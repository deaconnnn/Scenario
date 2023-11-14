welcome_message = print("\nWelcome to Copington Adventure Theme Park!\n""Get ready for an unforgettable adventure! \n""We're excited to help you plan your visit.")

ticket_prices = print("\nEntrance Ticket Prices:")
print("- Adult (ages 16+): £25")
print("- Child (ages 3-15): £15")
print("- Senior Citizen (65+): £20")
print("- Wristband for Rides: £10")

def lead_booker():
    return input("What is the lead bookers name? ")



while True:
    try:
        adult_tickets = int(input("\nHow many adult tickets do you need? "))
        if adult_tickets >= 0:
            print(f"You ordered {adult_tickets} adult tickets.")
            break
        else:
            print("Please enter a valid number (0 or greater).")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        child_tickets = int(input("\nHow many child tickets do you need? "))
        if child_tickets >= 0:
            print(f"You ordered {child_tickets} child tickets.")
            break
        else:
            print("Please enter a valid number (0 or greater).")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        senior_tickets = int(input("\nHow many senior citizen tickets do you need? "))
        if senior_tickets >= 0:
            print(f"You ordered {senior_tickets} senior tickets.")
            break
        else:
            print("Please enter a valid number (0 or greater).")
    except ValueError:
        print("Please enter a valid number.")

while True:
    try:
        wristband_tickets = int(input("\nHow many wristbands do you need? "))
        if wristband_tickets >= 0:
            print(f"You ordered {wristband_tickets} writsbands.")
            break
        else:
            print("Please enter a valid number (0 or greater).")
    except ValueError:
        print("Please enter a valid number.")