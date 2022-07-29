from bmi import user_input
import pytest


def test_user_input_one(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 160)
    assert user_input() == 0, f'0 is not valid'


def test_user_input_two(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 160)
    assert user_input() == 3+6j, f'complex number is not valid'


def test_user_input_three(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 160)
    assert user_input() == 'm', f'string is not valid'
