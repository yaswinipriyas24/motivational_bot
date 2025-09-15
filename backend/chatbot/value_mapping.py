def get_values_for_problem(problem_key, values_data=None):
    mapping = {
        "stress": ["empathy", "well_being", "compassion"],
        "confidence": ["trust", "discipline", "empathy"],
        "time_management": ["discipline", "responsibility"],
        "general": ["empathy", "well_being"]
    }
    return mapping.get(problem_key, ["empathy"])
