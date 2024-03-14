from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pl_firstdemo.udfs.UDFs import *
from . import *
from .config import *

def Subgraph_1(spark: SparkSession, subgraph_config: SubgraphConfig) -> DataFrame:
    Config.update(subgraph_config)
    df_ds_csv = ds_csv(spark)
    df_top_5_rows = top_5_rows(spark, df_ds_csv)
    subgraph_config.update(Config)

    return df_top_5_rows
