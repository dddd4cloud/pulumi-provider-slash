# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'ListCollectionServiceCollectionsResult',
    'AwaitableListCollectionServiceCollectionsResult',
    'list_collection_service_collections',
    'list_collection_service_collections_output',
]

@pulumi.output_type
class ListCollectionServiceCollectionsResult:
    def __init__(__self__, items=None):
        if items and not isinstance(items, dict):
            raise TypeError("Expected argument 'items' to be a dict")
        pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter
    def items(self) -> 'outputs.V1ListCollectionsResponse':
        return pulumi.get(self, "items")


class AwaitableListCollectionServiceCollectionsResult(ListCollectionServiceCollectionsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListCollectionServiceCollectionsResult(
            items=self.items)


def list_collection_service_collections(opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListCollectionServiceCollectionsResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('slash:api:listCollectionServiceCollections', __args__, opts=opts, typ=ListCollectionServiceCollectionsResult).value

    return AwaitableListCollectionServiceCollectionsResult(
        items=pulumi.get(__ret__, 'items'))


@_utilities.lift_output_func(list_collection_service_collections)
def list_collection_service_collections_output(opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListCollectionServiceCollectionsResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...