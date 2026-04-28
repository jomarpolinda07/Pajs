def withdrawal_system():
    balance = 2000  
    
    print("\n    WELCOME TO THE SMART BANK   ")
    
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Check Balance")
        print("2. Withdraw Money")
        print("3. Exit")
        
        choice = input("\nPlease select an option (1-3): ")

        if choice == '1':
            print("\n> Current Balance: $", balance)

        elif choice == '2':
            
            try:
                amount_input = input("Enter amount to withdraw: ")
                amount = float(amount_input)

                if amount > balance:
                    print("\n[!] Error: Insufficient funds.")
                else:  
                    balance -= amount
                    print("\n> Withdrawal successful. New balance: $", balance)
            except ValueError:
                print("\n[!] Error: Please enter a valid number.")

             

        elif choice == '3':
            print("\nThank you. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    withdrawal_system()