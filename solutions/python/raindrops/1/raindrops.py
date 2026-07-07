def convert(number):
    string_result = ""

    if number % 3 == 0:
        string_result += "Pling"
    if number % 5 == 0:
        string_result += "Plang"
    if number % 7 == 0:
        string_result += "Plong"
    
    return string_result if string_result else str(number)
    
