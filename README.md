# CS669-Group-Project
A repository of files from https://www.researchgate.net/publication/368230958_A_value-based_deep_reinforcement_learning_model_with_human_expertise_in_optimal_treatment_of_sepsis
# Sepsis RL Pipeline

A modular pipeline for extracting, processing, and modelling the MIMIC-III sepsis cohort from GCP BigQuery, with all inputs/outputs stored on Google Drive.

## File Structure

```
sepsis_rl_pipeline/
├── README.md
├── requirements.txt
├── config.py                  # Central config (project IDs, paths, constants)
│
├── 00_auth_drive.py           # Authenticate to Google Drive + mount helpers
├── 01_auth_gcp.py             # Authenticate to GCP / BigQuery
├── 02_extract_data.py         # Run BigQuery SQL queries → save raw data to Drive
├── 03_process_data.py         # Feature engineering, windowing, reward assignment
├── 04_model.py                # Train / evaluate RL model
└── 05_save_outputs.py         # Save final model artefacts and results to Drive
```

## Execution Order

Run the scripts in numbered order:

```bash
python 00_auth_drive.py        # one-time OAuth flow, saves token to Drive
python 01_auth_gcp.py          # validates GCP credentials / service account
python 02_extract_data.py      # pulls data from BigQuery → Drive (raw/)
python 03_process_data.py      # processes raw/ → processed/ on Drive
python 04_model.py             # trains model using processed data
python 05_save_outputs.py      # saves model + metrics → outputs/ on Drive
```

## Prerequisites

```bash
pip install -r requirements.txt
```

Set the following environment variables (or edit `config.py`):

| Variable | Description |
|---|---|
| `GCP_PROJECT_ID` | Your GCP project ID |
| `GOOGLE_APPLICATION_CREDENTIALS` | Path to GCP service account JSON key |
| `GDRIVE_CREDENTIALS_FILE` | Path to OAuth2 client secrets JSON from Google Cloud Console |

## Drive Folder Layout

The pipeline creates and uses the following folders inside your Drive:

```
My Drive/
└── sepsis_rl/
    ├── raw/          ← raw BigQuery extracts (parquet)
    ├── processed/    ← windowed feature + action datasets
    └── outputs/      ← model weights, metrics, plots
```
