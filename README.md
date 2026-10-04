# Causal Inference from Observational Data

Estimate treatment effects from non-experimental data using propensity scores, DoWhy, and a simple causal machine-learning workflow.

## Project Overview

This project demonstrates how to estimate the causal effect of a treatment when randomized experiments are not available. It uses the **Lalonde job-training dataset**, a classic observational dataset containing treated and untreated individuals and their post-treatment earnings.

The workflow is intentionally lightweight and notebook-first:

1. Load a small open dataset.
2. Explore treatment and outcome distributions.
3. Estimate propensity scores.
4. Estimate the Average Treatment Effect (ATE) with DoWhy.
5. Check the estimate with a simple propensity-score weighting approach.
6. Run basic robustness/refutation checks.
7. Explain the result through a small Django web application.

## Dataset

**Lalonde job-training dataset**  
Source: `https://raw.githubusercontent.com/py-why/dowhy/main/dowhy/datasets/causal_inference_data.csv`

The dataset is small enough for CPU-only experimentation and does not require a GPU or large model downloads.

## Repository Structure

```text
Causal-Inference-from-Observational-Data/
├── notebooks/
│   └── causal_inference_observational_data.ipynb
├── data/
│   └── README.md
├── webapp/
│   ├── manage.py
│   ├── causal_demo/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── asgi.py
│   │   └── wsgi.py
│   ├── demo/
│   │   ├── __init__.py
│   │   ├── apps.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates/
│   │   └── index.html
│   └── static/
│       └── style.css
├── CONTRIBUTING.md
├── CONTRIBUTE.md
├── CHANGELOG.md
├── requirements.txt
└── .gitignore
```

## Running the Notebook

Python 3.10+ is recommended.

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Then start Jupyter:

```bash
jupyter notebook
```

Open:

```text
notebooks/causal_inference_observational_data.ipynb
```

The notebook downloads the small CSV directly with `requests` and stores it under `data/`.

## Running the Django Demo

From the repository root:

```bash
cd webapp
python manage.py migrate
python manage.py runserver
```

Open the local address shown by Django, normally:

```text
http://127.0.0.1:8000/
```

The web application provides an interview-friendly explanation of:

- the causal question,
- treatment and outcome,
- propensity-score intuition,
- the causal graph,
- estimated treatment effect,
- limitations and assumptions.

It also links to the notebook and the project's GitHub/LinkedIn profiles.

## Causal Question

> What is the estimated causal effect of participating in job training on post-treatment earnings, after accounting for observed pre-treatment characteristics?

### Important limitation

This is observational data, so causal interpretation depends on assumptions such as:

- no important unmeasured confounding,
- adequate overlap/positivity,
- correctly specified or sufficiently robust estimation,
- treatment occurring before the outcome.

The project intentionally presents these assumptions instead of treating an estimated association as automatically causal.

## Skills Demonstrated

- Causal inference
- Directed acyclic graphs (DAGs)
- Propensity scoring
- Inverse probability weighting
- DoWhy
- Causal effect identification
- Refutation/robustness checks
- Python
- Jupyter
- Django

## Author

**Praveen Kumar**

- GitHub: https://github.com/InfinitePraveen
- LinkedIn: https://www.linkedin.com/in/infinitepraveen/
