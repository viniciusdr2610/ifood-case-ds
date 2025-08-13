from pathlib import Path
from typing import Dict
from pyspark.sql import SparkSession
from pyspark.sql import DataFrame


def create_spark_session(app_name: str = "iFood_Data_Processing_PySpark") -> SparkSession:
    return SparkSession.builder \
        .appName(app_name) \
        .config("spark.driver.extraJavaOptions", "-Djava.security.manager=allow") \
        .config("spark.executor.extraJavaOptions", "-Djava.security.manager=allow") \
        .config("spark.network.timeout", "3600s") \
        .config("spark.executor.heartbeatInterval", "60s") \
        .getOrCreate()

def load_json_data(file_path: Path, spark_session: SparkSession) -> DataFrame:
    print(f"Carregando: {file_path}")
    
    if not file_path.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")
    
    try:
        return spark_session.read.json(str(file_path), multiLine=True)                    
        
    except Exception as e:
        print(f"Erro ao carregar {file_path.name}: {e}")
        raise

def display_data_info_spark(df: DataFrame, df_name: str) -> None:
    print(f"\nINFORMATIONS - {df_name}")
    
    # Informações básicas
    row_count = df.count()
    print(f"📏 Row Count: ({row_count})")
    print(f"🔍 Columns: {df.columns}")
    
    # Schema detalhado
    df.printSchema()
    # Mostrar primeiras linhas
    print(f"First 3 rows:")
    df.show(3, truncate=False)