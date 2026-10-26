# Setup

## 1. Navigate to a directory

Open a terminal and navigate to the directory where you want to store the repository:

```bash
cd /path/to/your/directory
```

## 2. Clone the repository

```bash
git clone https://github.com/danielsehr/GEO6.git
cd geo6
```

## 3. Install dependencies

Make sure [uv](https://docs.astral.sh/uv/) is installed, then run:

```bash
uv sync
```

This creates a virtual environment (if needed) and installs the project dependencies specified in `pyproject.toml` and `uv.lock`.


## 4. Run the submission
Go to src/geo6/main.ipynb and run the script!   




H1 — Differences in microbial respiration
Microbial respiration differs between the rhizosphere soils associated with the three plant species and bulk soil.

Prediction: At least some soil groups differ in basal respiration or substrate-induced respiration.

We should not assume in advance that invasive plants necessarily produce higher respiration rates.


H2 — Differences in substrate-use profiles
The soil groups differ in their respiration responses to individual substrates.

Prediction: The profiles of substrate-induced respiration differ between soil groups, indicating differences in their functional responses to the supplied substrates.

This hypothesis concerns the pattern of microbial responses, not simply their overall magnitude.


H3 — Relationships with soil properties
Variation in microbial respiration is associated with measured soil physicochemical properties.

Prediction: At least some soil properties explain variation in respiration beyond the differences captured by soil-group identity alone.

We should only retain this hypothesis if the available sample size and number of independent samples support the required analysis.


1	Data validation and replicate handling	Ensure valid statistical inference
2	Basal respiration comparison	Test H1
3	Substrate response profiles and PCA	Investigate H2
4	Focused soil-property correlations	Investigate H3
5	Regression, if justified	Assess whether soil properties explain additional variation