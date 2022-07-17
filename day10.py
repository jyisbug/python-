# Function with outputs

def format_name(f_name, l_name):
    F_name = f_name.title()
    L_name = l_name.title()
    return f"{F_name} {L_name}"  # return 后面的代码不会运行，因为return 就已经默认函数结束了


formated_string = format_name("jiayuan", "liu")
print(formated_string)

# exercise 10.1
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        False


def days_in_month(year, month):
    """判断月份有几天"""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) == True:
        month_days[1] = 29
    return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
