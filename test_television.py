# Caelan Charleston & Evan Rathke
import pytest
from television import *

class TestTelevisionFunctions:
    def test_init(self):
        tv = Television()
        # Status, Channel, Volume
        assert tv.__str__() == f'Power = False, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'

    def test_power(self):
        tv = Television()
        # Power On
        tv.power()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'
        # Power Off
        tv.power()
        assert tv.__str__() == f'Power = False, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'

    def test_mute(self):
        tv = Television()
        # TV On, Volume Increased, Muted
        tv.power()
        tv.volume_up()
        tv.mute()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'
        # TV On, Unmuted
        tv.mute()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = 1'
        # TV Off, Muted
        tv.power()
        tv.mute()
        assert tv.__str__() == f'Power = False, Channel = {tv.MIN_CHANNEL}, Volume = 1'
        # TV Off, Unmuted
        tv.mute()
        assert tv.__str__() == f'Power = False, Channel = {tv.MIN_CHANNEL}, Volume = 1'

    def test_channel_up(self):
        tv = Television()
        # TV Off, Channel Increased
        tv.channel_up()
        assert tv.__str__() == f'Power = False, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'
        # TV On, Channel Increased
        tv.power()
        tv.channel_up()
        assert tv.__str__() == f'Power = True, Channel = 1, Volume = {tv.MIN_VOLUME}'
        # TV On, Channel Increased past Max
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'

    def test_channel_down(self):
        tv = Television()
        # TV Off, Channel Decreased
        tv.channel_down()
        assert tv.__str__() == f'Power = False, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'
        # TV On, Channel Decreased past Min
        tv.power()
        tv.channel_down()
        assert tv.__str__() == f'Power = True, Channel = 3, Volume = {tv.MIN_VOLUME}'

    def test_volume_up(self):
        tv = Television()
        # TV Off, Volume Increased
        tv.volume_up()
        assert tv.__str__() == f'Power = False, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'
        # TV On, Volume Increased
        tv.power()
        tv.volume_up()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = 1'
        # TV On, Muted, Volume Increased
        tv.mute()
        tv.volume_up()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = 2'
        # TV On, Volume Increased past Max
        tv.volume_up()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = 2'

    def test_volume_down(self):
        tv = Television()
        # TV Off, Volume Decreased
        tv.volume_down()
        assert tv.__str__() == f'Power = False, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'
        # TV On, Volume Decreased
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.volume_down()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = 1'
        # TV On, Muted, Volume Decreased
        tv.mute()
        tv.volume_down()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'
        # TV On, Volume Decreased past Min
        tv.volume_down()
        assert tv.__str__() == f'Power = True, Channel = {tv.MIN_CHANNEL}, Volume = {tv.MIN_VOLUME}'