import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -5, 0, -2]) == 0

def test_all_positive_numbers():
    """Test a list with all positive numbers."""
    assert longest_positive_streak([1, 2, 3, 4, 5]) == 5

def test_single_streak():
    """Test a single streak of positive numbers."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_multiple_streaks_longest_first():
    """Test multiple streaks where the longest streak is first."""
    assert longest_positive_streak([5, 6, 7, 0, 1, 2]) == 3

def test_multiple_streaks_longest_last():
    """Test multiple streaks where the longest streak is last."""
    assert longest_positive_streak([1, 2, 0, 5, 6, 7, 8]) == 4

def test_streak_with_zeros():
    """Test that zeros correctly break a streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 0, 5]) == 2

def test_streak_with_negatives():
    """Test that negative numbers correctly break a streak."""
    assert longest_positive_streak([1, 2, -5, 3, 4, -1, 5]) == 2

def test_single_element_list():
    """Test lists with a single element."""
    assert longest_positive_streak([5]) == 1
    assert longest_positive_streak([-5]) == 0
    assert longest_positive_streak([0]) == 0

def test_long_list():
    """Test with a longer list and multiple streaks."""
    assert longest_positive_streak([1, 0, 2, 2, 0, 3, 3, 3, 0, 4, 4, 4, 4, 0]) == 4
    assert longest_positive_streak([1, 1, 1, 1, 1, -10, 2, 2, 2, 2, -20, 3, 3, 3, -30, 4, 4, -40, 5]) == 5