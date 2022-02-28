import pytest
from game_math import *

def test_vec_creation():
    v = Vector4(1, 2, 3, 1)
    assert v.x == 1
    assert v.y == 2
    assert v.z == 3
    assert v.w == 1

    v = Vector3(3.5, 6.7, 8.1)
    assert v.x == 3.5
    assert v.y == 6.7
    assert v.z == 8.1
    assert v.w == 0

    v = Vector2(8.9, 2.3)
    assert v.x == 8.9
    assert v.y == 2.3
    assert v.z == 0
    assert v.w == 0

def test_eq():
    v = Vector4(2.3, 4.6, 8.2, 0)
    w = Vector4(2.3, 4.6, 8.2, 0)
    assert v == w
    v = Vector3(6.5, 7.22, 9.01)
    w = Vector3(6.5, 7.22, 9.01)
    assert v == w
    v = Vector2(91.2, 903.8)
    w = Vector2(91.2, 903.8)
    assert v == w

def test_add():
    a = Vector4(1, 2, 3, 1)
    b = Vector4(3, 4, 2, 1)
    c = a + b
    assert c.x == 4
    assert c.y == 6
    assert c.z == 5
    assert c.w == 0


def test_sub():
    a = Vector4(1, 2, 3, 1)
    b = Vector4(3, 4, 2, 1)
    c = a - b
    assert c.x == -2
    assert c.y == -2
    assert c.z == 1
    assert c.w == 0

def test_scale():
    v = Vector4(2, 6, 7, 0)
    s = 3
    w = v.scale(s)
    assert isinstance(w, Vector4)
    assert w.x == 6
    assert w.y == 18
    assert w.z == 21
    assert w.w == v.w

    v = Vector3(10, -20, 1)
    s = 9
    w = v.scale(s)
    assert isinstance(w, Vector4)
    assert w.x == 90
    assert w.y == -180
    assert w.z == 9
    assert w.w == 0

    v = Vector2(.3, 8.2)
    s = 2.4
    w = v.scale(s)
    assert isinstance(w, Vector4)
    assert w.x == pytest.approx(0.72, 0.1)
    assert w.y == pytest.approx(19.67, 0.1)
    assert w.z == 0
    assert w.w == 0

def test_dot():
    v = Vector4(1.2, 3.5, 9.1, 0)
    w = Vector4(1.6, 2.7, 0.2, 0)
    d = v * w
    assert d == pytest.approx(13.19)

    w = Vector4(-1.3, -9.2, -1.3, 0)
    d = v * w
    assert d == pytest.approx(-45.59, 0.1)

    d = w * v
    assert d == pytest.approx(-45.59, 0.1)

    v = Vector3(1, 2, 3)
    w = Vector3(4, 5, 6)
    d = w * v
    assert d == 32

def test_normalized():
    v = Vector4(3, 5, 6)
    w = v.normalize()
    assert w.magnitude() == pytest.approx(1.0, 0.1)
    assert w.x == pytest.approx(0.35, 0.1)
    assert w.y == pytest.approx(0.59, 0.1)
    assert w.z == pytest.approx(0.71, 0.1)

def test_cross():
    v = Vector4(2, 3, 4)
    w = Vector4(5, 6, 7)
    d = v.cross(w)
    assert d.x == -3
    assert d.y == 6
    assert d.z == -3

def test_matrix():
    d = Matrix()
    assert d.rows == 4
    assert d.cols == 4
    assert d.data[0][0] == 1
    assert d.data[1][1] == 1
    assert d.data[2][2] == 1
    assert d.data[3][3] == 1

def test_mul_matrix():
    a = Matrix()
    b = Matrix()
    a.data[0] = [1, 2, 3, 4]
    a.data[1] = [1, 2, 3, 4]
    a.data[2] = [1, 2, 3, 4]
    a.data[3] = [1, 2, 3, 4]
    c = a * b
    assert c.data[0][3] == 4
    b.data[3] = [3, 3, 3, 1]
    c = a * b
    assert c.data[0][0] == 13
    assert c.data[1][1] == 14
    assert c.data[2][2] == 15
    assert c.data[3][3] == 4

def test_vec_mul():
    a = Matrix()
    v = Vector4(1, 2, 3, 1)
    a.data[3] = [3, 3, 3, 1]
    n = a.vec_mul(v)
    assert n.x == 4
    assert n.y == 5
    assert n.z == 6
    assert n.w == 1
