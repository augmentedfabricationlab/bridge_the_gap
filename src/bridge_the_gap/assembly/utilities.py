import math as m
from compas.geometry import Frame, Vector, angle_vectors


def check_type(frame):
    """Return the type of the element.
    """

    a = abs(frame.xaxis.dot(Vector.Zaxis()))
    b = abs(frame.xaxis.dot(Vector.Yaxis()))

    if a > 0.9:
        elem_type = 'Z'
    elif a < 0.1:
        if b > 0.9:
            elem_type = 'Y'
        else:
            elem_type = 'X'
    else:
        elem_type = None

    return elem_type
