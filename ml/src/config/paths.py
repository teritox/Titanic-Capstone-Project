from pathlib import Path

# Repository root: .../<repo>/ml/src/config/paths.py -> parents[3] = <repo>
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Trained model file
MODEL_PATH = (PROJECT_ROOT / "web/predictor/titanic_model.pkl").resolve()

# Raw Kaggle-style input files
RAW_TRAIN_PATH = (PROJECT_ROOT / "ml/data/train.csv").resolve()
RAW_TEST_PATH = (PROJECT_ROOT / "ml/data/test.csv").resolve()

# Post-cleaning outputs
CLEANED_TRAIN_PATH = (PROJECT_ROOT / "ml/data/processed/train_cleaned.csv").resolve()
CLEANED_TEST_PATH = (PROJECT_ROOT / "ml/data/processed/test_cleaned.csv").resolve()

# Post-feature-engineering outputs
FEATURES_TRAIN_PATH = (PROJECT_ROOT / "ml/data/processed/train_features.csv").resolve()
FEATURES_TEST_PATH = (PROJECT_ROOT / "ml/data/processed/test_features.csv").resolve()

# Canonical default inputs for modeling/training code
MODEL_INPUT_TRAIN_PATH = FEATURES_TRAIN_PATH
MODEL_INPUT_TEST_PATH = FEATURES_TEST_PATH
