#exercise 1
def calculate_bmi(weight,height):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi = weight/(height*height)
    print(f"BMI= {bmi:.2f}")
    if bmi<18.5:
        print("Underweight")
        return -1
    elif bmi>25.0:
        print("Overweight")
        return 1
    else:
        print("Normal weight")
        return 0
calculate_bmi(weight=57,height=1.73) 
