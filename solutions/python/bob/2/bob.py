def response(hey_bob):
    clean_text = hey_bob.strip()
    
    if not clean_text:
        return "Fine. Be that way!"

    is_shouting = clean_text.isupper()
    is_question = clean_text.endswith("?")

    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
        
    if is_shouting:
        return "Whoa, chill out!"
        
    if is_question:
        return "Sure."
    
    return "Whatever."
    
    
