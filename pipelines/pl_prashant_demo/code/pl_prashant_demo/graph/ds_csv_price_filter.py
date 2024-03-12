from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_prashant_demo.config.ConfigStore import *
from pl_prashant_demo.udfs.UDFs import *

def ds_csv_price_filter(spark: SparkSession, in0: DataFrame):
    in0.write\
        .option("header", True)\
        .option("sep", ",")\
        .mode("error")\
        .option("separator", ",")\
        .option("header", True)\
        .csv("dbfs:/mnt/demo-datasets/bookstore/books-csv/priceFilter")
