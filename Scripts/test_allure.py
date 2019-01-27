import allure
import pytest

class Test_01:

    @pytest.allure.severity(pytest.allure.severity_level.CRITICAL)
    @allure.step(title="第一个步骤")
    def test_001(self):
        allure.attach("wenjianm1","我是步骤1的描述信息")
        assert True

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="第2个步骤")
    def test_002(self):
        allure.attach("wenjianm2", "我是步骤2的描述信息")
        assert True