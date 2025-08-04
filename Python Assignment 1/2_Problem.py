def count_characters(text: str) -> dict:
    """
    Analyzes a string and returns counts of different character types.
    
    Args:
        text (str): Input string to analyze
        
    Returns:
        dict: Dictionary containing counts of:
              - alphabetic characters
              - digits
              - lowercase letters
              - uppercase letters
              - other characters
              
    Raises:
        ValueError: If input is not a string
    """
    if not isinstance(text, str):
        raise ValueError("Input must be a string")
    
    counts = {
        'letters': 0,
        'digits': 0,
        'lowercase': 0,
        'uppercase': 0,
        'other': 0
    }
    
    for char in text:
        if char.isalpha():
            counts['letters'] += 1
            if char.islower():
                counts['lowercase'] += 1
            else:
                counts['uppercase'] += 1
        elif char.isdigit():
            counts['digits'] += 1
        else:
            counts['other'] += 1
            
    return counts

def format_report(counts: dict) -> str:
    """Formats the character counts into a readable report"""
    return (
        f"Alphabetic: {counts['letters']} "
        f"({counts['lowercase']} lowercase, {counts['uppercase']} uppercase)\n"
        f"Digits: {counts['digits']}\n"
        f"Other characters: {counts['other']}"
    )

def interactive_mode():
    """Runs the program in interactive command-line mode"""
    print("String Character Counter")
    print("Enter a string to analyze (or 'quit' to exit):")
    
    while True:
        try:
            user_input = input("> ")
            if user_input.lower() in ('quit', 'exit'):
                break
                
            counts = count_characters(user_input)
            print("\n" + format_report(counts) + "\n")
            
        except ValueError as e:
            print(f"Error: {e}\n")
        except KeyboardInterrupt:
            print("\nProgram terminated")
            break

if __name__ == "__main__":
    # Example usage
    sample = "Hello123!"
    print(f"Sample analysis for '{sample}':")
    print(format_report(count_characters(sample)))
    
    # Run interactive mode
    print("\nInteractive mode:")
    interactive_mode()