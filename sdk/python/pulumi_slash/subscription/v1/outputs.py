# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs
from ._enums import *

__all__ = [
    'V1GetSubscriptionResponse',
    'V1Subscription',
]

@pulumi.output_type
class V1GetSubscriptionResponse(dict):
    def __init__(__self__, *,
                 subscription: Optional['outputs.V1Subscription'] = None):
        if subscription is not None:
            pulumi.set(__self__, "subscription", subscription)

    @property
    @pulumi.getter
    def subscription(self) -> Optional['outputs.V1Subscription']:
        return pulumi.get(self, "subscription")


@pulumi.output_type
class V1Subscription(dict):
    def __init__(__self__, *,
                 expires_time: Optional[str] = None,
                 plan: Optional['V1SubscriptionPlan'] = None,
                 started_time: Optional[str] = None):
        if expires_time is not None:
            pulumi.set(__self__, "expires_time", expires_time)
        if plan is None:
            plan = 'PLAN_TYPE_UNSPECIFIED'
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if started_time is not None:
            pulumi.set(__self__, "started_time", started_time)

    @property
    @pulumi.getter(name="expiresTime")
    def expires_time(self) -> Optional[str]:
        return pulumi.get(self, "expires_time")

    @property
    @pulumi.getter
    def plan(self) -> Optional['V1SubscriptionPlan']:
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter(name="startedTime")
    def started_time(self) -> Optional[str]:
        return pulumi.get(self, "started_time")

