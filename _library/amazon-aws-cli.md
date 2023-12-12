---
layout: container
name:  "amazon/aws-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/amazon/aws-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/amazon/aws-cli/container.yaml"
updated_at: "2023-12-12 03:14:24.834345"
latest: "amd64"
container_url: "https://hub.docker.com/r/amazon/aws-cli"
aliases:
 - "aws"
 - "aws_completer"
versions:
 - "2.13.0"
 - "2.12.7"
 - "amd64"
 - "2.13.15"
 - "2.13.24"
 - "2.13.32"
 - "2.14.5"
 - "2.13.39"
description: "The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services."
config: {"docker": "amazon/aws-cli", "url": "https://hub.docker.com/r/amazon/aws-cli", "maintainer": "@sarahbeecroft", "description": "The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services.", "latest": {"amd64": "sha256:6284c46b883c819477718de34719534f82195115730936ca7c571a8c56f39fbb"}, "tags": {"2.13.0": "sha256:7590866b360c488028f018e120da4394c799de08a8d8c1b09570cf720867bed5", "2.12.7": "sha256:93c39fb5fcf7b8269a7f1e3ee342f446f4c463abdbe924c79f4de2f959a03b3b", "amd64": "sha256:6284c46b883c819477718de34719534f82195115730936ca7c571a8c56f39fbb", "2.13.15": "sha256:ac2c7d3827a8fef1024357ada9c6ccd8d0ce098a85cffd6803a52bb8cb4842ed", "2.13.24": "sha256:e6ea5be1036e5f490fd4cd49cf0f7081eaf401a8dd978c524c28666b60a8c1b2", "2.13.32": "sha256:c59ac67975129e96448601b92d5a890cdfdaff0f175a3e4eb9cfa32b3995dca6", "2.14.5": "sha256:8da8ae14cd7b6ea8a90d352736bb5dbde1be4bb408b67877f8f4f0e02c3e13e3", "2.13.39": "sha256:4fe0a87257ba17fc214ed9b3f3456ecf5cb6b040d8873944908f9b020ca2e58c"}, "aliases": {"aws": "/usr/local/aws-cli/v2/current/bin/aws", "aws_completer": "/usr/local/aws-cli/v2/current/bin/aws_completer"}, "features": {"home": true}}
---

This module is a singularity container wrapper for amazon/aws-cli.
The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install amazon/aws-cli
```

Or a specific version:

```bash
$ shpc install amazon/aws-cli:amd64
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load amazon/aws-cli/amd64
$ module help amazon/aws-cli/amd64
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aws-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aws-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aws-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aws-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aws-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aws-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### aws

```bash
$ singularity exec <container> /usr/local/aws-cli/v2/current/bin/aws
$ podman run --it --rm --entrypoint /usr/local/aws-cli/v2/current/bin/aws   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/aws-cli/v2/current/bin/aws   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aws_completer

```bash
$ singularity exec <container> /usr/local/aws-cli/v2/current/bin/aws_completer
$ podman run --it --rm --entrypoint /usr/local/aws-cli/v2/current/bin/aws_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/aws-cli/v2/current/bin/aws_completer   -v ${PWD} -w ${PWD} <container> -c " $@"
```



In the above, the `<container>` directive will reference an actual container provided
by the module, for the version you have chosen to load. An environment file in the
module folder will also be bound. Note that although a container
might provide custom commands, every container exposes unique exec, shell, run, and
inspect aliases. For anycommands above, you can export:

 - SINGULARITY_OPTS: to define custom options for singularity (e.g., --debug)
 - SINGULARITY_COMMAND_OPTS: to define custom options for the command (e.g., -b)
 - PODMAN_OPTS: to define custom options for podman or docker
 - PODMAN_COMMAND_OPTS: to define custom options for the command

<br>

### Install

You can install shpc locally (for yourself or your user base) as follows:

```bash
$ git clone https://github.com/singularityhub/singularity-hpc
$ cd singularity-hpc
$ pip install -e .
```

Have any questions, or want to request a new module or version? [ask for help!](https://github.com/singularityhub/singularity-hpc/issues)