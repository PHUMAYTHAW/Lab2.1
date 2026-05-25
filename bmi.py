#exercise 1
def calculate_bmi(weight,height):
    print("Height="+str(height))
    print("Weight="+str(weight))
    bmi = weight/(height*height)
    print(f"BMI= {bmi:.2f}")
    if bmi<18.5:
        print("Underweight")
    elif bmi>25.0:
        print("Overweight")
    else:
        print("Normal weight")
calculate_bmi(weight=57,height=1.73) 
