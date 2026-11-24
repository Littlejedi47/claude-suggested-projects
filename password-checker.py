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

        self.total_categories = 4

        self.minimum_password_length = 4
        self.maximum_password_length = 64

        self.reset_evaluation_values_to_false()

    def get_password_for_evaluation(self):
        self.password = gp.getpass("Enter a password to Evaluate(q to quit): ")

    def reset_evaluation_values_to_false(self):
        """Reset the state of each variable to false for revaluation."""
        self.is_lowercase = False
        self.is_uppercase = False
        self.is_symbol = False
        self.is_digits = False
        self.is_whitespace = False  # This condition should stay False.

    def password_evaluation(self):
        """Evaluate if password has lowercase,uppercase,digit,symbol and white space."""
        self.reset_evaluation_values_to_false()
        self.total_categories_present = 0
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

        for i in range(1):
            if self.is_lowercase:
                self.total_categories_present += 1
            if self.is_uppercase:
                self.total_categories_present += 1
            if self.is_digits:
                self.total_categories_present += 1
            if self.is_symbol:
                self.total_categories_present += 1

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

    def count_password_categories(self):
        """Count the presence of each category in the password."""
        self.password_evaluation()

        self.lowercase_count = 0
        self.uppercase_count = 0
        self.digits_count = 0
        self.symbol_count = 0

        for char in (self.password):
            # Lowercase
            if char in self.lowercase:
                self.lowercase_count += 1
            # Uppercase
            if char in self.uppercase:
                self.uppercase_count += 1
            # Digit
            if char in self.digits:
                self.digits_count += 1
            # Symbol
            if char in self.symbol:
                self.symbol_count += 1

        print("-----------------------------------------------")
        print(f"Total categories present: {self.total_categories_present}/{self.total_categories}")
        print(f"Lowercase:{self.lowercase_count} Uppercase:{self.uppercase_count} Digit:{self.digits_count} Symbol:{self.symbol_count}")
        print("-----------------------------------------------")

    def run_program(self):
        """Methods are executed in this block."""
        os.system('cls' if os.name == 'nt' else 'clear')
        self.get_password_for_evaluation()
        
        while True:
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
            
            if len(self.password) < self.minimum_password_length:
                print(f"\nPassword must have a minimum of {self.minimum_password_length} characters.\n")
                self.get_password_for_evaluation()
            elif len(self.password) > self.maximum_password_length:
                print(f"\nPassword must have a maximum of {self.maximum_password_length} characters.\n")
                self.get_password_for_evaluation()
            elif self.is_lowercase and self.is_uppercase and self.is_digits and self.is_symbol and self.is_whitespace == False:
                self.count_password_categories()
                print("** Your password meets all conditions. **")
                break
            else:
                self.count_password_categories()
                self.get_password_for_evaluation()


if __name__ == '__main__':
    pc = PasswordChecker()
    pc.run_program()