# Activity 3: Implementing Selection Structure - Chinese Zodiac Sign

## Problem Requirements
Create a Python program that calculates the Chinese Zodiac sign based on a birth year from 1900 onwards.
- Asks the user to enter a birth year (baseline year is 1900).
- Validates user input to ensure the year is not earlier than 1900.
- Displays an error message and stops execution if an invalid year is entered.
- Determines the Chinese Zodiac sign using a 12-year repeating cycle starting from 1900.

## Source Code (`zodiacSectionLN.py`)

```python
import sys

def main():
    try:
        birth_year = int(input("Enter your birth year: "))
    except ValueError:
        print("Invalid input. Please enter a valid numerical year.")
        sys.exit()

    if birth_year < 1900:
        print("Invalid Year, it should not be earlier than 1900")
        sys.exit()

    zodiac_signs = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]

    zodiac_index = (birth_year - 1900) % 12
    print(f"\nYour Chinese Zodiac Sign is : {zodiac_signs[zodiac_index]}")

if __name__ == "__main__":
    main()

![Output Screenshot](Screenshot (68).png)
