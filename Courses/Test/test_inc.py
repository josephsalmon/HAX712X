from inc import inc1, inc2

# This test will work


def test_inc1():
    assert inc1(3) == 4


# This test will fail
def test_inc2():
    # assert inc2(-1) == 4
    assert inc2(2) == 4
