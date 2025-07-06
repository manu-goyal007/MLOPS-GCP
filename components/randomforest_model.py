from kfp.dsl import component, Input, Output, Dataset, Model

@component(
    packages_to_install=["pandas", "scikit-learn", "joblib", "fsspec", "gcsfs"],
    base_image="python:3.10"
)
def random_forest_model(train_data: Input[Dataset], model: Output[Model]):
    import pandas as pd
    import joblib
    import os
    from sklearn.ensemble import RandomForestClassifier
    from sklearn.preprocessing import StandardScaler

    df = pd.read_csv(train_data.path)
    X = df.drop("Outcome", axis=1)
    # scaler=StandardScaler()
    # X = scaler.fit_transform(X)
    
    

    y = df["Outcome"]

    model_clf = RandomForestClassifier()
    model_clf.fit(X, y)

    os.makedirs(model.path, exist_ok=True)
    # "scaler": scaler
    joblib.dump( model_clf, f"{model.path}/model.joblib")
