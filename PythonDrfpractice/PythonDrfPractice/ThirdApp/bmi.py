

def bmiweight(height, weight):
    height = (height)
    weight = (weight)
    BMI = weight / (height / 100) ** 2.
    BMI = round(BMI, 2)
    return BMI