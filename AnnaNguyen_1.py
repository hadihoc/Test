# This program prompts the user for the desired number of tickets and then display the number of remaining tickets
# after their purchase. It then repeats until all tickets have been sold. Then display the total number of buyers.

# This get_tickets function prompts for user input
def get_tickets(max_tickets, num_of_buyers):
    print()
    print(f"Pre-Sell Cinema Tickets")
    print()

    # Prompts for user input until there is no more ticket left
    while max_tickets > 0:
        try:
            num_of_tickets = int(input("Enter the number of tickets you would like to buy:"))

            # If user's input is between 1 and 4, inclusive and input is less than or equal to the remaining tickets
            if 0 < num_of_tickets < 5 and num_of_tickets <= max_tickets:
                num_of_buyers += 1  # Increase the num_of_buyers accumulator by 1
                max_tickets = max_tickets - num_of_tickets  # Subtract the user's input from the tickets counter
                print()
                print(f"We have {max_tickets} tickets left.")  # Print the remaining tickets
            elif num_of_tickets > 4:  # Notify user if they enter more than 4 tickets
                print("Please enter the number of tickets between 1 and 4, inclusive.")
            elif num_of_tickets > max_tickets:  # Notify user if they enter more than the number of remaining tickets
                print(f"We only have {max_tickets} ticket left.")
        except ValueError:  # Notify user if their input is other than integer data type
            print("Invalid input! Please enter a number of tickets between 1 and 4, inclusive.")
    # Return the number of buyers
    return num_of_buyers


# This DisplayTotalNumberOfBuyers function displays the total number of buyers
def display_number_of_buyers(num_of_buyers):
    print(f"The total number of buyers are: {num_of_buyers}.")


def main():
    max_tickets = 20
    num_of_buyers = 0
    num_of_buyers = get_tickets(max_tickets, num_of_buyers)
    display_number_of_buyers(num_of_buyers)


if __name__ == "__main__":
    main()
