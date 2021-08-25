import pytest
from main import valid_email, log


class TestEmail:
    @pytest.mark.parametrize('email, test_result', [
        # Valid email:
        pytest.param('test@test.ru', True),
        pytest.param('w@w.com', True),
        pytest.param('123QWE@mmm.mmm', True),
        pytest.param('john.doe@gmail.com', True),
        # Invalid email:
        pytest.param('test@test.', False),
        pytest.param('w@', False),
        pytest.param('@tt', False),
        pytest.param('john.doe@gmail,com', False)
    ])
    def test_valid_email(self, email, log_file, test_result):
        result = valid_email(email)
        assert result == test_result
        log(log_file, f"{result} email: {email}\n")
