"""
This is a boilerplate pipeline 'demo'
generated using Kedro 0.19.2
"""
def write_delta(**kwargs):
    path = "data/bronze/managed/"
    for name, df in kwargs.items():
        filepath = f"{path}{name}"
        df.write.mode("overwrite").format("delta").save(filepath)
    return filepath