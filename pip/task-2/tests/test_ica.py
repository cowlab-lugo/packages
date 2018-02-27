# tests for promo code views
import pytest
from iscowalive import check


@pytest.mark.parametrize("url, expected", [
    ('https://www.google.com', True),
    ('https://www.google.com/404', False),
    ('not-url', False),
    (100, False),
])
def test_check(url, expected):
    res = check(url)
    assert res is expected
