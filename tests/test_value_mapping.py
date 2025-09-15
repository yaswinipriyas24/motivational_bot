from backend.chatbot.value_mapping import get_values_for_problem

def test_value_mapping():
    assert get_values_for_problem("stress") == ["empathy", "well_being", "compassion"]
    assert get_values_for_problem("unknown") == ["empathy"]
