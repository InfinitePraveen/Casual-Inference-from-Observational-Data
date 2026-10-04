from django.shortcuts import render

def home(request):
    context = {
        "title": "Causal Inference from Observational Data",
        "question": "What is the estimated effect of job-training participation on post-treatment earnings?",
        "dataset": "Lalonde job-training observational dataset",
        "methods": [
            "Propensity-score estimation",
            "Inverse Probability Weighting (IPW)",
            "DoWhy backdoor identification",
            "DoWhy causal effect estimation",
            "Placebo/refutation testing",
        ],
        "assumptions": [
            "Observed pre-treatment confounders are measured adequately.",
            "There is sufficient treatment/control overlap.",
            "Treatment occurs before the measured outcome.",
            "No important unmeasured confounder remains.",
        ],
        "github": "https://github.com/InfinitePraveen",
        "linkedin": "https://www.linkedin.com/in/infinitepraveen/",
        "notebook": "https://github.com/InfinitePraveen/Causal-Inference-from-Observational-Data/blob/main/notebooks/causal_inference_observational_data.ipynb",
    }
    return render(request, "index.html", context)
