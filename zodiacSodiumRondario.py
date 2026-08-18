import sys

def main():
    # 1. Input statement
    try:
        birth_year = int(input("Enter your birth year: "))
    except ValueError:
        print("Invalid input. Please enter a valid numerical year.")
        sys.exit()

    # 2. Selection structure for input validation
    if birth_year < 1900:
        print("Invalid Year, it should not be earlier than 1900")
        sys.exit()

    # 3. Zodiac animals ordered by remainder offset from 1900
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

    # 4. Calculate index using modulo 12
    zodiac_index = (birth_year - 1900) % 12
    zodiac_sign = zodiac_signs[zodiac_index]

    # 5. Output result
    print(f"\nYour Chinese Zodiac Sign is : {zodiac_sign}")

if __name__ == "__main__":
    main()