def equilateral(sides):
    """Returns True if the triangle is equilateral."""
    return is_valid_triangle(sides) and len(set(sides)) == 1

def isosceles(sides):
    """Returns True if the triangle is isosceles (at least 2 sides equal)."""
    # A set of sides with length <= 2 means either 2 sides are equal or all 3 are equal
    return is_valid_triangle(sides) and len(set(sides)) <= 2

def scalene(sides):
    """Returns True if the triangle is scalene (all sides different)."""
    return is_valid_triangle(sides) and len(set(sides)) == 3

def is_valid_triangle(sides):
    # Check if we have exactly 3 sides and all are > 0
    if len(sides) != 3 or any(s <= 0 for s in sides):
        return False
    
    # Sort sides to easily check the inequality: smallest + middle >= largest
    a, b, c = sorted(sides)
    return (a + b) >= c