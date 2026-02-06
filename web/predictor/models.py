from django.db import models


class Prediction(models.Model):
    """Model prediction record.

    Attributes:
        input_data: Input features to the model.
        prediction_result: Predicted outcome (survived or not).
        prediction_probability: Probability of the predicted outcome.
        timestamp: When the prediction was made.
    """
    input_data = models.JSONField()
    prediction_result = models.BooleanField()
    prediction_probability = models.DecimalField(max_digits=5, decimal_places=4)
    timestamp = models.DateTimeField(auto_now_add=True)
