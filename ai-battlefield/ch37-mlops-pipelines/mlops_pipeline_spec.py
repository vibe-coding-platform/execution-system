# Ch37 MLOps Pipeline - CI/CT/CD for Ch36A agent workflows → $2M/yr (End-to-End MLOps Pipeline)
from prefect import flow, task
from mlflow.tracking import MlflowClient
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import pandas as pd
import joblib

mlflow_client = MlflowClient()

@task
def data_ingestion():
    """Data pipeline → Feature store"""
    df = pd.read_parquet("ch34_agent_executions.parquet")  # Ch34 intelligence
    return df[["agent_id", "success", "latency_ms", "savings_usd"]]

@task  
def feature_engineering(df):
    """Ch37 Feature store → ML ready"""
    features = df.groupby('agent_id').agg({
        'success': ['mean', 'count'],
        'latency_ms': 'mean',
        'savings_usd': 'sum'
    }).round(4)
    return features

@task
def model_training(features):
    """Weekly model retrain → Agent improvement predictions"""
    X = features.drop(columns=['success-mean'])
    y = features['success-mean']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    pipeline = Pipeline([
        ('model', RandomForestRegressor(n_estimators=100))
    ])
    pipeline.fit(X_train, y_train)
    
    # MLflow tracking
    with mlflow.start_run():
        mlflow.log_metric("test_r2", pipeline.score(X_test, y_test))
        mlflow.sklearn.log_model(pipeline, "agent_optimizer")
        mlflow.log_param("n_estimators", 100)
    
    return pipeline

@flow(name="Ch37.MLOpsWeekly")
def mlops_pipeline():
    """CI/CT/CD → Production model weekly"""
    df = data_ingestion()
    features = feature_engineering(df)
    model = model_training(features)
    return {"model_uri": mlflow_client.active_run().info.run_id}
