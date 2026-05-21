from pydantic import BaseModel
from typing import Any
from app.core.logger import logger

class PredictionService(BaseModel):
    model: Any

    def predict(self, email: str) -> str:
        try:
            if not email or not email.strip():
                raise ValueError(f'Email cannot be empty.')

            prediction = self.model.predict(email)
            logger.info('Prediction successful.')

            return "Spam" if prediction[0] == 1 else "Not Spam"

        except Exception as e:
            logger.info(f'Prediction failed. {e}')
            raise RuntimeError(f'Error while predicting: {str(e)}')