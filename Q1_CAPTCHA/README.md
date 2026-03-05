# CAPTCHA Verification System Architecture

## Overview
This project implements a basic CAPTCHA verification system used to distinguish human users from automated programs. The system generates a random CAPTCHA, asks the user to enter the characters shown, verifies the response, and restricts the number of attempts to prevent brute-force guessing.

The design follows a modular architecture where CAPTCHA generation, validation, and session management are handled by separate components.


## System Components

### 1. User Interface Layer
This layer manages the interaction between the user and the system.

**Responsibilities**
- Display the generated CAPTCHA
- Accept user input
- Display verification results

**Example**
print("CAPTCHA:", captcha)
userInput = input("Enter CAPTCHA: ")


---

### 2. CAPTCHA Generator
The CAPTCHA generator creates the challenge that the user must solve.

**Component**
generate()


**Responsibilities**
- Generate random characters
- Use uppercase letters and digits
- Produce a CAPTCHA challenge

---

### 3. CAPTCHA Validator
This component v
erifies whether the user's input matches the generated CAPTCHA.

**Responsibilities**
- Compare user input with the generated CAPTCHA
- Ignore case differences
- Return validation result

---

### 4. CAPTCHA Session Manager
This component manages the CAPTCHA verification session.


**Responsibilities**
- Store the generated CAPTCHA
- Track the number of attempts
- Lock the system after reaching the maximum attempts

**Key Variables**
self.attempts
self.currentCode
MAX_ATTEMPTS


---

### 5. Verification Controller
This controller manages the overall workflow of the system.


**Responsibilities**
- Generate CAPTCHA challenges
- Collect user input
- Validate responses
- Handle retry attempts
- Display success or failure messages

---

## System Flow
User
↓
User Interface
↓
Captcha Generator
↓
Display CAPTCHA
↓
User Input
↓
Captcha Validator
↓
Captcha Session Manager
↓
┌──────────────┬──────────────┬──────────────┐
│ Correct │ Incorrect │ Max Attempts │
│ Access Grant │ Retry │ Access Denied│
└──────────────┴──────────────┴──────────────┘


---

## Components Summary

| Component | Description |
|-----------|-------------|
| User Interface | Displays CAPTCHA and collects user input |
| CAPTCHA Generator | Generates random CAPTCHA codes |
| CAPTCHA Validator | Verifies user input |
| CAPTCHA Session Manager | Tracks attempts and manages session state |
| Verification Controller | Controls system workflow |

---

## Features

- Random CAPTCHA generation
- Case-insensitive validation
- Limited retry attempts
- Session-based verification
- Access control after multiple failed attempts

---

## Conclusion

This CAPTCHA system demonstrates a simple but structured approach to human verification. By separating generation, validation, and session management, the architecture becomes easier to maintain and extend in larger systems.
