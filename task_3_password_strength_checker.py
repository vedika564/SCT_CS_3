import re

def check_password_strength(password):
    score = 0
    feedback = []
    
    # Length check
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("Use at least 8 characters")
    
    # Character checks
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        feedback.append("Add uppercase letters")
        
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Add lowercase letters")
        
    if re.search(r'\d', password):
        score += 1
    else:
        feedback.append("Add numbers")
        
    if re.search(r'[!@#$%^&*]', password):
        score += 1
    else:
        feedback.append("Add special characters")
    
    # Determine strength
    if score >= 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {
        'strength': strength,
        'score': f"{score}/6",
        'suggestions': feedback
    }

def main():
    print("Password Strength Checker")
    print("-" * 25)
    
    while True:
        password = input("\nEnter password (or 'quit' to exit): ")
        
        if password.lower() == 'quit':
            print("Goodbye!")
            break
            
        if not password:
            print("Please enter a password.")
            continue
            
        result = check_password_strength(password)
        
        print(f"\nStrength: {result['strength']} ({result['score']})")
        
        if result['suggestions']:
            print("Suggestions:")
            for suggestion in result['suggestions']:
                print(f"  • {suggestion}")
        else:
            print("✓ Password meets all criteria!")

if __name__ == "__main__":
    main()