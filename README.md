# Automated Data Pipelines with Prefect

Dataharvest 2026


## Setup

Follow these instructions to clone the project, install the `uv` package manager, and set up the local development environment.

### 1. Clone the Project
Open your terminal and run the following commands to download the repository and navigate into the project directory:

```bash
# Clone the repository
git clone  https://github.com/Tilana/dataharvest2026_automated_pipelines

# Move into the project directory
cd dataharvest2026_automated_pipelines 
```

---

## 2. Install uv (if you haven't already)

[`uv`](https://docs.astral.sh/uv/getting-started/installation/#installation-methods) is an ultra-fast Python package and project manager. Install it using the official command for your operating system:

### macOS & Linux
Run the standalone installer script via `curl`:
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*Alternative with Homebrew:* `brew install uv`


## 3. Install Dependencies

Run `uv sync` in the root of the project directory to install all dependencies from the `pyproject.toml`

Run `uv run prefect --version` to check if the installation was successful.




## Automated Pipelines with Prefect

### Prefect Dashboard


Run the following command to spin up the Prefect dashboard:

```
uv run prefect server start
```

Open localhost:4200 in your browser.


### Run a script

```
uv run python script.py
```






