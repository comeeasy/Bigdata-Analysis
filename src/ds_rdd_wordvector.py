import pyspark
import os


if __name__ == "__main__":
    myConf = pyspark.SparkConf()
    spark = pyspark.sql.SparkSession\
            .builder\
            .master('local')\
            .config(conf=myConf)\
            .appName('s-4')\
            .getOrCreate()

    wikiRdd = spark.sparkContext.textFile(os.path.join("data", "ds_spark_wiki.txt"))
    words = wikiRdd.flatMap(lambda x: x.split(sep=" "))\
                   .map(lambda x: (x.lower().rstrip()\
                        .lstrip().rstrip(',').lstrip('.'), 1))\
                 .reduceByKey(lambda x, y: x + y)
                #.groupByKey().mapValues(sum) # 동일한 결과 

    
    print(words.sortBy(lambda x: -x[1]).collect())
    spark.stop()
