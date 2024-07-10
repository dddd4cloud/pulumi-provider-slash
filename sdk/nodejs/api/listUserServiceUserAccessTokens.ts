// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

export function listUserServiceUserAccessTokens(args: ListUserServiceUserAccessTokensArgs, opts?: pulumi.InvokeOptions): Promise<ListUserServiceUserAccessTokensResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("slash:api:listUserServiceUserAccessTokens", {
        "id": args.id,
    }, opts);
}

export interface ListUserServiceUserAccessTokensArgs {
    /**
     * id is the user id.
     */
    id: string;
}

export interface ListUserServiceUserAccessTokensResult {
    readonly items: outputs.api.V1ListUserAccessTokensResponse;
}
export function listUserServiceUserAccessTokensOutput(args: ListUserServiceUserAccessTokensOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<ListUserServiceUserAccessTokensResult> {
    return pulumi.output(args).apply((a: any) => listUserServiceUserAccessTokens(a, opts))
}

export interface ListUserServiceUserAccessTokensOutputArgs {
    /**
     * id is the user id.
     */
    id: pulumi.Input<string>;
}
