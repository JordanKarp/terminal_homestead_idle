from src.classes.settings import Settings


def test_to_from_roundtrip():
    s = Settings(show_all=False, achievements=["a"], autosave=True, autosave_interval=7)
    d = s.to_dict()
    s2 = Settings.from_dict(d)
    assert s2.show_all is False
    assert s2.autosave is True
    assert s2.autosave_interval == 7
    assert s2.achievements == ["a"]


def test_from_dict_with_none_returns_defaults():
    s = Settings.from_dict(None)
    assert isinstance(s, Settings)
    assert s.show_all is True
    assert s.autosave is False


def test_from_dict_with_string_booleans_and_numeric_strings():
    data = {"show_all": "false", "autosave": "True", "autosave_interval": "20", "achievements": ["x", 2]}
    s = Settings.from_dict(data)
    assert s.show_all is False
    assert s.autosave is True
    assert s.autosave_interval == 20
    # non-string achievement should be coerced to string
    assert s.achievements == ["x", "2"]


def test_from_dict_invalid_interval_keeps_default():
    s = Settings.from_dict({"autosave_interval": "not-a-number"})
    assert s.autosave_interval == 10
