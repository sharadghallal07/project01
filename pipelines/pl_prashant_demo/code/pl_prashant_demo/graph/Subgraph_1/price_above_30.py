from pyspark.sql import *
from pyspark.sql.functions import *
from pyspark.sql.types import *
from prophecy.utils import *
from prophecy.libs import typed_lit
from .config import *
from pl_prashant_demo.udfs.UDFs import *

def price_above_30(spark: SparkSession, in0: DataFrame) -> DataFrame:
    return in0.filter((col("price") > lit(20)))
