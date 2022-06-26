import cv2
import numpy as np


class AsciiArt:

    CHARS = ' `.\',:^";*!²¤/r(?+¿cLª7t1fJCÝy¢zF3±%S2kñ5AZXG$À0Ãm&Q8#RÔßÊNBåMÆØ@¶'
    CHAR_WIDTH_TO_HEIGHT_RATIO = 0.5

    file: str
    white_background: bool
    height: int

    matrix: np.ndarray

    def main(
            self,
            file: str,
            white_background: bool,
            height: int):

        self.file = file
        self.white_background = white_background
        self.height = height

        self.read_image()
        self.convert_grey_scale()
        self.print_chars()

    def read_image(self):
        self.matrix = cv2.imread(self.file, 0)  # 0 for grey scale
        h, w = self.matrix.shape
        width = int(w * self.height / h)
        self.matrix = cv2.resize(
            src=self.matrix,
            dsize=(width, self.height)
        )

    def convert_grey_scale(self):
        scaling_factor = (len(self.CHARS) - 1) / 255
        self.matrix = self.matrix * scaling_factor
        self.matrix = self.matrix.round()
        self.matrix = self.matrix.astype(np.uint8)

    def print_chars(self):
        height, width = self.matrix.shape
        lines = []
        for y in range(height):
            line = self.get_line(pixel_array=self.matrix[y, :])
            lines.append(line)
        print('\n'.join(lines))

    def get_line(self, pixel_array: np.ndarray) -> str:
        chars = self.CHARS[::-1] if self.white_background else self.CHARS
        steps = int(len(pixel_array) // self.CHAR_WIDTH_TO_HEIGHT_RATIO)
        text = []
        for step in range(steps):
            start = step * self.CHAR_WIDTH_TO_HEIGHT_RATIO
            end = (step + 1) * self.CHAR_WIDTH_TO_HEIGHT_RATIO
            level = get_grey_level(start=start, end=end, pixel_array=pixel_array)
            c = chars[int(level)]
            text.append(c)
        return ''.join(text)


def get_grey_level(
        start: float,
        end: float,
        pixel_array: np.ndarray) -> float:

    if int(end) == int(start):
        return pixel_array[int(end)]
    elif int(end) == len(pixel_array):
        return pixel_array[-1]
    else:
        boundary = int(end)
        fraction = (boundary - start) / (end - start)
        return pixel_array[int(start)] * fraction + \
            pixel_array[int(end)] * (1 - fraction)
