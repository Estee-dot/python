import unittest
from sevensegment import SevenSegmentDisplay


class MyTestCase(unittest.TestCase):
        display = None

        def initialize_display(self):
            self.display = SevenSegmentDisplay()

        def test_user_inputs_non_digit_numbers_throws_non_digit_number_exception(self):
            with self.assertRaises(NonDigitNumberException):
                self.display.display_segment("1234s678")

        def test_user_inputs_non_binary_digit_numbers_throws_non_binary_number_exception(self):
            with self.assertRaises(NonDigitNumberException) :
                self.display.display_segment("12345678")

        def test_user_inputs_more_than_8_digit_numbers_throws_illegal_argument_exception(self):
            with pytest.raises(ValueError):
                self.display.display_segment("010011101")

        def test_user_inputs_less_than_8_digit_numbers_throws_illegal_argument_exception(self):
            with pytest.raises(ValueError):
                self.display.display_segment("1110001")

        def test_given_11111100_board_is_off(self):
            self.display.display_segment("11111100")
            assert not self.display.is_on()

        def test_given_11111101_board_is_on(self):
            self.display.display_segment("11111101")
            assert self.display.is_on()
            self.display.display_segment("11111100")
            assert not self.display.is_on()

        def test_given_11111100_is_off_then_empty_string_is_displayed(self):
            assert not self.display.is_on()
            assert self.display.display_segment("11111100") == ""

        def test_given_11111101_board_is_on_when_displayed_then_hashtags_representing_zero_is_displayed(self):
            actual = self.display.display_segment("11111101")
            assert self.display.is_on()
            expected = """
            # # # #
            #     #
            #     #
            #     #
            # # # #
            """
            assert actual == expected
            print(actual)

        def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_one_is_displayed(self):
            actual = self.display.display_segment("01100001")
            assert self.display.is_on()
            expected = """
                      #
                      #
                      #
                      #
                      #
            """
            assert actual == expected
            print(actual)

        def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_two_is_displayed(self):
            actual = self.display.display_segment("11011011")
            assert self.display.is_on()
            expected = """
            # # # #
                  #
            # # # #
            #
            # # # #
            """
            assert actual == expected
            print(actual)

        def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_three_is_displayed(self):
            actual = self.display.display_segment("11110011")
            assert self.display.is_on()
            expected = """
            # # # #
                  #
            # # # #
                  #
            # # # #
            """
            assert actual == expected
            print(actual)

        def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_four_is_displayed(self):
            actual = self.display.display_segment("01100111")
            assert self.display.is_on()
            expected = """
            #     #
            #     #
            # # # #
                  #
                  #
            """
            assert actual == expected
            print(actual)

        def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_five_is_displayed(self):
            actual = self.display.display_segment("10110111")
            assert self.display.is_on()
            expected = """
            # # # #
            #
            # # # #
                  #
            # # # #
            """
            assert actual == expected
            print(actual)

        def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_six_is_displayed(self):
            actual = self.display.display_segment("10111111")
            assert self.display.is_on()
            expected = """
            # # # #
            #
            # # # #
            #     #
            # # # #
            """
            assert actual == expected
            print(actual)

        def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_seven_is_displayed(self):
            actual = self.display.display_segment("11100001")
            assert self.display.is_on()
            expected = """
            # # # #
                  #
                  #
                  #
                  #
            """
            assert actual == expected
            print(actual)

        def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_eight_is_displayed(self):
            actual = self.display.display_segment("11111111")
            assert self.display.is_on()
            expected = """
            # # # #
            #     #
            # # # #
            #     #
            # # # #
            """
            assert actual == expected
            print(actual)

        def test_given_01100001_board_is_on_when_displayed_then_hashtags_representing_nine_is_displayed(self):
            actual = self.display.display_segment("11110111")
            assert self.display.is_on()
            expected = """
            # # # #
            #     #
            # # # #
                  #
            # # # #
            """
            assert actual == expected
            print(actual)



if __name__ == '__main__':
    unittest.main()
