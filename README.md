# fll
This repository contains functions for use with the Prorito team's Lego Spike Prime robot.
## Default port configuration
These ports are the ones that default in each function - you can always pass different ones as arguments but you won't have to if you use these mappings:

| Port  | Connected To              |
| ----- | ------------------        |
| A     | Left wheel          purple|
| B     | Right wheel          green|
| C     | Right color sensor  orange|
| D     | Left color sensor    brown|
| E     | Back attachment      white|
| F     | Front attachment      blue|

## Working on the competition runs
The `functions` directory now contains a file named `run_1.py` which holds the `zz_run_one()` function (we prepend `zz` so that it ends up at the bottom of the combined_functions file for easier editing).  This function gets called by the `start_run()` function when the color sensors detect a red color.  `start_run()` automatically gets called from the [combined functions file](https://github.com/cpb-gh/fll/blob/main/combined_functions.py), so if you just copy that file into your Spike IDE you should be able to start coding inside `zz_run_one()` right away.
We'll add `zz_run_two()` and a color for it as well as we start coding that run.

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
