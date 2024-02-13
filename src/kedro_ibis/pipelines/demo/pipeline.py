"""
This is a boilerplate pipeline 'demo'
generated using Kedro 0.19.2
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import write_delta
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=write_delta,
                inputs={"yellow_trips": "yellow_trips_spark"},
                outputs=None,
                name="delta"
            )

        ]
    )
