from twttr import shorten
import pytest


def test_shorten():
    assert shorten("Twitter") == "Twttr"
    assert shorten("Facebook") == "Fcbk"
    assert shorten("Tiktok") == "TkTk"
