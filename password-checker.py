import getpass as gp
import string
import os

class PasswordChecker:
    """Evaluate the length, strength and the chances of brute forcing a password."""

    def __init__(self):
        """Initializing variables."""
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.symbol = string.punctuation
        self.digits = string.digits
        self.whitespace = string.whitespace

        self.is_lowercase = False
        self.is_uppercase = False
        self.is_symbol = False
        self.is_digits = False
        self.is_whitespace = False  # This condition should stay False.

    def get_password_for_evaluation(self):
        self.password = gp.getpass("Enter a password to Evaluate(q to quit): ")

    def reset_evaluation_values(self):
        self.is_lowercase = False
        self.is_uppercase = False
        self.is_symbol = False
        self.is_digits = False
        self.is_whitespace = False

    def password_evaluation(self):
        """Evaluate if password has lowercase,uppercase,digit,symbol and white space."""
        self.reset_evaluation_values()
        for char in self.password:
            # Lowercase
            if char in self.lowercase:
                self.is_lowercase = True
            # Uppercase
            if char in self.uppercase:
                self.is_uppercase = True
            # Digit
            if char in self.digits:
                self.is_digits = True
            # Symbol
            if char in self.symbol:
                self.is_symbol = True
            # White space
            if char in self.whitespace:
                self.is_whitespace = True
    def password_evaluation_response(self):
        # Respond with evaluation.
        print(f"\nLength: {len(self.password)} characters.\n")

        # Lowercase
        if self.is_lowercase:
            print("Lowercase  (OK)")
        elif not self.is_lowercase:
            print("Lowercase  (X)")
        # Uppercase
        if self.is_uppercase:
            print("Uppercase  (OK)")
        elif not self.is_uppercase:
            print("Uppercase  (X)")
        # Digit
        if self.is_digits:
            print("Digit      (OK)")
        elif not self.is_digits:
            print("Digit      (X)")
        # Symbol
        if self.is_symbol:
            print("Symbol     (OK)")
        elif not self.is_symbol:
            print("Symbol     (X)")
        # White space
        if self.is_whitespace:
            print("Can't have white space!")

    def run_program(self):
        """Methods are executed in this block."""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.get_password_for_evaluation()
        
        while True:
            # self.reset_evaluation_values()
            if self.password.lower() == 'q':
                print("\n------------ See you later. ------------")
                break
            elif self.password == '':
                print("\nEmpty field, try again.")
                print("-----------------------")
                self.get_password_for_evaluation()
                continue

            self.password_evaluation()
            self.password_evaluation_response()
            
            if len(self.password) < 4:
                print("\nPassword must have a minimum of 4 characters.\n")
                self.get_password_for_evaluation()
            elif len(self.password) > 64:
                print("\nPassword must have a maximum of 64 characters.\n")
                self.get_password_for_evaluation()
            elif self.is_lowercase == True and self.is_uppercase == True and self.is_digits == True and self.is_symbol == True and self.is_whitespace == False:
                break
            elif self.is_lowercase == False or self.is_uppercase == False or self.is_digits == False or self.is_symbol == False or self.is_whitespace == True:
                self.get_password_for_evaluation()




if __name__ == '__main__':
    pc = PasswordChecker()
    pc.run_program()