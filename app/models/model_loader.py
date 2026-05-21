import joblib

# function to load model
def load_model():
    model_name: str = 'spam_classifier.pkl'

    try:
        model = joblib.load(model_name)
        return model

    except FileNotFoundError:
        raise RuntimeError(f'Model not found: {model_name}')

    except Exception as error:
        raise RuntimeError(f'Failed to load model: {str(error)}')
