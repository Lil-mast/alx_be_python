import sys
from bank_account import BankAccount

def main():
    # Initialize account with a starting balance of $100
    account = BankAccount(100)
    
    # Check if command line arguments are provided
    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)
    
    try:
        # Parse command and parameters
        command, *params = sys.argv[1].split(':')
        amount = float(params[0]) if params and params[0] else None
        
        # Execute the appropriate command
        if command == "deposit" and amount is not None:
            if amount > 0:
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            else:
                print("Deposit amount must be positive.")
        elif command == "withdraw" and amount is not None:
            if amount > 0:
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            else:
                print("Withdrawal amount must be positive.")
        elif command == "display":
            account.display_balance()
        else:
            print("Invalid command or missing amount.")
            print("Usage: python main.py <command>:<amount>")
            print("Commands: deposit, withdraw, display")
    
    except ValueError:
        print("Invalid amount. Please provide a numeric value.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()