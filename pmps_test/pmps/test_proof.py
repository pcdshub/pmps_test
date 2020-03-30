import logging

import pytest

logger = logging.getLogger(__name__)

def test_True():
    assert True

def test_False():
    assert False

def test_args(ams_net_id):
    assert ams_net_id == False 
