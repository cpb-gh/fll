# fll
This repository contains functions for use with Lego Spike Prime robots.

## Combining functions
There is a Github Action configured [here](https://github.com/cpb-gh/fll/blob/main/.github/workflows/update-functions.yaml)
which runs any time a file in the `functions` or `github` directories is updated.
The Action checks out the repo, executes the [merge-in-functions.sh](https://github.com/cpb-gh/fll/blob/main/github/merge-in-functions.sh) script,
and then commits any changes that the execution made to the [combined_functions.py](https://github.com/cpb-gh/fll/blob/main/combined_functions.py) combined file.

The [merge-in-functions.sh](https://github.com/cpb-gh/fll/blob/main/github/merge-in-functions.sh) script adds the standard Spike Prime imports to the [combined file](https://github.com/cpb-gh/fll/blob/main/combined_functions.py)
and then concatenates every file found in the `functions` directory into that file.
To allow for execution/testing of individual scripts in the `functions` directory, the `merge-in-functions.sh` script only splices in the section of the file between the strings `FUNCTION START` and `FUNCTION END`.
See the [test function](https://github.com/cpb-gh/fll/blob/main/functions/test_function.py) file as an example of a function getting spliced into the [combined file](https://github.com/cpb-gh/fll/blob/main/combined_functions.py).
Note that it has its own imports to allow it to be run independently by pasting into the Spike Prime IDE, but those imports are not spliced into the combined file because they are not between the `FUNCTION START` and `FUNCTION END` markers.
