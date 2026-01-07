from datetime import datetime

from src.classes.message_log import MessageLog


def test_message_log_show_most_recent_and_show_log():
    ml = MessageLog()
    now = datetime(2026, 1, 7, 10, 0)
    ml.add_message("First", now, 10)
    ml.add_message("Second", now, 5)

    recent = ml.show_most_recent
    assert isinstance(recent, str)
    assert "Second" in recent

    log = ml.show_log()
    assert isinstance(log, str)
    assert "First" in log and "Second" in log


def test_add_message_merges_consecutive_same_text():
    ml = MessageLog()
    now = datetime(2026, 1, 7, 10, 0)
    ml.add_message("Repeat", now, 10)
    ml.add_message("Repeat", now, 5)
    assert len(ml.messages) == 1
    assert ml.messages[0].duration == 15