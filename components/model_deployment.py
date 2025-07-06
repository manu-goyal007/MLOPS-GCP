from kfp.dsl import component, Input, Model
from typing import NamedTuple
PROJECT_ID = "egqrcxl-acn-mlops-train-s-c"
REGION = "us-east1"

@component
def compare_models(
    lr_accuracy: float,
    xgb_accuracy: float
) -> str:
    best_model = "rf_model" if lr_accuracy >= xgb_accuracy else "xgb_model"
    print(f"Best model is: {best_model}")
    return best_model

@component(packages_to_install=["kfp","google-cloud-aiplatform"],
            base_image="python:3.10" )
def deploy_best_model(
    best_model: str,
    lr_model_path: Input[Model],
    xgb_model_path: Input[Model]
)-> NamedTuple("DeployOutput", [("endpoint_url", str)]):
    from google.cloud import aiplatform
    from collections import namedtuple
    # aiplatform.init(project=PROJECT_ID, location=REGION)

    model_path = lr_model_path.path if best_model == "rf_model" else xgb_model_path.path

    model = aiplatform.Model.upload(
        display_name=f"{best_model}-diabetes-model",
        artifact_uri=lr_model_path.path,
        serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/sklearn-cpu.1-0:latest"
    )
    model.wait()
    endpoint = aiplatform.Endpoint.create(display_name=f"{best_model}-endpoint")

    endpoint_url = f"https://console.cloud.google.com/vertex-ai/locations/us-east1/endpoints/{endpoint.name.split('/')[-1]}?project=651302270690"
    print(f"this will be endpoint url : {endpoint_url}")
    model.deploy(endpoint=endpoint,
    machine_type="n1-standard-16",  
    traffic_split={"0": 100},
    traffic_percentage=100)

    

    print(f"Deployed to: {endpoint_url}")
    output = namedtuple("DeployOutput", ["endpoint_url"])
    return output(endpoint_url)