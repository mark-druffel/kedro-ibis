"""
This is a boilerplate pipeline 'demo'
generated using Kedro 0.19.2
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import *
def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            #node(
            #    func=None,
            #    inputs="source_yellow@spark",
            #    outputs="raw_yellow@spark",
            #    name="raw_yellow"
            #)

        ]
    )
