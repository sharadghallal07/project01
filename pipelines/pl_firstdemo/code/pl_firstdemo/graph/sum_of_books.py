from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_firstdemo.config.ConfigStore import *
from pl_firstdemo.udfs.UDFs import *

def sum_of_books(spark: SparkSession, in0: DataFrame) -> DataFrame:
    df1 = in0.groupBy(col("book_id"))

    return df1.agg(sum(col("price")).alias("Sum"))
