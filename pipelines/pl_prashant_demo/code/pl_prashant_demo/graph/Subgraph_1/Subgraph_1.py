from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from pl_prashant_demo.udfs.UDFs import *
from . import *
from .config import *

def Subgraph_1(spark: SparkSession, subgraph_config: SubgraphConfig) -> DataFrame:
    Config.update(subgraph_config)
    df_ds_csv_filter = ds_csv_filter(spark)
    df_price_above_30 = price_above_30(spark, df_ds_csv_filter)
    subgraph_config.update(Config)

    return df_price_above_30
