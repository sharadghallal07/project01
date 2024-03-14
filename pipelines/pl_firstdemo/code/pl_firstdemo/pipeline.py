from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pl_firstdemo.config.ConfigStore import *
from pl_firstdemo.udfs.UDFs import *
from prophecy.utils import *
from pl_firstdemo.graph import *

def pipeline(spark: SparkSession) -> None:
    df_Subgraph_1 = Subgraph_1(spark, Config.Subgraph_1)
    df_sum_of_books = sum_of_books(spark, df_Subgraph_1)
    df_limit_2_rows = limit_2_rows(spark, df_sum_of_books)
    ds_csv_output(spark, df_limit_2_rows)

def main():
    spark = SparkSession.builder\
                .config("spark.default.parallelism", "4")\
                .config("spark.sql.legacy.allowUntypedScalaUDF", "true")\
                .enableHiveSupport()\
                .appName("Prophecy Pipeline")\
                .getOrCreate()\
                .newSession()
    Utils.initializeFromArgs(spark, parse_args())
    spark.conf.set("prophecy.metadata.pipeline.uri", "pipelines/pl_firstdemo")
    registerUDFs(spark)

    try:
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pl_firstdemo", config = Config)
    except :
        
        MetricsCollector.start(spark = spark, pipelineId = "pipelines/pl_firstdemo")

    pipeline(spark)
    MetricsCollector.end(spark)

if __name__ == "__main__":
    main()
