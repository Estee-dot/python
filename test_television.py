import unittest
from __init__ import Television

class TestTelevisionFunction(unittest.TestCase):
    def test_that_tv_is_off_by_default(self):
        television = Television()
        self.assertFalse(television.is_on())

    def test_that_tv_can_turn_on(self):
        television = Television()
        self.assertFalse(television.is_on())
        television.turn_on()
        self.assertTrue(television.is_on())

    def test_that_tv_can_turn_off(self):
        television = Television()
        self.assertFalse(television.is_on())
        television.turn_on()
        self.assertTrue(television.is_on())
        television.turn_off()
        self.assertFalse(television.is_on())

    def test_that_tv_can_increase_volume(self):
        television = Television()
        self.assertFalse(television.is_on())
        television.turn_on()
        self.assertTrue(television.is_on())
        initial_volume = television.get_volume()
        expected = television.increase_volume()
        self.assertEqual(initial_volume + 1 , expected)

    def test_that_tv_can_decrease_volume(self):
        television = Television()
        self.assertFalse(television.is_on())
        television.turn_on()
        self.assertTrue(television.is_on())
        television.increase_volume()
        initial_volume = television.get_volume()
        expected = television.decrease_volume()
        self.assertEqual(initial_volume -1, expected)

    def test_that_tv_can_change_channel_forward(self):
        television = Television()
        self.assertFalse(television.is_on())
        television.turn_on()
        self.assertTrue(television.is_on())
        initial_channel = television.get_channel()
        expected = television.channel_up()
        self.assertEqual(initial_channel +1 , expected)

    def test_that_tv_can_change_channel_backward(self):
        television = Television()
        self.assertFalse(television.is_on())
        television.turn_on()
        self.assertTrue(television.is_on())
        television.channel_up()
        initial_channel = television.get_channel()
        expected = television.channel_down()
        self.assertEqual(initial_channel -1, expected)

    def test_that_tv_can_change_channel_to_specific_channel(self):
        television = Television()
        self.assertFalse(television.is_on())
        television.turn_on()
        self.assertTrue(television.is_on())
        television.set_channel(2)
        self.assertEqual(2, television.get_channel())

    def test_that_tv_volume_can_be_muted(self):
        television = Television()
        self.assertFalse(television.is_on())
        television.turn_on()
        self.assertTrue(television.is_on())
        television.mute()
        self.assertEqual(0, television.get_volume())

    def test_that_tv_volume_can_be_unMuted(self):
        television = Television()
        self.assertFalse(television.is_on())
        television.turn_on()
        self.assertTrue(television.is_on())
        television.increase_volume()
        self.assertEqual(1, television.get_volume())

        television.mute()
        self.assertEqual(0, television.get_volume())

        television.unmute()
        self.assertEqual(100, television.get_volume())

if __name__ == "__main__":
    unittest.main()

