# tools

A small collection of scripts that I have found convenient in my daily life.

## `show_path.py`

A simple Python script that shows the entries in a path line by line.  If run without arguments, it will analyze the `PATH` environment variable.  Otherwise, it will use the given path (e.g. `PYTHONPATH`).  The first column of the output may display additional information:

- `X`: the entry refers to a non-existing directory.
- `+`: duplicate entry (it has appeared previously).

If you like colorized output then make sure that you have installed [`colorama`](https://pypi.org/project/colorama/).

For convenience, there is also a Windows batch file that runs the Python script.  Note that `show_path.bat` assumes that you have set an environment variable named `MY_TOOLS_DIR` which should point to the directory containing `show_path.py`.
