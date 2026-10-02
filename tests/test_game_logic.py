from logic_utils import check_guess, parse_guess, update_score, get_range_for_difficulty


def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    # If secret is 50 and guess is 60, outcome is "Too High" and hint says go lower
    outcome, message = check_guess(60, 50)
    assert outcome == "Too High"
    assert "LOWER" in message


def test_guess_too_low():
    # If secret is 50 and guess is 40, outcome is "Too Low" and hint says go higher
    outcome, message = check_guess(40, 50)
    assert outcome == "Too Low"
    assert "HIGHER" in message


def test_numeric_comparison_not_text():
    # 9 is lower than 10 (as text "9" > "10", which was the bug)
    outcome, _ = check_guess(9, 10)
    assert outcome == "Too Low"


def test_parse_guess_valid():
    assert parse_guess("42") == (True, 42, None)


def test_parse_guess_rejects_bad_input():
    for raw in ["", "   ", None, "abc", "3.7", "-5", "0", "101"]:
        ok, value, err = parse_guess(raw)
        assert not ok and value is None and err


def test_hard_range_is_bigger_than_normal():
    assert get_range_for_difficulty("Hard")[1] > get_range_for_difficulty("Normal")[1]


def test_score_win_first_attempt():
    assert update_score(0, "Win", 1) == 90


def test_score_wrong_guess_always_loses_points():
    for attempt in (1, 2, 3, 4):
        assert update_score(0, "Too High", attempt) == -5
        assert update_score(0, "Too Low", attempt) == -5


# --- extra tests ---

def test_check_guess_boundaries():
    assert check_guess(1, 1)[0] == "Win"
    assert check_guess(100, 100)[0] == "Win"
    assert check_guess(1, 2)[0] == "Too Low"
    assert check_guess(100, 99)[0] == "Too High"


def test_check_guess_never_mixes_up_digits():
    # text comparison would get these wrong ("9" > "10", "100" < "20")
    assert check_guess(100, 20)[0] == "Too High"
    assert check_guess(2, 10)[0] == "Too Low"


def test_parse_guess_strips_whitespace():
    assert parse_guess("  7  ") == (True, 7, None)


def test_parse_guess_range_edges():
    assert parse_guess("1", 1, 20)[0] is True
    assert parse_guess("20", 1, 20)[0] is True
    assert parse_guess("0", 1, 20)[0] is False
    assert parse_guess("21", 1, 20)[0] is False


def test_parse_guess_error_messages():
    assert parse_guess("")[2] == "Enter a guess."
    assert parse_guess("abc")[2] == "That is not a whole number."
    assert "between 1 and 100" in parse_guess("500")[2]


def test_parse_guess_rejects_decimals_and_symbols():
    for raw in ["3.0", "1e2", "5 5", "#3", "one"]:
        assert parse_guess(raw)[0] is False


def test_difficulty_ranges():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 200)
    assert get_range_for_difficulty("Unknown") == (1, 100)


def test_score_win_decreases_with_attempts():
    assert update_score(0, "Win", 1) > update_score(0, "Win", 5)


def test_score_win_has_minimum_of_10():
    assert update_score(0, "Win", 20) == 10


def test_score_adds_to_current_score():
    assert update_score(50, "Win", 2) == 130
    assert update_score(50, "Too Low", 2) == 45


def test_score_unknown_outcome_unchanged():
    assert update_score(30, "Something", 1) == 30
