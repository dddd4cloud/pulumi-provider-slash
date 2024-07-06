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

__all__ = [
    'GetShortcutServiceShortcutAnalyticResult',
    'AwaitableGetShortcutServiceShortcutAnalyticResult',
    'get_shortcut_service_shortcut_analytic',
    'get_shortcut_service_shortcut_analytic_output',
]

@pulumi.output_type
class GetShortcutServiceShortcutAnalyticResult:
    def __init__(__self__, items=None):
        if items and not isinstance(items, dict):
            raise TypeError("Expected argument 'items' to be a dict")
        pulumi.set(__self__, "items", items)

    @property
    @pulumi.getter
    def items(self) -> 'outputs.V1GetShortcutAnalyticsResponse':
        return pulumi.get(self, "items")


class AwaitableGetShortcutServiceShortcutAnalyticResult(GetShortcutServiceShortcutAnalyticResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetShortcutServiceShortcutAnalyticResult(
            items=self.items)


def get_shortcut_service_shortcut_analytic(id: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetShortcutServiceShortcutAnalyticResult:
    """
    Use this data source to access information about an existing resource.
    """
    __args__ = dict()
    __args__['id'] = id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('slash:api:getShortcutServiceShortcutAnalytic', __args__, opts=opts, typ=GetShortcutServiceShortcutAnalyticResult).value

    return AwaitableGetShortcutServiceShortcutAnalyticResult(
        items=pulumi.get(__ret__, 'items'))


@_utilities.lift_output_func(get_shortcut_service_shortcut_analytic)
def get_shortcut_service_shortcut_analytic_output(id: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetShortcutServiceShortcutAnalyticResult]:
    """
    Use this data source to access information about an existing resource.
    """
    ...