from src.common.logger import logger


def test_logger():

    logger.info("Info message")

    logger.warning("Warning message")

    logger.error("Error message")

    logger.success("Success message")

    assert True