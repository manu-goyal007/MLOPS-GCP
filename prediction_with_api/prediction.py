from google.cloud import aiplatform
from typing import Any, Dict, List


def predict_custom_trained_model_sample(
    project: str,
    endpoint_id: str,
    location: str,
    instances: List[List[Any]],
    api_endpoint: str = None
) -> Dict:
    """
    Sends prediction request to a Vertex AI custom-trained model endpoint.

    Args:
        project (str): GCP Project ID
        endpoint_id (str): Vertex AI Endpoint ID
        location (str): GCP Region, e.g., "us-central1"
        instances (List[List[Any]]): List of input instances for prediction
        api_endpoint (str): Optional override for API endpoint

    Returns:
        Dict: Response from the prediction endpoint
    """
    # Default to region-specific API endpoint
    aiplatform.init(project=project, location=location)

    # Construct the full endpoint resource name
    endpoint = aiplatform.Endpoint(endpoint_name=f"projects/{project}/locations/{location}/endpoints/{endpoint_id}")

    # Make prediction
    response = endpoint.predict(instances=instances)

    print("Prediction results:")
    for prediction in response.predictions:
        print(prediction)

    return response.predictions


if __name__ == "__main__":
    # Example usage
    project = "651302270690" # Replace with your actual project ID
    endpoint_id = "7811261556720664576" # Replace with your actual endpoint ID
    location = "us-central1"

    input_instances = [
        [2, 130, 70, 20, 79, 28.4, 0.45, 32],
        [5, 155, 80, 33, 130, 35.2, 0.75, 41]
    ]

    predict_custom_trained_model_sample(
        project=project,
        endpoint_id=endpoint_id,
        location=location,
        instances=input_instances
        
    )
