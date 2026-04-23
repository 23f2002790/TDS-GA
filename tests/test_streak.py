import pytest
from streak import longest_positive_streak

def test_empty_list():
    """Test that an empty list returns a streak of 0."""
    assert longest_positive_streak([]) == 0

def test_single_streak():
    """Test a simple case with a single streak."""
    assert longest_positive_streak([1, 2, 3, 4]) == 4

def test_no_positive_numbers():
    """Test a list with no positive numbers."""
    assert longest_positive_streak([-1, -2, 0]) == 0

def test_multiple_streaks():
    """Test a list with multiple streaks of positive numbers."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7, 0, 4]) == 3

def test_streak_at_beginning():
    """Test a streak at the beginning of the list."""
    assert longest_positive_streak([5, 6, 7, 0, 4]) == 3

def test_streak_at_end():
    """Test a streak at the end of the list."""
    assert longest_positive_streak([2, 3, -1, 5, 6, 7]) == 3

def test_all_same_positive_numbers():
    """Test a list of identical positive numbers."""
    assert longest_positive_streak([1, 1, 1]) == 3

def test_with_zeros():
    """Test that zeros break the streak."""
    assert longest_positive_streak([1, 2, 0, 3, 4, 5]) == 3

def test_with_negatives():
    """Test that negative numbers break the streak."""
    assert longest_positive_streak([1, 2, -5, 3, 4]) == 2

def test_long_list():
    """Test with a longer list."""
    assert longest_positive_streak(list(range(-10, 10))) == 9