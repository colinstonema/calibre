#!/usr/bin/env python2
# vim:fileencoding=utf-8
# License: GPLv3 Copyright: 2019, Kovid Goyal <kovid at kovidgoyal.net>

from __future__ import absolute_import, division, print_function, unicode_literals

import json
from base64 import standard_b64encode


class WebStoreDialog(object):

    def __init__(self, gui, base_url, parent=None, detail_url=None, create_browser=None):
        self.gui = gui
        self.base_url = base_url
        self.detail_url = detail_url
        self.create_browser = create_browser
        self.window_title = None
        self.tags = None

    def setWindowTitle(self, title):
        self.window_title = title

    def set_tags(self, tags):
        self.tags = tags

    def exec_(self):
        data = {'base_url': self.base_url, 'detail_url': self.detail_url, 'window_title': self.window_title, 'tags': self.tags}
        data = json.dumps(data)
        if not isinstance(data, bytes):
            data = data.encode('utf-8')
        data = standard_b64encode(data)
        if isinstance(data, bytes):
            data = data.decode('ascii')
        args = ['store-dialog', data]
        self.gui.job_manager.launch_gui_app(args[0], kwargs={'args':args})
