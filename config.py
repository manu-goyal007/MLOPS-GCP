PROJECT_ID = "mlops" # Replace with your actual project ID
REGION = "us-east1"
BUCKET_NAME = "mlops" # Replace with your actual bucket name
SERVICE_ACCOUNT = "mlops--s-c.iam.gserviceaccount.com" # Replace with your actual service account email
GCS_DATA_PATH = f"gs://{BUCKET_NAME}/data/diabetes.csv"
endpoint_name = "diabetes-endpoint-manu"
PIPELINE_NAME = "cohort5_diabetes-pipeline-mg"
PACKAGE_PATH="cohort5_diabetes_package.json"