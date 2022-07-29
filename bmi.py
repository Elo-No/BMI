def user_input():
    try:
        var = int(input(f"Enter : "))
        if var == 0 or isinstance(var, complex) or isinstance(var, bool):
            print('invalid input, Try again : ')
            return user_input()
        else:
            return var
    except:
        print("something happened wrong , Try again :")
        return user_input()


def calculate_bmi():

    print("Enter Height and Weight in order")
    h = user_input()
    w = user_input()
    height = h * 0.01
    bmi = w / (height * height)
    min_normal_weight = round(18.5 * (height * height))
    max_normal_weight = round(24.9 * (height * height))

    if bmi < 18.5:
        print(
            f'bmi = {round(bmi)}, Below Normal Weight , increase ur Weight to =({min_normal_weight}~{max_normal_weight})')

    elif (18.5 <= bmi) and (bmi <= 24.9):
        print(f'bmi = {round(bmi)}, Normal Weight')

    elif (25 <= bmi) and (bmi <= 29.9):
        print(
            f'bmi = {round(bmi)}, Overweight , decrease ur Weight to =({min_normal_weight}~{max_normal_weight})')

    elif (30 <= bmi) and (bmi <= 34.9):
        print(
            f'bmi = {round(bmi)}, Overweight Class 1 , decrease ur Weight to = ({min_normal_weight}~{max_normal_weight})')
    else:
        print(
            f'bmi = {round(bmi)},Overweight Class 2, decrease ur Weight to =({min_normal_weight}~{max_normal_weight})')


if __name__ == "__main__":
    calculate_bmi()
