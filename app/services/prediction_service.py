from app.models.model_loader import model
from app.core.logger import logger

class PredictionService():
    @staticmethod
    def predict(email: str) -> str:
        try:
            if not email or not email.strip():
                raise ValueError(f'Email cannot be empty.')

            logger.info(email)
            prediction = model.predict([email])
            logger.info('Prediction successful.')

            return "Spam" if prediction[0] == 1 else "Not Spam"

        except Exception as e:
            logger.info(f'Prediction failed. {e}')
            raise RuntimeError(f'Error while predicting: {str(e)}')