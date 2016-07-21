def check(sequence,  code="ATGCM"):
    for base in sequence: 
        if base not in code: 
            return False 
    return True
