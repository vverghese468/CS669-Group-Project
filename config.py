# ============================================================
# config.py  —  Central configuration for the sepsis RL pipeline
#
# Running in Google Colab — no credential files needed.
# Authentication is handled by google.colab.auth (browser popup).
#
# *** The only value you must change before running: ***
#     GCP_PROJECT_ID  (line 14)
# ============================================================

# ----------------------------------------------------------------
# GCP / BigQuery
# ----------------------------------------------------------------
GCP_PROJECT_ID = "silken-physics-467815-g5"   # ← CHANGE THIS
MIMIC_DATASET  = "physionet-data.mimiciii_clinical"

# No key files or OAuth JSON needed — Colab authenticates as
# your logged-in Google account via a one-time browser popup.

# ----------------------------------------------------------------
# Drive folder layout
# All paths are relative to your Drive root ("My Drive")
# ----------------------------------------------------------------
DRIVE_BASE_FOLDER   = "sepsis_rl"          # top-level folder
DRIVE_RAW_FOLDER    = "raw"                # raw BigQuery extracts
DRIVE_PROC_FOLDER   = "processed"          # windowed / feature-engineered data
DRIVE_OUTPUT_FOLDER = "outputs"            # model artifacts + metrics

# ----------------------------------------------------------------
# Pipeline parameters
# ----------------------------------------------------------------
WINDOW_HOURS      = 4          # length of each time window
MAX_WINDOWS       = 20         # max windows per stay  (= 80 hours)
N_FLUID_BINS      = 5          # discrete fluid action levels  (0–4)
N_VASO_BINS       = 5          # discrete vasopressor levels   (0–4)
TERMINAL_REWARD   = 15.0       # ±15 reward at end of episode
SOFA_PENALTY      = 0.5        # weight on SOFA-change shaping reward
MORTALITY_HORIZON = 90         # days for primary outcome (90-day mortality)

# ----------------------------------------------------------------
# File names written to Drive
# ----------------------------------------------------------------
RAW_COHORT_FILE   = "cohort.parquet"
RAW_FEATURES_FILE = "features.parquet"
RAW_ACTIONS_FILE  = "actions_raw.parquet"
RAW_MORTALITY_FILE= "mortality.parquet"

PROC_STATES_FILE  = "states.parquet"
PROC_ACTIONS_FILE = "actions_binned.parquet"
PROC_DATASET_FILE = "sepsis_rl_dataset.parquet"

OUTPUT_MODEL_FILE   = "model.pt"
OUTPUT_METRICS_FILE = "metrics.json"
OUTPUT_PLOTS_DIR    = "plots"