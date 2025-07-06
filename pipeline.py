# from kfp.v2 import dsl
# ! pip install kfp google-cloud-aiplatform
from config import *
from components.load_data import load_data
from components.split import train_test_split
from components.randomforest_model import random_forest_model
from components.evaluate import evaluate_model,evaluate_model_noscale
from components.xgboost_model import xg_boost_model
from components.model_deployment import compare_models, deploy_best_model
import os
from google.cloud import aiplatform
from kfp import compiler
from kfp.dsl import pipeline, component, Input, Output, Dataset, Model, Metrics


# Initialize Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION, staging_bucket=f"gs://{BUCKET_NAME}")

# Define the pipeline
@pipeline(name=PIPELINE_NAME, pipeline_root=f"gs://{BUCKET_NAME}/pipeline-root")
def cohort5_diabetes_pipeline(gcs_path: str):

    data_task = load_data(gcs_path=gcs_path)
    split_task=train_test_split(input_data=data_task.outputs["input_data"])
    randomforest_model_task = random_forest_model(train_data=split_task.outputs["train_data"])
    xgb_model_component=xg_boost_model(train_data=split_task.outputs["train_data"])
    randomforest_model_eval=evaluate_model(
        test_data=split_task.outputs["test_data"],
        model=randomforest_model_task.outputs["model"]
    )
    xgb_eval=evaluate_model_noscale(
        test_data=split_task.outputs["test_data"],
        model=xgb_model_component.outputs["model_xgb"]
        )
    best_model = compare_models(
            lr_accuracy=randomforest_model_eval.outputs["accuracy"],
            xgb_accuracy=xgb_eval.outputs["accuracy"]
        )

    deploy_best_model(
        best_model=best_model.output,
        lr_model_path=randomforest_model_task.outputs["model"],
        xgb_model_path=xgb_model_component.outputs["model_xgb"]
    )


# Compile the pipeline
compiler.Compiler().compile(
    pipeline_func=cohort5_diabetes_pipeline,
    package_path=PACKAGE_PATH
)

# Submit the pipeline job
pipeline_job = aiplatform.PipelineJob(
    display_name=PIPELINE_NAME,
    template_path=PACKAGE_PATH,
    parameter_values={"gcs_path": GCS_DATA_PATH},
    enable_caching=True,
    project=PROJECT_ID,
    location=REGION,
)

pipeline_job.run(service_account=SERVICE_ACCOUNT)