import getpass as gp
import string
import os



class PasswordChecker:
    """Evaluate the length, strength and the chances of brute forcing a password."""

    def __init__(self):
        self.password = gp.getpass("\n\nEnter a password to Evaluate: ")
        
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

    def evaluate_password(self):
        """Evaluate if password has lowercase,uppercase,digit,symbol and white space."""

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

    def character_evaluation_response(self):
        """Clear screen and respond with evaluation."""

        os.system('cls' if os.name == 'nt' else 'clear')

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
            print("Number     (OK)")
        elif not self.is_digits:
            print("Number     (X)")
        # Symbol
        if self.is_symbol:
            print("Symbol     (OK)")
        elif not self.is_symbol:
            print("Symbol     (X)")
        # White space
        if self.is_whitespace == True:
            print("Can't have white space!")
        elif self.is_whitespace == False:
            print("White space (OK)")
        
            
    def run_programme(self):
        """Methods are executed in this block."""

        while True:
            
            self.evaluate_password()
            self.character_evaluation_response()
            

            exit() # Without the exit function, The while loop would never stop.




if __name__ == '__main__':
    pc = PasswordChecker()
    pc.run_programme()