class SevenSegmentDisplay:
    def __init__(self):
        self.is_on = False

    def display_segment(self, digits: str) -> str:
        self.validate(digits)
        self.change_status(digits)

        if not self.is_on:
            return ""

        return {
            "11111101": self.display_zero,
            "01100001": self.display_one,
            "11011011": self.display_two,
            "11110011": self.display_three,
            "01100111": self.display_four,
            "10110111": self.display_five,
            "10111111": self.display_six,
            "11100001": self.display_seven,
            "11111111": self.display_eight,
            "11110111": self.display_nine,
        }.get(digits, lambda: self._display_segment(*digits))()

    @staticmethod
    def _display_segment(*digits: str) -> str:
        output = [
            "# # # #" if digits[0] == '1' else "       ",
            ("#    " if digits[5] == '1' else "     ") + (" #" if digits[1] == '1' else "  "),
            "# # # #" if digits[6] == '1' else "       ",
            ("#  " if digits[4] == '1' else "   ") + ("   #" if digits[2] == '1' else "   "),
            "# # # #" if digits[3] == '1' else "       ",
        ]
        return "\n".join(output)

    @staticmethod
    def display_zero() -> str:
        return """
        # # # #
        #     #
        #     #
        #     #
        # # # #
        """

    @staticmethod
    def display_one() -> str:
        return """
              #
              #
              #
              #
              #
        """

    @staticmethod
    def display_two() -> str:
        return """
        # # # #
              #
        # # # #
        #
        # # # #
        """

    @staticmethod
    def display_three() -> str:
        return """
        # # # #
              #
        # # # #
              #
        # # # #
        """

    @staticmethod
    def display_four() -> str:
        return """
        #     #
        #     #
        # # # #
              #
              #
        """

    @staticmethod
    def display_five() -> str:
        return """
        # # # #
        #
        # # # #
              #
        # # # #
        """

    @staticmethod
    def display_six() -> str:
        return """
        # # # #
        #
        # # # #
        #     #
        # # # #
        """

    @staticmethod
    def display_seven() -> str:
        return """
        # # # #
              #
              #
              #
              #
        """

    @staticmethod
    def display_eight() -> str:
        return """
        # # # #
        #     #
        # # # #
        #     #
        # # # #
        """

    @staticmethod
    def display_nine() -> str:
        return """
        # # # #
        #     #
        # # # #
              #
        # # # #
        """

    def change_status(self, digits: str):
        self.is_on = digits[7] == '1'

    @staticmethod
    def validate(digits: str):
        if not digits.isdigit():
            raise ValueError("Binary number must be only digits")
        if not all(char in '01' for char in digits):
            raise ValueError("Binary number must consist of only 0s and 1s")
        if len(digits) != 8:
            raise ValueError("Binary number must be 8 digits long")

    def is_on(self) -> bool:
        return self.is_on
