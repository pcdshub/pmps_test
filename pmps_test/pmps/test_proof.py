import logging

logger = logging.getLogger(__name__)


def test_True():
    assert True


def test_False():
    assert False


def test_passed_args(cmdopt):
    """
    Example test using an argument passed programatically
    """
    print(cmdopt)
    assert cmdopt == 100


def test_commandline_args(ams_net_id):
    """
    Example test using an argument passed at runtime
    """
    print(ams_net_id)
    assert ams_net_id == "127.0.0.1.1.1"
