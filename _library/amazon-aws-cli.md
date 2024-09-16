---
layout: container
name:  "amazon/aws-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/amazon/aws-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/amazon/aws-cli/container.yaml"
updated_at: "2024-09-16 02:54:13.160875"
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
 - "2.15.7"
 - "2.14.6"
 - "2.15.17"
 - "2.15.25"
 - "2.15.35"
 - "2.15.44"
 - "2.16.1"
 - "2.15.62"
 - "2.17.8"
 - "2.16.12"
 - "2.17.22"
 - "2.17.44"
description: "The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services."
config: {"docker": "amazon/aws-cli", "url": "https://hub.docker.com/r/amazon/aws-cli", "maintainer": "@sarahbeecroft", "description": "The AWS Command Line Interface (AWS CLI) is a unified tool to manage your AWS services.", "latest": {"amd64": "sha256:7eabe3c1a03ed262759429e5ce5651379106a9e32bef98dc298d8b7c861987f4"}, "tags": {"2.13.0": "sha256:7590866b360c488028f018e120da4394c799de08a8d8c1b09570cf720867bed5", "2.12.7": "sha256:93c39fb5fcf7b8269a7f1e3ee342f446f4c463abdbe924c79f4de2f959a03b3b", "amd64": "sha256:7eabe3c1a03ed262759429e5ce5651379106a9e32bef98dc298d8b7c861987f4", "2.13.15": "sha256:ac2c7d3827a8fef1024357ada9c6ccd8d0ce098a85cffd6803a52bb8cb4842ed", "2.13.24": "sha256:e6ea5be1036e5f490fd4cd49cf0f7081eaf401a8dd978c524c28666b60a8c1b2", "2.13.32": "sha256:c59ac67975129e96448601b92d5a890cdfdaff0f175a3e4eb9cfa32b3995dca6", "2.14.5": "sha256:8da8ae14cd7b6ea8a90d352736bb5dbde1be4bb408b67877f8f4f0e02c3e13e3", "2.13.39": "sha256:4fe0a87257ba17fc214ed9b3f3456ecf5cb6b040d8873944908f9b020ca2e58c", "2.15.7": "sha256:07cc353f732a986c45ee0a8082c56442ade50b114f668df6af97b1b156916e5a", "2.14.6": "sha256:7a3f926997cfafa1cf737d5250a1b9040ffc902a632516f0e6a80c7828495482", "2.15.17": "sha256:a0c252c1822e1e484dcb4025ac4a6f765007b7b4ea57db1f09ada597e093df5c", "2.15.25": "sha256:16c5a4e1022a04208561d571b36615fe207e56c725b0d83f60b63729783f4415", "2.15.35": "sha256:9d1582256677c240d1f735b4ff4cc407c0596dccffa713fc405186794fab8139", "2.15.44": "sha256:1ace13eeb6eb414b1196811e59122b4705bd196479d29a80529ea4c837fce9ad", "2.16.1": "sha256:4da43fad4f528f45a63a8bce054bbc39cd417be9fb397cfd0535f16ccd6c1a8c", "2.15.62": "sha256:2cf6c1ad8ebfe2010c36bc2acb16217a2b2e6e5aabc474b6a2027bd885d93ea1", "2.17.8": "sha256:8b7517a6519843174c8759666ce3abd112e7b7a711c58ca9b164216100737f9f", "2.16.12": "sha256:0d9ab2b67b11a1958fa731459e37e9cd0f99457e24a1a2a972b7b163fc41901c", "2.17.22": "sha256:d384a7fb1e23d15d757fcdbfc188c7e4c2e0dae767713170505bdb57ca421510", "2.17.44": "sha256:f2094b8092475b7dae06fbec228bcd25ad24206f5b4fdce5b81bfe2a4b381892"}, "aliases": {"aws": "/usr/local/aws-cli/v2/current/bin/aws", "aws_completer": "/usr/local/aws-cli/v2/current/bin/aws_completer"}, "features": {"home": true}}
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