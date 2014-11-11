import os

print('OLD PATH = ' + os.environ['PATH'])

HOME = os.path.expanduser("~")
paths = [ HOME + "/.rbenv/shims", HOME + "/.ndenv/shims", "/usr/local/bin" ]
path_string = ":".join(paths)
if os.environ['PATH'].find(path_string) == -1:
    os.environ['PATH'] = path_string + ":" + os.environ['PATH']

print('NEW PATH = ' + os.environ['PATH'])