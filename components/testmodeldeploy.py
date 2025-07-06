    
from google.cloud import aiplatform
from collections import namedtuple
PROJECT_ID = "egqrcxl-acn-mlops-train-s-c"
REGION = "us-east1"
BUCKET_NAME = "cohort5_mlopstraining"
SERVICE_ACCOUNT = "cohort5-vai-sa@egqrcxl-acn-mlops-train-s-c.iam.gserviceaccount.com"
GCS_DATA_PATH = f"gs://{BUCKET_NAME}/data/diabetes.csv"
endpoint_name = "diabetes-endpoint-manu"
PIPELINE_NAME = "cohort5_diabetes-pipeline-mg"
PACKAGE_PATH="cohort5_diabetes_package.json"


aiplatform.init(project=PROJECT_ID, location=REGION)
model = aiplatform.Model.upload(
    display_name=f"mg-rf-diabetes-model",
    artifact_uri='gs://cohort5_mlopstraining/pipeline-root/651302270690/cohort5-diabetes-pipeline-mg-20250617071308/random-forest-model_3921263222367191040/model',
    serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-0:latest"
)
model.wait()
endpoint = aiplatform.Endpoint.create(display_name=f"mg-rf-diabetes-model-endpoint")

endpoint_url = f"https://console.cloud.google.com/vertex-ai/locations/{REGION}/endpoints/{endpoint.name.split('/')[-1]}?project={PROJECT_ID}"
model.deploy(endpoint=endpoint,
machine_type="n1-standard-16",  
traffic_split={"0": 100},
traffic_percentage=100)

# endpoint_url = f"https://console.cloud.google.com/vertex-ai/locations/{REGION}/endpoints/{endpoint.name.split('/')[-1]}?project={PROJECT_ID}"



print(endpoint_url)