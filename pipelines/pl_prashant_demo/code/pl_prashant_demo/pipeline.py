from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_prashant_demo.config.ConfigStore import *
from pl_prashant_demo.udfs.UDFs import *
from prophecy.utils import *
from pl_prashant_demo.graph import *

def pipeline(spark: SparkSession) -> None:
    df_ds_csv_filter = ds_csv_filter(spark)
    df_price_above_30 = price_above_30(spark, df_ds_csv_filter)
    ds_csv_price_filter(spark, df_price_above_30)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_prashant_demo")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pl_prashant_demo", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pl_prashant_demo")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
