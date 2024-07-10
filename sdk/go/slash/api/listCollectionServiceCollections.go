// Code generated by pulumigen DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package api

import (
	"context"
	"reflect"

	"github.com/dddd4cloud/pulumi-provider-slash/sdk/go/slash/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func ListCollectionServiceCollections(ctx *pulumi.Context, args *ListCollectionServiceCollectionsArgs, opts ...pulumi.InvokeOption) (*ListCollectionServiceCollectionsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv ListCollectionServiceCollectionsResult
	err := ctx.Invoke("slash:api:listCollectionServiceCollections", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type ListCollectionServiceCollectionsArgs struct {
}

type ListCollectionServiceCollectionsResult struct {
	Items V1ListCollectionsResponse `pulumi:"items"`
}

func ListCollectionServiceCollectionsOutput(ctx *pulumi.Context, args ListCollectionServiceCollectionsOutputArgs, opts ...pulumi.InvokeOption) ListCollectionServiceCollectionsResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (ListCollectionServiceCollectionsResult, error) {
			args := v.(ListCollectionServiceCollectionsArgs)
			r, err := ListCollectionServiceCollections(ctx, &args, opts...)
			var s ListCollectionServiceCollectionsResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(ListCollectionServiceCollectionsResultOutput)
}

type ListCollectionServiceCollectionsOutputArgs struct {
}

func (ListCollectionServiceCollectionsOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*ListCollectionServiceCollectionsArgs)(nil)).Elem()
}

type ListCollectionServiceCollectionsResultOutput struct{ *pulumi.OutputState }

func (ListCollectionServiceCollectionsResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*ListCollectionServiceCollectionsResult)(nil)).Elem()
}

func (o ListCollectionServiceCollectionsResultOutput) ToListCollectionServiceCollectionsResultOutput() ListCollectionServiceCollectionsResultOutput {
	return o
}

func (o ListCollectionServiceCollectionsResultOutput) ToListCollectionServiceCollectionsResultOutputWithContext(ctx context.Context) ListCollectionServiceCollectionsResultOutput {
	return o
}

func (o ListCollectionServiceCollectionsResultOutput) Items() V1ListCollectionsResponseOutput {
	return o.ApplyT(func(v ListCollectionServiceCollectionsResult) V1ListCollectionsResponse { return v.Items }).(V1ListCollectionsResponseOutput)
}

func init() {
	pulumi.RegisterOutputType(ListCollectionServiceCollectionsResultOutput{})
}
