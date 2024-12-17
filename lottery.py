import random

def get_valid_numbers(total_numbers=6, number_range=(0, 100)):
    """
    Collect valid lottery numbers from user input with comprehensive validation.
    
    Args:
        total_numbers (int): Total numbers to collect
        number_range (tuple): Valid range for numbers (min, max)
    
    Returns:
        list: Validated lottery numbers
    """
    lucky_numbers = []
    min_num, max_num = number_range
    
    while len(lucky_numbers) < total_numbers:
        try:
            # Prompt for input with clear instructions
            user_input = input(f"Enter lucky number {len(lucky_numbers) + 1} "
                               f"(between {min_num} and {max_num}): ").strip()
            
            # Convert input to integer
            number = int(user_input)
            
            # Validate number range
            if number < min_num or number > max_num:
                print(f"Invalid number! Please enter a number between {min_num} and {max_num}.")
                continue
            
            # Check for duplicates
            if number in lucky_numbers:
                print("You've already entered this number. Please choose a different one.")
                continue
            
            # Add valid number
            lucky_numbers.append(number)
        
        except ValueError:
            print("Invalid input! Please enter a valid integer.")
    
    return lucky_numbers

def calculate_winnings(jackpot, winning_numbers, player_numbers):
    """
    Calculate winnings based on number of matching numbers.
    
    Args:
        jackpot (float): Total jackpot amount
        winning_numbers (list): Randomly generated winning numbers
        player_numbers (list): Player's selected numbers
    
    Returns:
        tuple: (number of matches, winnings amount)
    """
    # Match numbers exactly
    matches = sum(w == p for w, p in zip(winning_numbers, player_numbers))
    
    # Winnings calculation with more detailed tiers
    winnings_tiers = {
        0: 0,        # No matches
        1: 0.1,      # 1 match: 10% of jackpot
        2: 0.25,     # 2 matches: 25% of jackpot
        3: 0.4,      # 3 matches: 40% of jackpot
        4: 0.6,      # 4 matches: 60% of jackpot
        5: 0.8,      # 5 matches: 80% of jackpot
        6: 1.0       # All matches: Full jackpot
    }
    
    # Calculate winnings
    winnings = winnings_tiers.get(matches, 0) * jackpot
    
    return matches, winnings

def main():
    """
    Main lottery game simulation with enhanced features.
    """
    # Set up game parameters
    jackpot = 1_000_000  # 1 million
    total_numbers = 6
    number_range = (0, 100)
    
    # Generate winning numbers
    winning_numbers = random.sample(range(number_range[0], number_range[1] + 1), total_numbers)
    
    # Get player's numbers with validation
    try:
        print("🎲 Welcome to the Lottery Number Matcher! 🍀")
        print(f"Enter {total_numbers} unique numbers between {number_range[0]} and {number_range[1]}")
        player_numbers = get_valid_numbers(total_numbers, number_range)
        
        # Calculate results
        matches, winnings = calculate_winnings(jackpot, winning_numbers, player_numbers)
        
        # Display results
        print("\n--- Lottery Results ---")
        print(f"Winning Numbers:\t{winning_numbers}")
        print(f"Your Numbers:\t{player_numbers}")
        print(f"Matching Numbers:\t{matches}")
        print(f"Your Winnings:\tKsh {winnings:,.2f}")
        
        # Add congratulatory messages
        if matches == total_numbers:
            print("🎉 JACKPOT WINNER! Congratulations!! 🎊")
        elif matches > 0:
            print("Congratulations on your win!")
        else:
            print("Better luck next time!")
    
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the game
if __name__ == "__main__":
    main()
