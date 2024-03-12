from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from pl_firstdemo.config.ConfigStore import *
from pl_firstdemo.udfs.UDFs import *

def top_5_rows(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.limit(5)
