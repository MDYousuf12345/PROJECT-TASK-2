def calculate_bmi():
    print("Welcome to the BMI Calculator!")

    
    try:
        weight = float(input("Enter your weight (in kilograms): "))
        height = float(input("Enter your height (in meters): "))

        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive numbers.")
            return

        
        bmi = weight / (height ** 2)

        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 24.9:
            category = "Normal weight"
        elif 25 <= bmi < 29.9:
            category = "Overweight"
        else:
            category = "Obesity"

        
        print(f"\nYour BMI is: {bmi:.2f}")
        print(f"You are classified as: {category}")

    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    calculate_bmi()
