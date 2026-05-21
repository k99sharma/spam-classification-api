import joblib
from pathlib import Path
from app.core.logger import logger

# function to load model
def load_model():
    MODEL_PATH = Path(__file__).parent / "spam_classifier.pkl"

    try:
        model = joblib.load(MODEL_PATH)
        logger.info("Loaded model from '{}'".format(MODEL_PATH))
        return model

    except FileNotFoundError:
        logger.error("Model '{}' not found at ".format(MODEL_PATH))
        raise RuntimeError(f'Model not found at: {MODEL_PATH}')

    except Exception as error:
        logger.error(error)
        raise RuntimeError(f'Failed to load model: {str(error)}')

model = load_model()