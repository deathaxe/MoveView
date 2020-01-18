from os.path import basename

import sublime_plugin

__all__ = ["MoveToNeighboringIndexCommand", "MoveToIndexCommand"]


def active_view_group_index(window):
    view = window.active_view()
    group, index = window.get_view_index(view)
    return view, group, index


class MoveToNeighboringIndexCommand(sublime_plugin.WindowCommand):
    def is_enabled(self, forward=True):
        return len(self.window.views_in_group(self.window.active_group())) > 1

    def run(self, forward=True):
        view, view_group, view_index = active_view_group_index(self.window)
        num_views = len(self.window.views_in_group(view_group))
        if num_views > 1:
            if forward:
                index = (view_index + 1) % num_views
            else:
                index = (view_index - 1) % num_views
            if index != view_index:
                self.window.set_view_index(view, view_group, index)
                self.window.focus_view(view)


class MoveToIndexCommand(sublime_plugin.WindowCommand):
    def is_enabled(self, index=None):
        if index is None:
            return True
        _, view_group, view_index = active_view_group_index(self.window)
        if view_index in (-1, index):
            return False
        num_views = len(self.window.views_in_group(view_group))
        return num_views > 1 and index < num_views

    def input(self, args):
        if args.get("index") is None:
            return IndexInputHandler(self.window)
        return None

    def input_description(self):
        return "Move View:"

    def run(self, index):
        view, view_group, view_index = active_view_group_index(self.window)
        num_views = len(self.window.views_in_group(view_group))
        if num_views > 1:
            if index < 0:
                index = num_views + index
            index = max(0, min(index, num_views - 1))
            if index != view_index:
                self.window.set_view_index(view, view_group, index)
                self.window.focus_view(view)


class IndexInputHandler(sublime_plugin.ListInputHandler):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def list_items(self):
        view, view_group, view_index = active_view_group_index(self.window)
        views = self.window.views_in_group(view_group)
        views.pop(view_index)

        if view_index > 0:
            items = [("First Position\tto position 1", 0)]
        else:
            items = []

        for i, v in enumerate(views, start=1):
            if i == view_index:
                continue
            try:
                title = basename(v.file_name())
            except TypeError:
                title = v.name() or "untitled"
            items.append(("{}\tto position {}".format(title, i + 1), i))

        return items
