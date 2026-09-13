from datetime import datetime
import calendar

DIGITS = {
    '0':[
        "*****",
        "*   *",
        "*   *",
        "*   *",
        "*****"
    ],
    '1': [
        "    *",
        "    *",
        "    *",
        "    *",
        "    *"
    ],
    "2" : [
        "*****",
        "    *",
        "*****",
        "*    ",
        "*****"
    ],
    "3" : [
        "*****",
        "    *",
        "*****",
        "    *",
        "*****"
    ],
    "4" : [
        "*   *",
        "*   *",
        "*****",
        "    *",
        "    *"
    ],
    "5" : [
        "*****",
        "*    ",
        "*****",
        "    *",
        "*****"
    ],
    "6" : [
        "*****",
        "*    ",
        "*****",
        "*   *",
        "*****"
    ],
    "7" : [
        "*****",
        "    *",
        "    *",
        "    *",
        "    *"
    ],
    "8" : [
        "*****",
        "*   *",
        "*****",
        "*   *",
        "*****"
    ],
    "9" : [
        "*****",
        "*   *",
        "*****",
        "    *",
        "*****"
    ]}

def get_weekday(day, month,year):
    try:
        date_obj = datetime(year, month, day)
        weekdays=["понедельник","вторник","среда","четверг","пятница","суббота","воскресенье"]
        return weekdays[date_obj.weekday()]
    except ValueError:
        return None

def is_leap_year(year):
    return (year %4 ==0 and year %100 != 0) or (year%400 ==0)

def calculate_age(day, month, year):
    today = datetime.now()
    birth = datetime(year, month, day)
    age = today.year - birth.year
    if (today.month, today.day)< (birth.month,birth.day):
        age -=1
    return age

def print_number_as_digits(number_str):
    lines = ["" for _ in range(5)]

    for char in number_str:
        if char in DIGITS:
            digit_lines = DIGITS[char]
            for i in range(5):
                lines[i] += digit_lines[i]+"  "
        else:
            for i in range(5):
                lines[i] += "     "
    
    for line in lines:
        print(line)

def print_date_as_display(day, month, year):
    date_str= f"{day:02d} {month:02d} {year:04d}"
    print_number_as_digits(date_str)

def main():
    try:
        day = int(input('день рождения'))
        month = int(input('месяц рождения'))
        year = int(input('год рождения'))

        try:
            datetime(year,month,day)
        except ValueError:
            print('неправильная дата')
            return
        
        weekday = get_weekday(day,month,year)
        if weekday:
            print(f"\n день недели: {weekday}")
        else:
            print("\n error")
            return
        
        if is_leap_year(year):
            print("високосный")
        else:
            print("невисокосный")
        
        age = calculate_age(day,month,year)
        print(f" Вам сейчас {age} лет")

        print_date_as_display(day,month,year)
    
    except ValueError:
        print("Ошибка ввода")

if __name__ == "__main__":
    main()
    
