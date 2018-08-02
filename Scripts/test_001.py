import allure,pytest

class Test_001():

    @allure.step(title = "login")
    @pytest.allure.severity(pytest.allure.severity_level.MINOR)
    def test_001(self):
        allure.attach("function","daom")

        assert 1

    @allure.step(title="buy")
    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    def test_002(self):
        allure.attach("function","logout")
        assert 0