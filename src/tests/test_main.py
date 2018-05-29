from ..main import get_total_budget_value

def test_get_total_budget_value():
    result = get_total_budget_value("tests/sample_data_fully_valid_10_rows.csv", 2018)
    assert result == float(500)
