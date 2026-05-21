from app.schemas.request_schema import EmailRequest
from app.schemas.response_schema import SuccessResponse, ErrorResponse
from app.services.prediction_service import PredictionService
from fastapi import APIRouter

router = APIRouter()

# router
@router.post('/predict')
def predict(data: EmailRequest):
    try:
        prediction = PredictionService.predict(data.email)

        return SuccessResponse(
            message='Prediction successful',
            data=prediction,
        )

    except Exception as e:
        return ErrorResponse(
            message='Prediction failed',
            error=e,
        )
