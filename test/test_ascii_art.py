import numpy as np
from ascii_art.ascii_art import AsciiArt, get_grey_level
from .setup import TestCase


class TestAsciiArt(TestCase):

    def setUp(self):
        self.set_up(py_path=__file__)
        self.art = AsciiArt()

    def tearDown(self):
        self.tear_down()

    def test_main(self):
        self.art.main(
            file=f'{self.indir}/snow.png',
            white_background=False,
            height=100)


class TestGetGreyLevel(TestCase):

    def test_within_pixel(self):
        actual = get_grey_level(
            start=0.0,
            end=0.1,
            pixel_array=np.array([0, 10, 20, 30, 40])
        )
        expected = 0.
        self.assertEqual(expected, actual)

    def test_across_pixel(self):
        actual = get_grey_level(
            start=0.9,
            end=1.3,
            pixel_array=np.array([0, 10, 20, 30, 40])
        )
        expected = 7.5
        self.assertEqual(expected, actual)

    def test_on_boundary(self):
        actual = get_grey_level(
            start=1.9,
            end=2.,
            pixel_array=np.array([0, 10, 20, 30, 40])
        )
        expected = 10.
        self.assertEqual(expected, actual)

    def test_end_on_boudnary(self):
        actual = get_grey_level(
            start=4.5,
            end=5.,
            pixel_array=np.array([0, 10, 20, 30, 40])
        )
        expected = 40.
        self.assertEqual(expected, actual)

