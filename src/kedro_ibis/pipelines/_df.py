from delta.tables import converToDelta

# Spark DataFrame
def to_table(***kwargs):
    for name, df in kwargs.items():
        df.createOrReplaceTempView(name)


# Spark Delta Table
def to_delta(df: DataFrame):
    df = df.convertToDelta(spark, "parquet.`<path-to-table>`")