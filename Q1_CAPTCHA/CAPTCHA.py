import random
import string

class CaptchaGenerator:
    def generate(self):
        characters = string.ascii_uppercase + string.digits
        return "".join(random.choices(characters, k=5))

class CaptchaValidator:
    def check(self, originalCode, userInput):
        return userInput.strip().upper() == originalCode.upper()

class CaptchaSession:

    MAX_ATTEMPTS = 3

    def __init__(self):
        self.attempts = 0
        self.generator = CaptchaGenerator()
        self.validator = CaptchaValidator()
        self.currentCode = None

    def newChallenge(self):
        self.currentCode = self.generator.generate()
        return self.currentCode

    def submit(self, userInput):

        if self.validator.check(self.currentCode, userInput):
            return "correct"

        self.attempts += 1

        if self.attempts >= self.MAX_ATTEMPTS:
            return "locked"

        return "incorrect"

def run():

    print("CAPTCHA Verification")

    session = CaptchaSession()

    while True:

        captcha = session.newChallenge()
        print("CAPTCHA:", captcha)

        userInput = input("Enter CAPTCHA: ")

        result = session.submit(userInput)

        if result == "correct":
            print("Verification Successful")
            break

        elif result == "locked":
            print("Too many incorrect attempts. Access denied.")
            break

        else:
            remaining = CaptchaSession.MAX_ATTEMPTS - session.attempts
            print("Incorrect CAPTCHA")
            print("Attempts remaining:", remaining)

run()
