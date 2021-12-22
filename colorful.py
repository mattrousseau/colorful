def is_colorful(number):
    number_as_string = str(number)

    if len(number_as_string) == 1:
        return True

    if "0" in number_as_string or "1" in number_as_string:
        return False

    number_list = [digit for digit in number_as_string]

    if len(number_list) != len(set(number_list)):
        return False

    for width in range(2, len(number_as_string)):
        for i in range(len(number_as_string) - width + 1):
            slice = number_as_string[i : i + width]
            result = 1
            for digit in slice:
                result *= int(digit)

            if str(result) in number_list:
                return False

            number_list.append(str(result))
    return True

if __name__ == '__main__':
    is_colorful(3245)
