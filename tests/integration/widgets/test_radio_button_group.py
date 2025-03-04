#-----------------------------------------------------------------------------
# Copyright (c) 2012 - 2024, Anaconda, Inc. All rights reserved.
#
# Powered by the Bokeh Development Team.
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

# Bokeh imports
from bokeh.layouts import column
from bokeh.models import (
    ColumnDataSource,
    CustomJS,
    Plot,
    RadioButtonGroup,
    Range1d,
    Scatter,
)
from tests.support.plugins.project import BokehModelPage, BokehServerPage
from tests.support.util.selenium import RECORD, find_element_for

#-----------------------------------------------------------------------------
# Tests
#-----------------------------------------------------------------------------

pytest_plugins = (
    "tests.support.plugins.project",
)

LABELS = ["Option 1", "Option 2", "Option 3"]


@pytest.mark.selenium
class Test_RadioButtonGroup:
    def test_server_on_change_round_trip(self, bokeh_server_page: BokehServerPage) -> None:
        group = RadioButtonGroup(labels=LABELS)
        def modify_doc(doc):
            source = ColumnDataSource(dict(x=[1, 2], y=[1, 1], val=["a", "b"]))
            plot = Plot(height=400, width=400, x_range=Range1d(0, 1), y_range=Range1d(0, 1), min_border=0)
            plot.add_glyph(source, Scatter(x='x', y='y', size=20))
            plot.tags.append(CustomJS(name="custom-action", args=dict(s=source), code=RECORD("data", "s.data")))
            def cb(event):
                source.data['val'] = [group.active, "b"]
            group.on_event('button_click', cb)
            doc.add_root(column(group, plot))

        page = bokeh_server_page(modify_doc)

        el = find_element_for(page.driver, group, ".bk-btn:nth-child(3)")
        el.click()

        page.eval_custom_action()

        results = page.results
        assert results['data']['val'] == [2, "b"]

        el = find_element_for(page.driver, group, ".bk-btn:nth-child(1)")
        el.click()

        page.eval_custom_action()

        results = page.results
        assert results['data']['val'] == [0, "b"]

        assert page.has_no_console_errors()

    def test_js_on_change_executes(self, bokeh_model_page: BokehModelPage) -> None:
        group = RadioButtonGroup(labels=LABELS)
        group.js_on_event('button_click', CustomJS(code=RECORD("active", "cb_obj.origin.active")))

        page = bokeh_model_page(group)

        el = find_element_for(page.driver, group, ".bk-btn:nth-child(3)")
        el.click()

        results = page.results
        assert results['active'] == 2

        el = find_element_for(page.driver, group, ".bk-btn:nth-child(1)")
        el.click()

        results = page.results
        assert results['active'] == 0

        assert page.has_no_console_errors()
