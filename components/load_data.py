from kfp.dsl import component, Output, Dataset

@component(
    packages_to_install=["pandas", "fsspec", "gcsfs"],
    base_image="python:3.10"
)
def load_data(gcs_path: str, input_data: Output[Dataset]):
    import pandas as pd

    df=pd.read_csv(gcs_path)

    df.to_csv(input_data.path, index=False)
    # df.to_csv(df.path, index=False)