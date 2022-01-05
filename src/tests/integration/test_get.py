
def test_empty_db(app_init):
    """Test case one."""
    test_case_one = app_init.get('/get/correlation')
    assert test_case_one != 500