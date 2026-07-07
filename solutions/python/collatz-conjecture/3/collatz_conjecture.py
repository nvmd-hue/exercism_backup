def steps(number):
    steps_taken = 0
    working_number = number
    
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    while working_number > 1:
        if working_number % 2 == 0:
            working_number = working_number // 2
            steps_taken = steps_taken + 1
            continue
        
        working_number = (working_number * 3) + 1
        steps_taken = steps_taken + 1
        continue
            
    return steps_taken


