import pytest
import triangle_classification  

def test_l():
    assert triangle_classification.classify_triangle(3, 2, 5) == "The triangle is equilateral"

#Test to check if it tell if it is a triangle if one of the sides is 0.
def test_2():
    assert triangle_classification.classify_triangle(3, 0, 3) == "This triangle is equilateral"

def test_3():
    assert triangle_classification.classify_triangle(3,3,3) =="The triangle is equilateral"

def test_4():
    assert triangle_classification.classify_triangle(2,1,2) == "The triangle is isosceles"

#Test to see if it will return equilateral or isosceles triangle. It should return equilateral.
def test_5():
    assert triangle_classification.classify_triangle(4, 4, 4) == "The triangle is isosceles"

def test_6():
    assert triangle_classification.classify_triangle(4,4,2) == "The triangle is isosceles"

def test_7():
    assert triangle_classification.classify_triangle(2,3,4) == "The triangle is scalene"

#Test to check if the triangle is right and if it sorted the sides since 5 should be for "c" side
def test_8():
    assert triangle_classification.classify_triangle(3,5,4) == "The triangle is right"



