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

__all__ = ['CollectionServiceCollectionArgs', 'CollectionServiceCollection']

@pulumi.input_type
class CollectionServiceCollectionArgs:
    def __init__(__self__, *,
                 created_time: Optional[pulumi.Input[str]] = None,
                 creator_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shortcut_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 updated_time: Optional[pulumi.Input[str]] = None,
                 visibility: Optional[pulumi.Input['Visibility']] = None):
        """
        The set of arguments for constructing a CollectionServiceCollection resource.
        """
        if created_time is not None:
            pulumi.set(__self__, "created_time", created_time)
        if creator_id is not None:
            pulumi.set(__self__, "creator_id", creator_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if shortcut_ids is not None:
            pulumi.set(__self__, "shortcut_ids", shortcut_ids)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if updated_time is not None:
            pulumi.set(__self__, "updated_time", updated_time)
        if visibility is None:
            visibility = 'VISIBILITY_UNSPECIFIED'
        if visibility is not None:
            pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "created_time")

    @created_time.setter
    def created_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_time", value)

    @property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "creator_id")

    @creator_id.setter
    def creator_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "creator_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="shortcutIds")
    def shortcut_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "shortcut_ids")

    @shortcut_ids.setter
    def shortcut_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "shortcut_ids", value)

    @property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "updated_time")

    @updated_time.setter
    def updated_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "updated_time", value)

    @property
    @pulumi.getter
    def visibility(self) -> Optional[pulumi.Input['Visibility']]:
        return pulumi.get(self, "visibility")

    @visibility.setter
    def visibility(self, value: Optional[pulumi.Input['Visibility']]):
        pulumi.set(self, "visibility", value)


class CollectionServiceCollection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_time: Optional[pulumi.Input[str]] = None,
                 creator_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shortcut_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 updated_time: Optional[pulumi.Input[str]] = None,
                 visibility: Optional[pulumi.Input['Visibility']] = None,
                 __props__=None):
        """
        Create a CollectionServiceCollection resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[CollectionServiceCollectionArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a CollectionServiceCollection resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param CollectionServiceCollectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CollectionServiceCollectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 created_time: Optional[pulumi.Input[str]] = None,
                 creator_id: Optional[pulumi.Input[int]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 shortcut_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 updated_time: Optional[pulumi.Input[str]] = None,
                 visibility: Optional[pulumi.Input['Visibility']] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CollectionServiceCollectionArgs.__new__(CollectionServiceCollectionArgs)

            __props__.__dict__["created_time"] = created_time
            __props__.__dict__["creator_id"] = creator_id
            __props__.__dict__["description"] = description
            __props__.__dict__["name"] = name
            __props__.__dict__["shortcut_ids"] = shortcut_ids
            __props__.__dict__["title"] = title
            __props__.__dict__["updated_time"] = updated_time
            if visibility is None:
                visibility = 'VISIBILITY_UNSPECIFIED'
            __props__.__dict__["visibility"] = visibility
            __props__.__dict__["collection"] = None
        super(CollectionServiceCollection, __self__).__init__(
            'slash:api:CollectionServiceCollection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CollectionServiceCollection':
        """
        Get an existing CollectionServiceCollection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CollectionServiceCollectionArgs.__new__(CollectionServiceCollectionArgs)

        __props__.__dict__["collection"] = None
        __props__.__dict__["created_time"] = None
        __props__.__dict__["creator_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["shortcut_ids"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["updated_time"] = None
        __props__.__dict__["visibility"] = None
        return CollectionServiceCollection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def collection(self) -> pulumi.Output[Optional['outputs.Apiv1Collection']]:
        return pulumi.get(self, "collection")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> pulumi.Output[Optional[int]]:
        return pulumi.get(self, "creator_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="shortcutIds")
    def shortcut_ids(self) -> pulumi.Output[Optional[Sequence[int]]]:
        return pulumi.get(self, "shortcut_ids")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> pulumi.Output[Optional[str]]:
        return pulumi.get(self, "updated_time")

    @property
    @pulumi.getter
    def visibility(self) -> pulumi.Output[Optional['Visibility']]:
        return pulumi.get(self, "visibility")
