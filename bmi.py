def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than 0.")
    return weight / (height ** 2)
