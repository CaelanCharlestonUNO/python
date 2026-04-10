# Caelan Charleston & Evan Rathke
class Television:
    """
    A class containing details and logic for a TV
    """
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3
    def __init__(self) -> None:
        """
        Method to initialize TV variables
        """
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL

    def power(self) -> None:
        """
        Method to turn the TV on and off
        """
        if self.__status:
            self.__status: bool = False
        else:
            self.__status: bool = True

    def mute(self) -> None:
        """
        Method to mute and unmute the TV
        """
        if self.__status:
            if self.__muted:
                self.__muted: bool = False
            else:
                self.__muted: bool = True

    def channel_up(self) -> None:
        """
        Method to raise the TV's channel by 1
        """
        if self.__status:
            if self.__channel == self.MAX_CHANNEL:
                self.__channel: int = self.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to lower the TV's channel by 1
        """
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel: int = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Method to raise the TV's volume by 1
        """
        if self.__status:
            if self.__muted:
                self.__muted: bool = False
            if self.__volume == self.MAX_VOLUME:
                self.__volume: int = self.MAX_VOLUME
            else:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to lower the TV's volume by 1
        """
        if self.__status:
            if self.__muted:
                self.__muted: bool = False
            if self.__volume == self.MIN_VOLUME:
                self.__volume: int = self.MIN_VOLUME
            else:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Method to display current details about the TV in the correct format
        :return: Current details/state of the TV
        """
        if self.__muted:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.MIN_VOLUME}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'