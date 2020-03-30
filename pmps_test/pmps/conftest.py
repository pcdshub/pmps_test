import pytest

AMS_NET_ID_OPTION = "--ams_net_id"


def pytest_addoption(parser):
    parser.addoption(
        AMS_NET_ID_OPTION, action="store", default=True, help="pytest argument"
    )

@pytest.fixture
def ams_net_id(request):
    return request.config.getoption(AMS_NET_ID_OPTION)
