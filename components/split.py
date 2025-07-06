from kfp.dsl import component, Input, Output, Dataset

@component(
    packages_to_install=["pandas", "scikit-learn", "joblib", "fsspec", "gcsfs"],
    base_image="python:3.10"
)
def train_test_split(input_data: Input[Dataset], train_data: Output[Dataset], test_data: Output[Dataset]):
    import pandas as pd
    from sklearn.model_selection import train_test_split

    df = pd.read_csv(input_data.path)
    df = df.fillna(df.mean(numeric_only=True))

    
    train_df, test_df = train_test_split(df, test_size=0.2, random_state=42)

    train_df.to_csv(train_data.path, index=False)
    test_df.to_csv(test_data.path, index=False)
