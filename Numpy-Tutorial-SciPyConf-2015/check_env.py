""" Run this file to check your python installation.
"""
from numpy.testing import assert_array_equal


def test_import_numpy():
    import numpy


def test_pandas_version():
    import numpy
    version_found = numpy.__version__.split(".")
    version_found = tuple(int(num) for num in version_found)
    assert version_found > (1, 8)


def test_import_matplotlib():
    from matplotlib.pyplot import plot


def test_slicing():
    from numpy import array
    x = array([[1, 2, 3], [4, 5, 6]])
    assert_array_equal(x[:, ::2], array([[1, 3], [4, 6]]))


if __name__ == "__main__":
    import nose
    nose.run(defaultTest=__name__)
