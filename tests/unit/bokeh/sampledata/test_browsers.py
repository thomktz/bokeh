#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2024, Anaconda, Inc., and Bokeh Contributors.
# All rights reserved.
#
# The full license is in the file LICENSE.txt, distributed with this software.
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Boilerplate
#-----------------------------------------------------------------------------
from __future__ import annotations # isort:skip

import pytest ; pytest

#-----------------------------------------------------------------------------
# Imports
#-----------------------------------------------------------------------------

# External imports
import pandas as pd

# Bokeh imports
from tests.support.util.api import verify_all

# Module under test
#import bokeh.sampledata.browsers as bsb # isort:skip

#-----------------------------------------------------------------------------
# Setup
#-----------------------------------------------------------------------------

ALL = (
    'browsers_nov_2013',
    'icons',
)

#-----------------------------------------------------------------------------
# General API
#-----------------------------------------------------------------------------

Test___all__ = pytest.mark.sampledata(verify_all("bokeh.sampledata.browsers", ALL))

@pytest.mark.sampledata
def test_browsers_nov_2013() -> None:
    import bokeh.sampledata.browsers as bsb
    assert isinstance(bsb.browsers_nov_2013, pd.DataFrame)

    # check detail for package data
    assert len(bsb.browsers_nov_2013) == 118

@pytest.mark.sampledata
def test_icons() -> None:
    import bokeh.sampledata.browsers as bsb
    assert isinstance(bsb.icons, dict)

    # check detail for package data
    assert set(bsb.icons.keys()).issubset({"Chrome", "Firefox", "Safari", "Opera", "IE"})

#-----------------------------------------------------------------------------
# Dev API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Private API
#-----------------------------------------------------------------------------

#-----------------------------------------------------------------------------
# Code
#-----------------------------------------------------------------------------
