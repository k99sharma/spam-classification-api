import joblib
from app.core.logger import logger

# function to load model
def load_model():
    model_name: str = 'spam_classifier.pkl'

    try:
        model = joblib.load(model_name)
        logger.info("Loaded model '{}'".format(model_name))
        return model

    except FileNotFoundError:
        logger.error("Model '{}' not found".format(model_name))
        raise RuntimeError(f'Model not found: {model_name}')

    except Exception as error:
        logger.error(error)
        raise RuntimeError(f'Failed to load model: {str(error)}')
