import os
from src.config import load_config, require_env
from src.exception import MissingConfigError

TEST_SETTING = "REPAIRDESK_TEST_SETTING"
def test_missing_setting() -> None:
    os.environ.pop(TEST_SETTING, None)
    result = "WRONG"
    # print("require func result : ",require_env(TEST_SETTING))
    try:
        require_env(TEST_SETTING)
    except MissingConfigError:
        result = "OK"
    print(f"case 1 (missing setting) -> {result}")
def test_empty_setting() -> None:
    os.environ[TEST_SETTING] = ""
    result = "WRONG"
    try:
        require_env(TEST_SETTING)
    except MissingConfigError:
        result = "OK"
    print(f"case 2 (empty setting) -> {result}")
def test_config_loads() -> None:
    os.environ["OPENAI_API_KEY"] = "sk-test-123"
    os.environ["MODEL"] = "test-model"

    config = load_config()
    result = "OK"
    if config.openai_api_key != "sk-test-123":
        result = "WRONG"
    print(f"case 3 (config loads) -> {result}")
if __name__ == "__main__":
    test_missing_setting()
    test_empty_setting()
    test_config_loads()