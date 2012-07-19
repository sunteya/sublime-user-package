# -*- coding: utf-8 -*-

from datetime import datetime
import sublime_plugin


class TimestampCommand(sublime_plugin.EventListener):
    """Expand `isoD`, `isoT`
"""
    def on_query_completions(self, view, prefix, locations):
        if prefix == 'isoD':
            val = datetime.now().strftime('%Y-%m-%d')
        elif prefix in ('isoT'):
            val = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        else:
            val = None

        return [(prefix, prefix, val)] if val else []
