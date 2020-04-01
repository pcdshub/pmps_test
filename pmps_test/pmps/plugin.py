import pytest

AMS_NET_ID_OPTION = "--ams_net_id"


def pytest_load_initial_conftests(args, early_config, parser):
    pass


def pytest_addoption(parser):
    """
    This is a built-in pytest hook. Don't rename this function

    This function allows os to pass options directly to pytest when run.
    """
    parser.addoption(
        AMS_NET_ID_OPTION, action="store", default=False,
        help="pytest argument"
    )
    parser.addoption(
        "--cmdopt", action="store", default="type1",
        help="my option: type1 or type2"
    )


def pytest_configure(config):
    pass


@pytest.fixture
def ams_net_id(request):
    return request.config.getoption(AMS_NET_ID_OPTION)


@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")
