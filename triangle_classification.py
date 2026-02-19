"""This module is used to classify triangles and if they are equilateral, scalene, or isosceles."""
def classify_triangle(a, b, c):
    """This is used to classify the triangle based on the different sides. 
The triangle has three sides (a,b,c)"""

    #Used a sort function to ensure the largest side is always for "c"
    #side as to test a right triangle the longest cide is "c"
    sides = sorted([a, b, c])
    a, b, c = sides

    if a <= 0 or b <= 0 or c <= 0:
        return "This is not a form of triangle."
    if a + b <= c or a+c <= b or b +c <=a:
        return "This is not a form of triangle."
    if a == b == c:
        return "The triangle is equilateral"
    if a == b or a == c or b == c:
        return "The triangle is isosceles"
    if a * a + b * b == c * c:
        return "The triangle is right"
    return "The triangle is scalene"
