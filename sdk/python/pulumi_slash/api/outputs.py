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
    'Apiv1AutoBackupWorkspaceSetting',
    'Apiv1Collection',
    'Apiv1OpenGraphMetadata',
    'Apiv1Shortcut',
    'Apiv1UserSetting',
    'Apiv1WorkspaceSetting',
    'V1GetCollectionResponse',
    'V1GetShortcutResponse',
    'V1GetUserResponse',
    'V1GetUserSettingResponse',
    'V1GetWorkspaceProfileResponse',
    'V1GetWorkspaceSettingResponse',
    'V1ListCollectionsResponse',
    'V1ListShortcutsResponse',
    'V1ListUserAccessTokensResponse',
    'V1ListUsersResponse',
    'V1User',
    'V1UserAccessToken',
    'V1WorkspaceProfile',
]

@pulumi.output_type
class Apiv1AutoBackupWorkspaceSetting(dict):
    def __init__(__self__, *,
                 cron_expression: Optional[str] = None,
                 enabled: Optional[bool] = None,
                 max_keep: Optional[int] = None):
        """
        :param str cron_expression: The cron expression for auto backup.
               For example, "0 0 0 * * *" means backup at 00:00:00 every day.
               See https://en.wikipedia.org/wiki/Cron for more details.
        :param bool enabled: Whether auto backup is enabled.
        :param int max_keep: The maximum number of backups to keep.
        """
        if cron_expression is not None:
            pulumi.set(__self__, "cron_expression", cron_expression)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if max_keep is not None:
            pulumi.set(__self__, "max_keep", max_keep)

    @property
    @pulumi.getter(name="cronExpression")
    def cron_expression(self) -> Optional[str]:
        """
        The cron expression for auto backup.
        For example, "0 0 0 * * *" means backup at 00:00:00 every day.
        See https://en.wikipedia.org/wiki/Cron for more details.
        """
        return pulumi.get(self, "cron_expression")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Whether auto backup is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="maxKeep")
    def max_keep(self) -> Optional[int]:
        """
        The maximum number of backups to keep.
        """
        return pulumi.get(self, "max_keep")


@pulumi.output_type
class Apiv1Collection(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdTime":
            suggest = "created_time"
        elif key == "creatorId":
            suggest = "creator_id"
        elif key == "updatedTime":
            suggest = "updated_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Apiv1Collection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Apiv1Collection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Apiv1Collection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_time: Optional[str] = None,
                 creator_id: Optional[int] = None,
                 description: Optional[str] = None,
                 id: Optional[int] = None,
                 ids: Optional[Sequence[int]] = None,
                 name: Optional[str] = None,
                 title: Optional[str] = None,
                 updated_time: Optional[str] = None,
                 visibility: Optional['Apiv1CollectionVisibility'] = None):
        if created_time is not None:
            pulumi.set(__self__, "created_time", created_time)
        if creator_id is not None:
            pulumi.set(__self__, "creator_id", creator_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if ids is not None:
            pulumi.set(__self__, "ids", ids)
        if name is not None:
            pulumi.set(__self__, "name", name)
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
    def created_time(self) -> Optional[str]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> Optional[int]:
        return pulumi.get(self, "creator_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[int]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def ids(self) -> Optional[Sequence[int]]:
        return pulumi.get(self, "ids")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> Optional[str]:
        return pulumi.get(self, "updated_time")

    @property
    @pulumi.getter
    def visibility(self) -> Optional['Apiv1CollectionVisibility']:
        return pulumi.get(self, "visibility")


@pulumi.output_type
class Apiv1OpenGraphMetadata(dict):
    def __init__(__self__, *,
                 description: Optional[str] = None,
                 image: Optional[str] = None,
                 title: Optional[str] = None):
        if description is not None:
            pulumi.set(__self__, "description", description)
        if image is not None:
            pulumi.set(__self__, "image", image)
        if title is not None:
            pulumi.set(__self__, "title", title)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def image(self) -> Optional[str]:
        return pulumi.get(self, "image")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        return pulumi.get(self, "title")


@pulumi.output_type
class Apiv1Shortcut(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdTime":
            suggest = "created_time"
        elif key == "creatorId":
            suggest = "creator_id"
        elif key == "ogMetadata":
            suggest = "og_metadata"
        elif key == "rowStatus":
            suggest = "row_status"
        elif key == "updatedTime":
            suggest = "updated_time"
        elif key == "viewCount":
            suggest = "view_count"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in Apiv1Shortcut. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        Apiv1Shortcut.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        Apiv1Shortcut.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_time: Optional[str] = None,
                 creator_id: Optional[int] = None,
                 description: Optional[str] = None,
                 id: Optional[int] = None,
                 link: Optional[str] = None,
                 name: Optional[str] = None,
                 og_metadata: Optional['outputs.Apiv1OpenGraphMetadata'] = None,
                 row_status: Optional['Apiv1ShortcutRowStatus'] = None,
                 tags: Optional[Sequence[str]] = None,
                 title: Optional[str] = None,
                 updated_time: Optional[str] = None,
                 view_count: Optional[int] = None,
                 visibility: Optional['Apiv1ShortcutVisibility'] = None):
        if created_time is not None:
            pulumi.set(__self__, "created_time", created_time)
        if creator_id is not None:
            pulumi.set(__self__, "creator_id", creator_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if link is not None:
            pulumi.set(__self__, "link", link)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if og_metadata is not None:
            pulumi.set(__self__, "og_metadata", og_metadata)
        if row_status is None:
            row_status = 'ROW_STATUS_UNSPECIFIED'
        if row_status is not None:
            pulumi.set(__self__, "row_status", row_status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if title is not None:
            pulumi.set(__self__, "title", title)
        if updated_time is not None:
            pulumi.set(__self__, "updated_time", updated_time)
        if view_count is not None:
            pulumi.set(__self__, "view_count", view_count)
        if visibility is None:
            visibility = 'VISIBILITY_UNSPECIFIED'
        if visibility is not None:
            pulumi.set(__self__, "visibility", visibility)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter(name="creatorId")
    def creator_id(self) -> Optional[int]:
        return pulumi.get(self, "creator_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> Optional[int]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def link(self) -> Optional[str]:
        return pulumi.get(self, "link")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="ogMetadata")
    def og_metadata(self) -> Optional['outputs.Apiv1OpenGraphMetadata']:
        return pulumi.get(self, "og_metadata")

    @property
    @pulumi.getter(name="rowStatus")
    def row_status(self) -> Optional['Apiv1ShortcutRowStatus']:
        return pulumi.get(self, "row_status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def title(self) -> Optional[str]:
        return pulumi.get(self, "title")

    @property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> Optional[str]:
        return pulumi.get(self, "updated_time")

    @property
    @pulumi.getter(name="viewCount")
    def view_count(self) -> Optional[int]:
        return pulumi.get(self, "view_count")

    @property
    @pulumi.getter
    def visibility(self) -> Optional['Apiv1ShortcutVisibility']:
        return pulumi.get(self, "visibility")


@pulumi.output_type
class Apiv1UserSetting(dict):
    def __init__(__self__, *,
                 color_theme: Optional['Apiv1UserSettingColorTheme'] = None,
                 id: Optional[int] = None,
                 locale: Optional['Apiv1UserSettingLocale'] = None):
        """
        :param int id: id is the user id.
        """
        if color_theme is None:
            color_theme = 'COLOR_THEME_UNSPECIFIED'
        if color_theme is not None:
            pulumi.set(__self__, "color_theme", color_theme)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if locale is None:
            locale = 'LOCALE_UNSPECIFIED'
        if locale is not None:
            pulumi.set(__self__, "locale", locale)

    @property
    @pulumi.getter(name="colorTheme")
    def color_theme(self) -> Optional['Apiv1UserSettingColorTheme']:
        return pulumi.get(self, "color_theme")

    @property
    @pulumi.getter
    def id(self) -> Optional[int]:
        """
        id is the user id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def locale(self) -> Optional['Apiv1UserSettingLocale']:
        return pulumi.get(self, "locale")


@pulumi.output_type
class Apiv1WorkspaceSetting(dict):
    def __init__(__self__, *,
                 auto_backup: Optional['outputs.Apiv1AutoBackupWorkspaceSetting'] = None,
                 custom_script: Optional[str] = None,
                 custom_style: Optional[str] = None,
                 default_visibility: Optional['Apiv1WorkspaceSettingDefaultVisibility'] = None,
                 enable_signup: Optional[bool] = None,
                 favicon_provider: Optional[str] = None,
                 instance_url: Optional[str] = None,
                 license_key: Optional[str] = None):
        """
        :param str custom_script: The custom script.
        :param str custom_style: The custom style.
        :param bool enable_signup: Whether to enable other users to sign up.
        :param str favicon_provider: The url of custom favicon provider.
        :param str instance_url: The instance URL.
        """
        if auto_backup is not None:
            pulumi.set(__self__, "auto_backup", auto_backup)
        if custom_script is not None:
            pulumi.set(__self__, "custom_script", custom_script)
        if custom_style is not None:
            pulumi.set(__self__, "custom_style", custom_style)
        if default_visibility is None:
            default_visibility = 'VISIBILITY_UNSPECIFIED'
        if default_visibility is not None:
            pulumi.set(__self__, "default_visibility", default_visibility)
        if enable_signup is not None:
            pulumi.set(__self__, "enable_signup", enable_signup)
        if favicon_provider is not None:
            pulumi.set(__self__, "favicon_provider", favicon_provider)
        if instance_url is not None:
            pulumi.set(__self__, "instance_url", instance_url)
        if license_key is not None:
            pulumi.set(__self__, "license_key", license_key)

    @property
    @pulumi.getter(name="autoBackup")
    def auto_backup(self) -> Optional['outputs.Apiv1AutoBackupWorkspaceSetting']:
        return pulumi.get(self, "auto_backup")

    @property
    @pulumi.getter(name="customScript")
    def custom_script(self) -> Optional[str]:
        """
        The custom script.
        """
        return pulumi.get(self, "custom_script")

    @property
    @pulumi.getter(name="customStyle")
    def custom_style(self) -> Optional[str]:
        """
        The custom style.
        """
        return pulumi.get(self, "custom_style")

    @property
    @pulumi.getter(name="defaultVisibility")
    def default_visibility(self) -> Optional['Apiv1WorkspaceSettingDefaultVisibility']:
        return pulumi.get(self, "default_visibility")

    @property
    @pulumi.getter(name="enableSignup")
    def enable_signup(self) -> Optional[bool]:
        """
        Whether to enable other users to sign up.
        """
        return pulumi.get(self, "enable_signup")

    @property
    @pulumi.getter(name="faviconProvider")
    def favicon_provider(self) -> Optional[str]:
        """
        The url of custom favicon provider.
        """
        return pulumi.get(self, "favicon_provider")

    @property
    @pulumi.getter(name="instanceUrl")
    def instance_url(self) -> Optional[str]:
        """
        The instance URL.
        """
        return pulumi.get(self, "instance_url")

    @property
    @pulumi.getter(name="licenseKey")
    def license_key(self) -> Optional[str]:
        return pulumi.get(self, "license_key")


@pulumi.output_type
class V1GetCollectionResponse(dict):
    def __init__(__self__, *,
                 collection: Optional['outputs.Apiv1Collection'] = None):
        if collection is not None:
            pulumi.set(__self__, "collection", collection)

    @property
    @pulumi.getter
    def collection(self) -> Optional['outputs.Apiv1Collection']:
        return pulumi.get(self, "collection")


@pulumi.output_type
class V1GetShortcutResponse(dict):
    def __init__(__self__, *,
                 shortcut: Optional['outputs.Apiv1Shortcut'] = None):
        if shortcut is not None:
            pulumi.set(__self__, "shortcut", shortcut)

    @property
    @pulumi.getter
    def shortcut(self) -> Optional['outputs.Apiv1Shortcut']:
        return pulumi.get(self, "shortcut")


@pulumi.output_type
class V1GetUserResponse(dict):
    def __init__(__self__, *,
                 user: Optional['outputs.V1User'] = None):
        if user is not None:
            pulumi.set(__self__, "user", user)

    @property
    @pulumi.getter
    def user(self) -> Optional['outputs.V1User']:
        return pulumi.get(self, "user")


@pulumi.output_type
class V1GetUserSettingResponse(dict):
    def __init__(__self__, *,
                 user_setting: Optional['outputs.Apiv1UserSetting'] = None):
        if user_setting is not None:
            pulumi.set(__self__, "user_setting", user_setting)

    @property
    @pulumi.getter(name="userSetting")
    def user_setting(self) -> Optional['outputs.Apiv1UserSetting']:
        return pulumi.get(self, "user_setting")


@pulumi.output_type
class V1GetWorkspaceProfileResponse(dict):
    def __init__(__self__, *,
                 profile: Optional['outputs.V1WorkspaceProfile'] = None):
        if profile is not None:
            pulumi.set(__self__, "profile", profile)

    @property
    @pulumi.getter
    def profile(self) -> Optional['outputs.V1WorkspaceProfile']:
        return pulumi.get(self, "profile")


@pulumi.output_type
class V1GetWorkspaceSettingResponse(dict):
    def __init__(__self__, *,
                 setting: Optional['outputs.Apiv1WorkspaceSetting'] = None):
        if setting is not None:
            pulumi.set(__self__, "setting", setting)

    @property
    @pulumi.getter
    def setting(self) -> Optional['outputs.Apiv1WorkspaceSetting']:
        return pulumi.get(self, "setting")


@pulumi.output_type
class V1ListCollectionsResponse(dict):
    def __init__(__self__, *,
                 collections: Optional[Sequence['outputs.Apiv1Collection']] = None):
        if collections is not None:
            pulumi.set(__self__, "collections", collections)

    @property
    @pulumi.getter
    def collections(self) -> Optional[Sequence['outputs.Apiv1Collection']]:
        return pulumi.get(self, "collections")


@pulumi.output_type
class V1ListShortcutsResponse(dict):
    def __init__(__self__, *,
                 shortcuts: Optional[Sequence['outputs.Apiv1Shortcut']] = None):
        if shortcuts is not None:
            pulumi.set(__self__, "shortcuts", shortcuts)

    @property
    @pulumi.getter
    def shortcuts(self) -> Optional[Sequence['outputs.Apiv1Shortcut']]:
        return pulumi.get(self, "shortcuts")


@pulumi.output_type
class V1ListUserAccessTokensResponse(dict):
    def __init__(__self__, *,
                 access_tokens: Optional[Sequence['outputs.V1UserAccessToken']] = None):
        if access_tokens is not None:
            pulumi.set(__self__, "access_tokens", access_tokens)

    @property
    @pulumi.getter(name="accessTokens")
    def access_tokens(self) -> Optional[Sequence['outputs.V1UserAccessToken']]:
        return pulumi.get(self, "access_tokens")


@pulumi.output_type
class V1ListUsersResponse(dict):
    def __init__(__self__, *,
                 users: Optional[Sequence['outputs.V1User']] = None):
        if users is not None:
            pulumi.set(__self__, "users", users)

    @property
    @pulumi.getter
    def users(self) -> Optional[Sequence['outputs.V1User']]:
        return pulumi.get(self, "users")


@pulumi.output_type
class V1User(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdTime":
            suggest = "created_time"
        elif key == "rowStatus":
            suggest = "row_status"
        elif key == "updatedTime":
            suggest = "updated_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in V1User. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        V1User.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        V1User.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_time: Optional[str] = None,
                 email: Optional[str] = None,
                 id: Optional[int] = None,
                 nickname: Optional[str] = None,
                 password: Optional[str] = None,
                 role: Optional['V1UserRole'] = None,
                 row_status: Optional['V1UserRowStatus'] = None,
                 updated_time: Optional[str] = None):
        if created_time is not None:
            pulumi.set(__self__, "created_time", created_time)
        if email is not None:
            pulumi.set(__self__, "email", email)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if nickname is not None:
            pulumi.set(__self__, "nickname", nickname)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if role is None:
            role = 'ROLE_UNSPECIFIED'
        if role is not None:
            pulumi.set(__self__, "role", role)
        if row_status is None:
            row_status = 'ROW_STATUS_UNSPECIFIED'
        if row_status is not None:
            pulumi.set(__self__, "row_status", row_status)
        if updated_time is not None:
            pulumi.set(__self__, "updated_time", updated_time)

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> Optional[str]:
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def email(self) -> Optional[str]:
        return pulumi.get(self, "email")

    @property
    @pulumi.getter
    def id(self) -> Optional[int]:
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def nickname(self) -> Optional[str]:
        return pulumi.get(self, "nickname")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def role(self) -> Optional['V1UserRole']:
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="rowStatus")
    def row_status(self) -> Optional['V1UserRowStatus']:
        return pulumi.get(self, "row_status")

    @property
    @pulumi.getter(name="updatedTime")
    def updated_time(self) -> Optional[str]:
        return pulumi.get(self, "updated_time")


@pulumi.output_type
class V1UserAccessToken(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "accessToken":
            suggest = "access_token"
        elif key == "expiresAt":
            suggest = "expires_at"
        elif key == "issuedAt":
            suggest = "issued_at"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in V1UserAccessToken. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        V1UserAccessToken.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        V1UserAccessToken.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 access_token: Optional[str] = None,
                 description: Optional[str] = None,
                 expires_at: Optional[str] = None,
                 issued_at: Optional[str] = None):
        if access_token is not None:
            pulumi.set(__self__, "access_token", access_token)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if issued_at is not None:
            pulumi.set(__self__, "issued_at", issued_at)

    @property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[str]:
        return pulumi.get(self, "access_token")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[str]:
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter(name="issuedAt")
    def issued_at(self) -> Optional[str]:
        return pulumi.get(self, "issued_at")


@pulumi.output_type
class V1WorkspaceProfile(dict):
    def __init__(__self__, *,
                 custom_script: Optional[str] = None,
                 custom_style: Optional[str] = None,
                 enable_signup: Optional[bool] = None,
                 favicon_provider: Optional[str] = None,
                 mode: Optional[str] = None,
                 owner: Optional[str] = None,
                 plan: Optional['V1WorkspaceProfilePlan'] = None,
                 version: Optional[str] = None):
        """
        :param str custom_script: The custom script.
        :param str custom_style: The custom style.
        :param bool enable_signup: Whether to enable other users to sign up.
        :param str favicon_provider: The url of custom favicon provider.
        :param str mode: Current workspace mode: dev, prod.
        :param str version: Current workspace version.
        """
        if custom_script is not None:
            pulumi.set(__self__, "custom_script", custom_script)
        if custom_style is not None:
            pulumi.set(__self__, "custom_style", custom_style)
        if enable_signup is not None:
            pulumi.set(__self__, "enable_signup", enable_signup)
        if favicon_provider is not None:
            pulumi.set(__self__, "favicon_provider", favicon_provider)
        if mode is not None:
            pulumi.set(__self__, "mode", mode)
        if owner is not None:
            pulumi.set(__self__, "owner", owner)
        if plan is None:
            plan = 'PLAN_TYPE_UNSPECIFIED'
        if plan is not None:
            pulumi.set(__self__, "plan", plan)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="customScript")
    def custom_script(self) -> Optional[str]:
        """
        The custom script.
        """
        return pulumi.get(self, "custom_script")

    @property
    @pulumi.getter(name="customStyle")
    def custom_style(self) -> Optional[str]:
        """
        The custom style.
        """
        return pulumi.get(self, "custom_style")

    @property
    @pulumi.getter(name="enableSignup")
    def enable_signup(self) -> Optional[bool]:
        """
        Whether to enable other users to sign up.
        """
        return pulumi.get(self, "enable_signup")

    @property
    @pulumi.getter(name="faviconProvider")
    def favicon_provider(self) -> Optional[str]:
        """
        The url of custom favicon provider.
        """
        return pulumi.get(self, "favicon_provider")

    @property
    @pulumi.getter
    def mode(self) -> Optional[str]:
        """
        Current workspace mode: dev, prod.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def owner(self) -> Optional[str]:
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter
    def plan(self) -> Optional['V1WorkspaceProfilePlan']:
        return pulumi.get(self, "plan")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        Current workspace version.
        """
        return pulumi.get(self, "version")


