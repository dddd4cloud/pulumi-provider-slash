// Code generated by pulumigen DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package api

import (
	"context"
	"reflect"

	"github.com/dddd4cloud/pulumi-provider-slash/sdk/go/slash/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupCollectionServiceCollection(ctx *pulumi.Context, args *LookupCollectionServiceCollectionArgs, opts ...pulumi.InvokeOption) (*LookupCollectionServiceCollectionResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCollectionServiceCollectionResult
	err := ctx.Invoke("slash:api:getCollectionServiceCollection", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return rv.Defaults(), nil
}

type LookupCollectionServiceCollectionArgs struct {
	Id string `pulumi:"id"`
}

type LookupCollectionServiceCollectionResult struct {
	Items V1GetCollectionResponse `pulumi:"items"`
}

// Defaults sets the appropriate defaults for LookupCollectionServiceCollectionResult
func (val *LookupCollectionServiceCollectionResult) Defaults() *LookupCollectionServiceCollectionResult {
	if val == nil {
		return nil
	}
	tmp := *val
	tmp.Items = *tmp.Items.Defaults()

	return &tmp
}

func LookupCollectionServiceCollectionOutput(ctx *pulumi.Context, args LookupCollectionServiceCollectionOutputArgs, opts ...pulumi.InvokeOption) LookupCollectionServiceCollectionResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCollectionServiceCollectionResult, error) {
			args := v.(LookupCollectionServiceCollectionArgs)
			r, err := LookupCollectionServiceCollection(ctx, &args, opts...)
			var s LookupCollectionServiceCollectionResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCollectionServiceCollectionResultOutput)
}

type LookupCollectionServiceCollectionOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (LookupCollectionServiceCollectionOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCollectionServiceCollectionArgs)(nil)).Elem()
}

type LookupCollectionServiceCollectionResultOutput struct{ *pulumi.OutputState }

func (LookupCollectionServiceCollectionResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCollectionServiceCollectionResult)(nil)).Elem()
}

func (o LookupCollectionServiceCollectionResultOutput) ToLookupCollectionServiceCollectionResultOutput() LookupCollectionServiceCollectionResultOutput {
	return o
}

func (o LookupCollectionServiceCollectionResultOutput) ToLookupCollectionServiceCollectionResultOutputWithContext(ctx context.Context) LookupCollectionServiceCollectionResultOutput {
	return o
}

func (o LookupCollectionServiceCollectionResultOutput) Items() V1GetCollectionResponseOutput {
	return o.ApplyT(func(v LookupCollectionServiceCollectionResult) V1GetCollectionResponse { return v.Items }).(V1GetCollectionResponseOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCollectionServiceCollectionResultOutput{})
}