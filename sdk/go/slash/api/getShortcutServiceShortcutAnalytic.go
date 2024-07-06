// Code generated by pulumigen DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package api

import (
	"context"
	"reflect"

	"github.com/dddd4cloud/pulumi-provider-slash/sdk/go/slash/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func GetShortcutServiceShortcutAnalytic(ctx *pulumi.Context, args *GetShortcutServiceShortcutAnalyticArgs, opts ...pulumi.InvokeOption) (*GetShortcutServiceShortcutAnalyticResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetShortcutServiceShortcutAnalyticResult
	err := ctx.Invoke("slash:api:getShortcutServiceShortcutAnalytic", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type GetShortcutServiceShortcutAnalyticArgs struct {
	Id string `pulumi:"id"`
}

type GetShortcutServiceShortcutAnalyticResult struct {
	Items V1GetShortcutAnalyticsResponse `pulumi:"items"`
}

func GetShortcutServiceShortcutAnalyticOutput(ctx *pulumi.Context, args GetShortcutServiceShortcutAnalyticOutputArgs, opts ...pulumi.InvokeOption) GetShortcutServiceShortcutAnalyticResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetShortcutServiceShortcutAnalyticResult, error) {
			args := v.(GetShortcutServiceShortcutAnalyticArgs)
			r, err := GetShortcutServiceShortcutAnalytic(ctx, &args, opts...)
			var s GetShortcutServiceShortcutAnalyticResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetShortcutServiceShortcutAnalyticResultOutput)
}

type GetShortcutServiceShortcutAnalyticOutputArgs struct {
	Id pulumi.StringInput `pulumi:"id"`
}

func (GetShortcutServiceShortcutAnalyticOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetShortcutServiceShortcutAnalyticArgs)(nil)).Elem()
}

type GetShortcutServiceShortcutAnalyticResultOutput struct{ *pulumi.OutputState }

func (GetShortcutServiceShortcutAnalyticResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetShortcutServiceShortcutAnalyticResult)(nil)).Elem()
}

func (o GetShortcutServiceShortcutAnalyticResultOutput) ToGetShortcutServiceShortcutAnalyticResultOutput() GetShortcutServiceShortcutAnalyticResultOutput {
	return o
}

func (o GetShortcutServiceShortcutAnalyticResultOutput) ToGetShortcutServiceShortcutAnalyticResultOutputWithContext(ctx context.Context) GetShortcutServiceShortcutAnalyticResultOutput {
	return o
}

func (o GetShortcutServiceShortcutAnalyticResultOutput) Items() V1GetShortcutAnalyticsResponseOutput {
	return o.ApplyT(func(v GetShortcutServiceShortcutAnalyticResult) V1GetShortcutAnalyticsResponse { return v.Items }).(V1GetShortcutAnalyticsResponseOutput)
}

func init() {
	pulumi.RegisterOutputType(GetShortcutServiceShortcutAnalyticResultOutput{})
}
