from kfp.v2.dsl import component, Input, Dataset, Model
from typing import NamedTuple

@component(
    packages_to_install=["pandas", "scikit-learn", "joblib", "fsspec", "gcsfs"],
    base_image="python:3.10"
)
def evaluate_model(test_data: Input[Dataset], model: Input[Model]) -> NamedTuple("EvaluationOutput", [("accuracy", float)]):
    import pandas as pd
    import joblib
    from sklearn.metrics import accuracy_score
    from collections import namedtuple

    df = pd.read_csv(test_data.path)
    X = df.drop("Outcome", axis=1)
    # X = preprocess(X)
    y = df["Outcome"]

    model_clf = joblib.load(model.path + "/model.joblib")
    # model_clf = saved["model"]
    # scaler = saved["scaler"]
    # X = scaler.transform(X)
    preds = model_clf.predict(X)
    acc = accuracy_score(y, preds)

    output = namedtuple("EvaluationOutput", ["accuracy"])
    print("Model Accuracy:", acc)
    return output(acc)

@component(
    packages_to_install=["pandas", "scikit-learn",'xgboost', "joblib", "fsspec", "gcsfs"],
    base_image="python:3.10"
)
def evaluate_model_noscale(test_data: Input[Dataset], model: Input[Model]) -> NamedTuple("EvaluationOutput", [("accuracy", float)]):
    import pandas as pd
    import joblib
    from sklearn.metrics import accuracy_score
    from collections import namedtuple

    df = pd.read_csv(test_data.path)
    X = df.drop("Outcome", axis=1)
    # X = preprocess(X)
    y = df["Outcome"]

    model_clf = joblib.load(model.path + "/model.joblib")
    # model_clf = saved["model"]
    # scaler = saved["scaler"]
    # X = scaler.transform(X)
    preds = model_clf.predict(X)
    acc = accuracy_score(y, preds)

    output = namedtuple("EvaluationOutput", ["accuracy"])
    print("Model Accuracy:", acc)
    return output(acc)
