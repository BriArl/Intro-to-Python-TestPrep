try:
    user_num = int(input())
    div_num = int(input())
    
    quotient = user_num // div_num
    print(quotient)
    
except ZeroDivisionError:
    print("Zero Division Exception: integer division or modulo by zero")
    
except ValueError as e:
    print(f"Input Exception: {e}")