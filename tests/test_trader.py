import pytest

from src.simulator.trader import Trader


def test_trader_is_abstract():

    with pytest.raises(TypeError):
        Trader(trader_id=1)