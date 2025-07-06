from kfp.dsl import component, Input , Output , Dataset , Model

@component(
    packages_to_install=["pandas", "scikit-learn", 'xgboost',"joblib", "fsspec", "gcsfs"],
    base_image="python:3.10"
)
def xg_boost_model(train_data: Input[Dataset], model_xgb: Output[Model]):
    
    import pandas as pd
    import joblib
    import os
    import xgboost as xgb

    df=pd.read_csv(train_data.path)
    X=df.drop("Outcome", axis=1)
    y=df["Outcome"]

    model_clf=xgb.XGBClassifier()
    model_clf.fit(X,y)

    os.makedirs(model_xgb.path, exist_ok=True)
    joblib.dump( model_clf, f"{model_xgb.path}/model.joblib")