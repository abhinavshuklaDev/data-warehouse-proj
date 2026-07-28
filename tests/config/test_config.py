from src.config.config import config


def test_customer_count():
    assert config.config.master_data.customers > 0


def test_bucket():
    assert config.config.aws.bucket != ""


def test_region():
    assert config.config.aws.region == "ap-southeast-2"