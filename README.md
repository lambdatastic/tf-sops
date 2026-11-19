# tf-sops

## WARNING
This program is experimental, and you should back up your state files before trying to set up this tool. A bad SOPS config will mess up your state, and the author has not verified support for attended encryption.

## Description
`tf-sops` is a small program that lets Terraform / OpenTofu use SOPS to encrypt plan and state files at rest.

## Installation
Before setting up tf-sops in a project, make sure that you can already encrypt standard files with SOPS.

Once that's done, clone this repo and install it using `pipx install .`

If `tf-sops` is now in your path, you can use the [Tofu guide to enable encryption](https://opentofu.org/docs/language/state/encryption/#migrating-from-an-unencrypted-stateplan)

## Credits

This script is a modification of the [OpenTofu python example](https://github.com/opentofu/opentofu/blob/v1.13.9/website/docs/language/state/examples/encryption/external-method/method-external-method.py)
