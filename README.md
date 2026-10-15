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