#Eye-track
Project Eye-Track has a couple of goals:
1. use eye-tracking to validate learner experiences of learning context
2. Explore how eyetracking can be ised with other informational analytics to perform intervention or achieve predictive/adaptive learning

There are two pieces to this project

## Web interface
Available at [https://eye-track.hugodf.xyz](https://eye-track.hugodf.xyz).

Features:
- uses the webgazer.js Library to monitor the eye and cursor movement of the user
- use heatmap.js to overlay this information onto the screen

##Analysis scripts
`analyse.py` and `data.json` (respectively analysis script and sample data) allow us to further our understanding of the eye-tracking data.

You need to have `numpy` and `matplotlib` installed.

Run: `python analyse.py`
