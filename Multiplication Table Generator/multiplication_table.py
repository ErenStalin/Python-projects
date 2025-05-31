def tables():
    
    
    try:
        user = int(input('Enter only numbers to fetch the tables that required fro your calculation : '))
        for i in range(1,11):
            multi = i * user
            print(f"{user} * {i} = {multi}")
    
    except ValueError as e:
        print("Only numbers are allowed")

tables()