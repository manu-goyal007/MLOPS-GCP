# MLOPS in GCP 
## Description

 -- In this repository, end to end pipeline is created for the machine learning using kubeflow and deployed in GCP with help of Vertex ai other functionality like model registry and endpoint is tested
## How the pipeline looks in Vertex AI 

    <img src="Pictures/vertex-pipeline.png" width="500" alt="A visual workflow diagram of a machine learning pipeline in Vertex AI. The pipeline starts with a load data step, followed by train test split. Two parallel branches train random forest and XGBoost models. Each model is evaluated, with one branch using evaluate model and the other using evaluate model noscale. The results are compared in a compare models step, and the best model is deployed in the deploy best model step. Each step is labeled with the corresponding Python version, and the diagram is set on a grid background, conveying a structured and organized process flow."/>

## How the endpoint working in Vertex UI 
    <img src="Pictures\EndPoint-prediction.png" width="500" alt="Google Cloud Vertex AI user interface showing a deployed diabetes prediction model endpoint. The screen displays the endpoint status as active, with details such as ID, region, and last updated time. Below, a Test your model section allows users to input a JSON request with instances of numerical data and parameters. The Response panel on the right shows a JSON output with predictions and model metadata. The environment is a typical cloud dashboard with navigation menus on the left for model registry, online prediction, and other Vertex AI features. The tone is technical and informative, focused on machine learning model deployment and testing."/>    

## Future Works to incorporate 
    -- Monitoring and Drift detection 
    -- Scalable with Flask API for enterprise use on real use case
    -- Add Test case to check and ensure the flow is working fine 
         Unit tests for pipelines using pytest
         Model validation checks (e.g., no NaNs, shape consistency, schema check)
    -- Machine learning side 
         Hyperparamter tuning and use mlfow to trac and versioning 
         Fairness, Explainability & Interpretability
            SHAP / LIME for model explanations
            Bias detection (feature parity, demographic parity)
            Feature attribution reports in MLflow
    