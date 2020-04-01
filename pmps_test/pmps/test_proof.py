import logging

logger = logging.getLogger(__name__)


def test_True():
    assert True


def test_False():
    assert False


def test_args(cmdopt):
    """
    Example test using an argument passed at test runtime.
    """
    print(cmdopt)
    assert False
    # assert ams_net_id == "127.0.0.1.1.1"
