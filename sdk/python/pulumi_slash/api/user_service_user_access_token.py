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

__all__ = ['UserServiceUserAccessTokenArgs', 'UserServiceUserAccessToken']

@pulumi.input_type
class UserServiceUserAccessTokenArgs:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UserServiceUserAccessToken resource.
        :param pulumi.Input[str] description: description is the description of the access token.
        :param pulumi.Input[str] expires_at: expires_at is the expiration time of the access token.
               If expires_at is not set, the access token will never expire.
        :param pulumi.Input[str] id: id is the user id.
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        description is the description of the access token.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        expires_at is the expiration time of the access token.
        If expires_at is not set, the access token will never expire.
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        id is the user id.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


class UserServiceUserAccessToken(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a UserServiceUserAccessToken resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: description is the description of the access token.
        :param pulumi.Input[str] expires_at: expires_at is the expiration time of the access token.
               If expires_at is not set, the access token will never expire.
        :param pulumi.Input[str] id: id is the user id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[UserServiceUserAccessTokenArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a UserServiceUserAccessToken resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param UserServiceUserAccessTokenArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UserServiceUserAccessTokenArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = UserServiceUserAccessTokenArgs.__new__(UserServiceUserAccessTokenArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["expires_at"] = expires_at
            __props__.__dict__["id"] = id
            __props__.__dict__["access_token"] = None
        super(UserServiceUserAccessToken, __self__).__init__(
            'slash:api:UserServiceUserAccessToken',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'UserServiceUserAccessToken':
        """
        Get an existing UserServiceUserAccessToken resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = UserServiceUserAccessTokenArgs.__new__(UserServiceUserAccessTokenArgs)

        __props__.__dict__["access_token"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["expires_at"] = None
        return UserServiceUserAccessToken(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> pulumi.Output[Optional['outputs.V1UserAccessToken']]:
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        description is the description of the access token.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[Optional[str]]:
        """
        expires_at is the expiration time of the access token.
        If expires_at is not set, the access token will never expire.
        """
        return pulumi.get(self, "expires_at")
