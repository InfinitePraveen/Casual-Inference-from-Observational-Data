# Data

The notebook downloads the small Lalonde observational job-training dataset at runtime.

Source:
https://raw.githubusercontent.com/py-why/dowhy/main/dowhy/datasets/causal_inference_data.csv

The CSV is intentionally not committed to the repository so the project remains small. The notebook uses `requests` and `pathlib` to download it only when needed.
