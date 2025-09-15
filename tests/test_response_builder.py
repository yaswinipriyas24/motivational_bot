from backend.chatbot.response_builder import build_response

def test_build_response():
    values_data = {
        "empathy": "I understand how you feel.",
        "compassion": "Be kind to yourself."
    }
    result = build_response("stress", ["empathy", "compassion"], values_data)
    expected = "I understand how you feel. Be kind to yourself."
    assert result == expected
