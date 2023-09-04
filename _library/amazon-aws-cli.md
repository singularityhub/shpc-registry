---
layout: container
name:  "amazon/aws-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/amazon/aws-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/amazon/aws-cli/container.yaml"
updated_at: "2023-09-04 04:38:42.504656"
latest: "2.13.0"
container_url: "https://hub.docker.com/r/amazon/aws-cli"
aliases:
 - "aws"
 - "aws_completer"
versions:
 - "2.13.0"
 - "2.12.7"
description: "The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services."
config: {"docker": "amazon/aws-cli", "url": "https://hub.docker.com/r/amazon/aws-cli", "maintainer": "@sarahbeecroft", "description": "The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services.", "latest": {"2.13.0": "sha256:e119d71e8a39a6a3dec5f60f06b090dcdb7adb1b463ae6e9c1cb55d52a05d418"}, "tags": {"2.13.0": "sha256:e119d71e8a39a6a3dec5f60f06b090dcdb7adb1b463ae6e9c1cb55d52a05d418", "2.12.7": "sha256:3aaf7f14eba1d7bcae719e4e187a96682bdacd25b64b8c2bfd5d24bd34ac2376"}, "aliases": {"aws": "/usr/local/aws-cli/v2/current/bin/aws", "aws_completer": "/usr/local/aws-cli/v2/current/bin/aws_completer"}, "features": {"home": true}}
---

This module is a singularity container wrapper for amazon/aws-cli.
The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install amazon/aws-cli
```

Or a specific version:

```bash
$ shpc install amazon/aws-cli:2.13.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load amazon/aws-cli/2.13.0
$ module help amazon/aws-cli/2.13.0
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