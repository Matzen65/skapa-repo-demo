
from veckouppgift_5.src.uppgift_2_1 import c_to_f
def test_c_to_f__low_returns_none():
    expected = None
    actual = c_to_f(-275)
    assert expected == actual