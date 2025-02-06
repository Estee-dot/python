class Television:
    pass

    def __init__(self):
        self._is_on = False
        self.channel = 1
        self.volume = 0
        self.max_volume = 100
        self.min_volume = 0

    def is_on(self):
        return self._is_on

    def turn_on(self):
        self._is_on = True
        return self.is_on

    def turn_off(self):
        self._is_on = False
        return not self.is_on

    def is_tv_on(self):
        return self._is_on

    def increase_volume(self):
        if self.volume < self.max_volume:
            self.volume += 1
            return self.volume

    def decrease_volume(self):
        if self.volume > self.min_volume:
            self.volume -= 1
            return self.volume

    def set_channel(self, channel):
        self.channel = channel

    def get_channel(self):
        return self.channel

    def channel_up(self):
        self.channel += 1
        return self.channel

    def channel_down(self):
        self.channel -= 1
        return self.channel

    def mute(self):
        self.volume = 0
        return self.volume

    def unmute(self):
        self.volume = 100
        return self.volume

    def get_volume(self):
        return self.volume


# def __str__(self):

