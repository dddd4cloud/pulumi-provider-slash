// Code generated by pulumigen DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package api

import (
	"context"
	"reflect"

	"github.com/dddd4cloud/pulumi-provider-slash/sdk/go/slash/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

var _ = internal.GetEnvOrDefault

type Apiv1OpenGraphMetadata struct {
	Description *string `pulumi:"description"`
	Image       *string `pulumi:"image"`
	Title       *string `pulumi:"title"`
}

// Apiv1OpenGraphMetadataInput is an input type that accepts Apiv1OpenGraphMetadataArgs and Apiv1OpenGraphMetadataOutput values.
// You can construct a concrete instance of `Apiv1OpenGraphMetadataInput` via:
//
//	Apiv1OpenGraphMetadataArgs{...}
type Apiv1OpenGraphMetadataInput interface {
	pulumi.Input

	ToApiv1OpenGraphMetadataOutput() Apiv1OpenGraphMetadataOutput
	ToApiv1OpenGraphMetadataOutputWithContext(context.Context) Apiv1OpenGraphMetadataOutput
}

type Apiv1OpenGraphMetadataArgs struct {
	Description pulumi.StringPtrInput `pulumi:"description"`
	Image       pulumi.StringPtrInput `pulumi:"image"`
	Title       pulumi.StringPtrInput `pulumi:"title"`
}

func (Apiv1OpenGraphMetadataArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*Apiv1OpenGraphMetadata)(nil)).Elem()
}

func (i Apiv1OpenGraphMetadataArgs) ToApiv1OpenGraphMetadataOutput() Apiv1OpenGraphMetadataOutput {
	return i.ToApiv1OpenGraphMetadataOutputWithContext(context.Background())
}

func (i Apiv1OpenGraphMetadataArgs) ToApiv1OpenGraphMetadataOutputWithContext(ctx context.Context) Apiv1OpenGraphMetadataOutput {
	return pulumi.ToOutputWithContext(ctx, i).(Apiv1OpenGraphMetadataOutput)
}

func (i Apiv1OpenGraphMetadataArgs) ToApiv1OpenGraphMetadataPtrOutput() Apiv1OpenGraphMetadataPtrOutput {
	return i.ToApiv1OpenGraphMetadataPtrOutputWithContext(context.Background())
}

func (i Apiv1OpenGraphMetadataArgs) ToApiv1OpenGraphMetadataPtrOutputWithContext(ctx context.Context) Apiv1OpenGraphMetadataPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(Apiv1OpenGraphMetadataOutput).ToApiv1OpenGraphMetadataPtrOutputWithContext(ctx)
}

// Apiv1OpenGraphMetadataPtrInput is an input type that accepts Apiv1OpenGraphMetadataArgs, Apiv1OpenGraphMetadataPtr and Apiv1OpenGraphMetadataPtrOutput values.
// You can construct a concrete instance of `Apiv1OpenGraphMetadataPtrInput` via:
//
//	        Apiv1OpenGraphMetadataArgs{...}
//
//	or:
//
//	        nil
type Apiv1OpenGraphMetadataPtrInput interface {
	pulumi.Input

	ToApiv1OpenGraphMetadataPtrOutput() Apiv1OpenGraphMetadataPtrOutput
	ToApiv1OpenGraphMetadataPtrOutputWithContext(context.Context) Apiv1OpenGraphMetadataPtrOutput
}

type apiv1OpenGraphMetadataPtrType Apiv1OpenGraphMetadataArgs

func Apiv1OpenGraphMetadataPtr(v *Apiv1OpenGraphMetadataArgs) Apiv1OpenGraphMetadataPtrInput {
	return (*apiv1OpenGraphMetadataPtrType)(v)
}

func (*apiv1OpenGraphMetadataPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Apiv1OpenGraphMetadata)(nil)).Elem()
}

func (i *apiv1OpenGraphMetadataPtrType) ToApiv1OpenGraphMetadataPtrOutput() Apiv1OpenGraphMetadataPtrOutput {
	return i.ToApiv1OpenGraphMetadataPtrOutputWithContext(context.Background())
}

func (i *apiv1OpenGraphMetadataPtrType) ToApiv1OpenGraphMetadataPtrOutputWithContext(ctx context.Context) Apiv1OpenGraphMetadataPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(Apiv1OpenGraphMetadataPtrOutput)
}

type Apiv1OpenGraphMetadataOutput struct{ *pulumi.OutputState }

func (Apiv1OpenGraphMetadataOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Apiv1OpenGraphMetadata)(nil)).Elem()
}

func (o Apiv1OpenGraphMetadataOutput) ToApiv1OpenGraphMetadataOutput() Apiv1OpenGraphMetadataOutput {
	return o
}

func (o Apiv1OpenGraphMetadataOutput) ToApiv1OpenGraphMetadataOutputWithContext(ctx context.Context) Apiv1OpenGraphMetadataOutput {
	return o
}

func (o Apiv1OpenGraphMetadataOutput) ToApiv1OpenGraphMetadataPtrOutput() Apiv1OpenGraphMetadataPtrOutput {
	return o.ToApiv1OpenGraphMetadataPtrOutputWithContext(context.Background())
}

func (o Apiv1OpenGraphMetadataOutput) ToApiv1OpenGraphMetadataPtrOutputWithContext(ctx context.Context) Apiv1OpenGraphMetadataPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v Apiv1OpenGraphMetadata) *Apiv1OpenGraphMetadata {
		return &v
	}).(Apiv1OpenGraphMetadataPtrOutput)
}

func (o Apiv1OpenGraphMetadataOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Apiv1OpenGraphMetadata) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o Apiv1OpenGraphMetadataOutput) Image() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Apiv1OpenGraphMetadata) *string { return v.Image }).(pulumi.StringPtrOutput)
}

func (o Apiv1OpenGraphMetadataOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Apiv1OpenGraphMetadata) *string { return v.Title }).(pulumi.StringPtrOutput)
}

type Apiv1OpenGraphMetadataPtrOutput struct{ *pulumi.OutputState }

func (Apiv1OpenGraphMetadataPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Apiv1OpenGraphMetadata)(nil)).Elem()
}

func (o Apiv1OpenGraphMetadataPtrOutput) ToApiv1OpenGraphMetadataPtrOutput() Apiv1OpenGraphMetadataPtrOutput {
	return o
}

func (o Apiv1OpenGraphMetadataPtrOutput) ToApiv1OpenGraphMetadataPtrOutputWithContext(ctx context.Context) Apiv1OpenGraphMetadataPtrOutput {
	return o
}

func (o Apiv1OpenGraphMetadataPtrOutput) Elem() Apiv1OpenGraphMetadataOutput {
	return o.ApplyT(func(v *Apiv1OpenGraphMetadata) Apiv1OpenGraphMetadata {
		if v != nil {
			return *v
		}
		var ret Apiv1OpenGraphMetadata
		return ret
	}).(Apiv1OpenGraphMetadataOutput)
}

func (o Apiv1OpenGraphMetadataPtrOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Apiv1OpenGraphMetadata) *string {
		if v == nil {
			return nil
		}
		return v.Description
	}).(pulumi.StringPtrOutput)
}

func (o Apiv1OpenGraphMetadataPtrOutput) Image() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Apiv1OpenGraphMetadata) *string {
		if v == nil {
			return nil
		}
		return v.Image
	}).(pulumi.StringPtrOutput)
}

func (o Apiv1OpenGraphMetadataPtrOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Apiv1OpenGraphMetadata) *string {
		if v == nil {
			return nil
		}
		return v.Title
	}).(pulumi.StringPtrOutput)
}

type Apiv1Shortcut struct {
	CreatedTime *string                  `pulumi:"createdTime"`
	CreatorId   *int                     `pulumi:"creatorId"`
	Description *string                  `pulumi:"description"`
	Id          *int                     `pulumi:"id"`
	Link        *string                  `pulumi:"link"`
	Name        *string                  `pulumi:"name"`
	OgMetadata  *Apiv1OpenGraphMetadata  `pulumi:"ogMetadata"`
	RowStatus   *Apiv1ShortcutRowStatus  `pulumi:"rowStatus"`
	Tags        []string                 `pulumi:"tags"`
	Title       *string                  `pulumi:"title"`
	UpdatedTime *string                  `pulumi:"updatedTime"`
	ViewCount   *int                     `pulumi:"viewCount"`
	Visibility  *Apiv1ShortcutVisibility `pulumi:"visibility"`
}

// Defaults sets the appropriate defaults for Apiv1Shortcut
func (val *Apiv1Shortcut) Defaults() *Apiv1Shortcut {
	if val == nil {
		return nil
	}
	tmp := *val
	if tmp.RowStatus == nil {
		rowStatus_ := Apiv1ShortcutRowStatus("ROW_STATUS_UNSPECIFIED")
		tmp.RowStatus = &rowStatus_
	}
	if tmp.Visibility == nil {
		visibility_ := Apiv1ShortcutVisibility("VISIBILITY_UNSPECIFIED")
		tmp.Visibility = &visibility_
	}
	return &tmp
}

type Apiv1ShortcutOutput struct{ *pulumi.OutputState }

func (Apiv1ShortcutOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Apiv1Shortcut)(nil)).Elem()
}

func (o Apiv1ShortcutOutput) ToApiv1ShortcutOutput() Apiv1ShortcutOutput {
	return o
}

func (o Apiv1ShortcutOutput) ToApiv1ShortcutOutputWithContext(ctx context.Context) Apiv1ShortcutOutput {
	return o
}

func (o Apiv1ShortcutOutput) CreatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *string { return v.CreatedTime }).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutOutput) CreatorId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *int { return v.CreatorId }).(pulumi.IntPtrOutput)
}

func (o Apiv1ShortcutOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *string { return v.Description }).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutOutput) Id() pulumi.IntPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *int { return v.Id }).(pulumi.IntPtrOutput)
}

func (o Apiv1ShortcutOutput) Link() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *string { return v.Link }).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutOutput) OgMetadata() Apiv1OpenGraphMetadataPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *Apiv1OpenGraphMetadata { return v.OgMetadata }).(Apiv1OpenGraphMetadataPtrOutput)
}

func (o Apiv1ShortcutOutput) RowStatus() Apiv1ShortcutRowStatusPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *Apiv1ShortcutRowStatus { return v.RowStatus }).(Apiv1ShortcutRowStatusPtrOutput)
}

func (o Apiv1ShortcutOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v Apiv1Shortcut) []string { return v.Tags }).(pulumi.StringArrayOutput)
}

func (o Apiv1ShortcutOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *string { return v.Title }).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutOutput) UpdatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *string { return v.UpdatedTime }).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutOutput) ViewCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *int { return v.ViewCount }).(pulumi.IntPtrOutput)
}

func (o Apiv1ShortcutOutput) Visibility() Apiv1ShortcutVisibilityPtrOutput {
	return o.ApplyT(func(v Apiv1Shortcut) *Apiv1ShortcutVisibility { return v.Visibility }).(Apiv1ShortcutVisibilityPtrOutput)
}

type Apiv1ShortcutPtrOutput struct{ *pulumi.OutputState }

func (Apiv1ShortcutPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Apiv1Shortcut)(nil)).Elem()
}

func (o Apiv1ShortcutPtrOutput) ToApiv1ShortcutPtrOutput() Apiv1ShortcutPtrOutput {
	return o
}

func (o Apiv1ShortcutPtrOutput) ToApiv1ShortcutPtrOutputWithContext(ctx context.Context) Apiv1ShortcutPtrOutput {
	return o
}

func (o Apiv1ShortcutPtrOutput) Elem() Apiv1ShortcutOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) Apiv1Shortcut {
		if v != nil {
			return *v
		}
		var ret Apiv1Shortcut
		return ret
	}).(Apiv1ShortcutOutput)
}

func (o Apiv1ShortcutPtrOutput) CreatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *string {
		if v == nil {
			return nil
		}
		return v.CreatedTime
	}).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) CreatorId() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *int {
		if v == nil {
			return nil
		}
		return v.CreatorId
	}).(pulumi.IntPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) Description() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *string {
		if v == nil {
			return nil
		}
		return v.Description
	}).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) Id() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *int {
		if v == nil {
			return nil
		}
		return v.Id
	}).(pulumi.IntPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) Link() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *string {
		if v == nil {
			return nil
		}
		return v.Link
	}).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *string {
		if v == nil {
			return nil
		}
		return v.Name
	}).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) OgMetadata() Apiv1OpenGraphMetadataPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *Apiv1OpenGraphMetadata {
		if v == nil {
			return nil
		}
		return v.OgMetadata
	}).(Apiv1OpenGraphMetadataPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) RowStatus() Apiv1ShortcutRowStatusPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *Apiv1ShortcutRowStatus {
		if v == nil {
			return nil
		}
		return v.RowStatus
	}).(Apiv1ShortcutRowStatusPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) Tags() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) []string {
		if v == nil {
			return nil
		}
		return v.Tags
	}).(pulumi.StringArrayOutput)
}

func (o Apiv1ShortcutPtrOutput) Title() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *string {
		if v == nil {
			return nil
		}
		return v.Title
	}).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) UpdatedTime() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *string {
		if v == nil {
			return nil
		}
		return v.UpdatedTime
	}).(pulumi.StringPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) ViewCount() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *int {
		if v == nil {
			return nil
		}
		return v.ViewCount
	}).(pulumi.IntPtrOutput)
}

func (o Apiv1ShortcutPtrOutput) Visibility() Apiv1ShortcutVisibilityPtrOutput {
	return o.ApplyT(func(v *Apiv1Shortcut) *Apiv1ShortcutVisibility {
		if v == nil {
			return nil
		}
		return v.Visibility
	}).(Apiv1ShortcutVisibilityPtrOutput)
}

type Apiv1ShortcutArrayOutput struct{ *pulumi.OutputState }

func (Apiv1ShortcutArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Apiv1Shortcut)(nil)).Elem()
}

func (o Apiv1ShortcutArrayOutput) ToApiv1ShortcutArrayOutput() Apiv1ShortcutArrayOutput {
	return o
}

func (o Apiv1ShortcutArrayOutput) ToApiv1ShortcutArrayOutputWithContext(ctx context.Context) Apiv1ShortcutArrayOutput {
	return o
}

func (o Apiv1ShortcutArrayOutput) Index(i pulumi.IntInput) Apiv1ShortcutOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Apiv1Shortcut {
		return vs[0].([]Apiv1Shortcut)[vs[1].(int)]
	}).(Apiv1ShortcutOutput)
}

type V1GetShortcutResponse struct {
	Shortcut *Apiv1Shortcut `pulumi:"shortcut"`
}

// Defaults sets the appropriate defaults for V1GetShortcutResponse
func (val *V1GetShortcutResponse) Defaults() *V1GetShortcutResponse {
	if val == nil {
		return nil
	}
	tmp := *val
	tmp.Shortcut = tmp.Shortcut.Defaults()

	return &tmp
}

type V1GetShortcutResponseOutput struct{ *pulumi.OutputState }

func (V1GetShortcutResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*V1GetShortcutResponse)(nil)).Elem()
}

func (o V1GetShortcutResponseOutput) ToV1GetShortcutResponseOutput() V1GetShortcutResponseOutput {
	return o
}

func (o V1GetShortcutResponseOutput) ToV1GetShortcutResponseOutputWithContext(ctx context.Context) V1GetShortcutResponseOutput {
	return o
}

func (o V1GetShortcutResponseOutput) Shortcut() Apiv1ShortcutPtrOutput {
	return o.ApplyT(func(v V1GetShortcutResponse) *Apiv1Shortcut { return v.Shortcut }).(Apiv1ShortcutPtrOutput)
}

type V1ListShortcutsResponse struct {
	Shortcuts []Apiv1Shortcut `pulumi:"shortcuts"`
}

type V1ListShortcutsResponseOutput struct{ *pulumi.OutputState }

func (V1ListShortcutsResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*V1ListShortcutsResponse)(nil)).Elem()
}

func (o V1ListShortcutsResponseOutput) ToV1ListShortcutsResponseOutput() V1ListShortcutsResponseOutput {
	return o
}

func (o V1ListShortcutsResponseOutput) ToV1ListShortcutsResponseOutputWithContext(ctx context.Context) V1ListShortcutsResponseOutput {
	return o
}

func (o V1ListShortcutsResponseOutput) Shortcuts() Apiv1ShortcutArrayOutput {
	return o.ApplyT(func(v V1ListShortcutsResponse) []Apiv1Shortcut { return v.Shortcuts }).(Apiv1ShortcutArrayOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*Apiv1OpenGraphMetadataInput)(nil)).Elem(), Apiv1OpenGraphMetadataArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*Apiv1OpenGraphMetadataPtrInput)(nil)).Elem(), Apiv1OpenGraphMetadataArgs{})
	pulumi.RegisterOutputType(Apiv1OpenGraphMetadataOutput{})
	pulumi.RegisterOutputType(Apiv1OpenGraphMetadataPtrOutput{})
	pulumi.RegisterOutputType(Apiv1ShortcutOutput{})
	pulumi.RegisterOutputType(Apiv1ShortcutPtrOutput{})
	pulumi.RegisterOutputType(Apiv1ShortcutArrayOutput{})
	pulumi.RegisterOutputType(V1GetShortcutResponseOutput{})
	pulumi.RegisterOutputType(V1ListShortcutsResponseOutput{})
}