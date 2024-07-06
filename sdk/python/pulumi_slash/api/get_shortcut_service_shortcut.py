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
    'GetShortcutServiceShortcutResult',
    'AwaitableGetShortcutServiceShortcutResult',
    'get_shortcut_service_shortcut',
    'get_shortcut_service_shortcut_output',
]

@pulumi.output_type
class GetShortcutServiceShortcutResult:
    def __init__(__self__, items=None):
        if items and not isinstance(items, dict):
            raise TypeError("Expected argument 'items' to be a dict")
        pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter
    def items(self) -> 'outputs.V1GetShortcutResponse':
        return pulumi.get(self, "items")


class AwaitableGetShortcutServiceShortcutResult(GetShortcutServiceShortcutResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetShortcutServiceShortcutResult(
            items=self.items)


def get_shortcut_service_shortcut(id: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetShortcutServiceShortcutResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('slash:api:getShortcutServiceShortcut', __args__, opts=opts, typ=GetShortcutServiceShortcutResult).value

    return AwaitableGetShortcutServiceShortcutResult(
        items=pulumi.get(__ret__, 'items'))


@_utilities.lift_output_func(get_shortcut_service_shortcut)
def get_shortcut_service_shortcut_output(id: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetShortcutServiceShortcutResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...