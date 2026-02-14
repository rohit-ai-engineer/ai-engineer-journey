# Simple Calculator - Week 1 Project

print ("Welcome to my calculator!")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
             

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2

print("--- Results ---")
print("Addition:      ", round(addition, 2))
print("Subtraction:   ", round(subtraction, 2))
print("Multiplication:", round(multiplication, 2))
print("Division:      ", round(division, 2))
