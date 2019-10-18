// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package packet

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides a Packet project SSH key resource to manage project-specific SSH keys.
// Project SSH keys will only be populated onto servers that belong to that project, in contrast to User SSH Keys.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-packet/blob/master/website/docs/r/project_ssh_key.html.markdown.
type ProjectSshKey struct {
	s *pulumi.ResourceState
}

// NewProjectSshKey registers a new resource with the given unique name, arguments, and options.
func NewProjectSshKey(ctx *pulumi.Context,
	name string, args *ProjectSshKeyArgs, opts ...pulumi.ResourceOpt) (*ProjectSshKey, error) {
	if args == nil || args.Name == nil {
		return nil, errors.New("missing required argument 'Name'")
	}
	if args == nil || args.ProjectId == nil {
		return nil, errors.New("missing required argument 'ProjectId'")
	}
	if args == nil || args.PublicKey == nil {
		return nil, errors.New("missing required argument 'PublicKey'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["name"] = nil
		inputs["projectId"] = nil
		inputs["publicKey"] = nil
	} else {
		inputs["name"] = args.Name
		inputs["projectId"] = args.ProjectId
		inputs["publicKey"] = args.PublicKey
	}
	inputs["created"] = nil
	inputs["fingerprint"] = nil
	inputs["updated"] = nil
	s, err := ctx.RegisterResource("packet:index/projectSshKey:ProjectSshKey", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ProjectSshKey{s: s}, nil
}

// GetProjectSshKey gets an existing ProjectSshKey resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetProjectSshKey(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ProjectSshKeyState, opts ...pulumi.ResourceOpt) (*ProjectSshKey, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["created"] = state.Created
		inputs["fingerprint"] = state.Fingerprint
		inputs["name"] = state.Name
		inputs["projectId"] = state.ProjectId
		inputs["publicKey"] = state.PublicKey
		inputs["updated"] = state.Updated
	}
	s, err := ctx.ReadResource("packet:index/projectSshKey:ProjectSshKey", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &ProjectSshKey{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *ProjectSshKey) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *ProjectSshKey) ID() *pulumi.IDOutput {
	return r.s.ID()
}

// The timestamp for when the SSH key was created
func (r *ProjectSshKey) Created() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["created"])
}

// The fingerprint of the SSH key
func (r *ProjectSshKey) Fingerprint() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["fingerprint"])
}

// The name of the SSH key for identification
func (r *ProjectSshKey) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

// The ID of parent project
func (r *ProjectSshKey) ProjectId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["projectId"])
}

// The public key. If this is a file, it can be read using the file interpolation function
func (r *ProjectSshKey) PublicKey() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["publicKey"])
}

// The timestamp for the last time the SSH key was updated
func (r *ProjectSshKey) Updated() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["updated"])
}

// Input properties used for looking up and filtering ProjectSshKey resources.
type ProjectSshKeyState struct {
	// The timestamp for when the SSH key was created
	Created interface{}
	// The fingerprint of the SSH key
	Fingerprint interface{}
	// The name of the SSH key for identification
	Name interface{}
	// The ID of parent project
	ProjectId interface{}
	// The public key. If this is a file, it can be read using the file interpolation function
	PublicKey interface{}
	// The timestamp for the last time the SSH key was updated
	Updated interface{}
}

// The set of arguments for constructing a ProjectSshKey resource.
type ProjectSshKeyArgs struct {
	// The name of the SSH key for identification
	Name interface{}
	// The ID of parent project
	ProjectId interface{}
	// The public key. If this is a file, it can be read using the file interpolation function
	PublicKey interface{}
}
