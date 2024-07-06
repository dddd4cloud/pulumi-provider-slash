// Code generated by pulumigen DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package api

import (
	"context"
	"reflect"

	"github.com/dddd4cloud/pulumi-provider-slash/sdk/go/slash/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func ListUserServiceUsers(ctx *pulumi.Context, args *ListUserServiceUsersArgs, opts ...pulumi.InvokeOption) (*ListUserServiceUsersResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv ListUserServiceUsersResult
	err := ctx.Invoke("slash:api:listUserServiceUsers", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type ListUserServiceUsersArgs struct {
}

type ListUserServiceUsersResult struct {
	Items V1ListUsersResponse `pulumi:"items"`
}

func ListUserServiceUsersOutput(ctx *pulumi.Context, args ListUserServiceUsersOutputArgs, opts ...pulumi.InvokeOption) ListUserServiceUsersResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (ListUserServiceUsersResult, error) {
			args := v.(ListUserServiceUsersArgs)
			r, err := ListUserServiceUsers(ctx, &args, opts...)
			var s ListUserServiceUsersResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(ListUserServiceUsersResultOutput)
}

type ListUserServiceUsersOutputArgs struct {
}

func (ListUserServiceUsersOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ListUserServiceUsersArgs)(nil)).Elem()
}

type ListUserServiceUsersResultOutput struct{ *pulumi.OutputState }

func (ListUserServiceUsersResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ListUserServiceUsersResult)(nil)).Elem()
}

func (o ListUserServiceUsersResultOutput) ToListUserServiceUsersResultOutput() ListUserServiceUsersResultOutput {
	return o
}

func (o ListUserServiceUsersResultOutput) ToListUserServiceUsersResultOutputWithContext(ctx context.Context) ListUserServiceUsersResultOutput {
	return o
}

func (o ListUserServiceUsersResultOutput) Items() V1ListUsersResponseOutput {
	return o.ApplyT(func(v ListUserServiceUsersResult) V1ListUsersResponse { return v.Items }).(V1ListUsersResponseOutput)
}

func init() {
	pulumi.RegisterOutputType(ListUserServiceUsersResultOutput{})
}
