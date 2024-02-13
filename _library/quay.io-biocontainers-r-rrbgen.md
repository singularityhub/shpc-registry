---
layout: container
name:  "quay.io/biocontainers/r-rrbgen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-rrbgen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-rrbgen/container.yaml"
updated_at: "2024-02-13 02:39:49.625193"
latest: "0.0.6--r43h4ac6f70_10"
container_url: "https://biocontainers.pro/tools/r-rrbgen"

versions:
 - "0.0.6--r41h9f5acd7_6"
 - "0.0.6--r42h9f5acd7_7"
 - "0.0.6--r42h4ac6f70_9"
 - "0.0.6--r43h4ac6f70_10"
description: "shpc-registry automated BioContainers addition for r-rrbgen"
config: {"url": "https://biocontainers.pro/tools/r-rrbgen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-rrbgen", "latest": {"0.0.6--r43h4ac6f70_10": "sha256:f31fab521895779d895c49ad4eff0fbe05d509a6a85fae8dbdefc82ba75d1a44"}, "tags": {"0.0.6--r41h9f5acd7_6": "sha256:484ac797fab2a3f76843f4123df2f791dd6d7f31921228ef095479d42474b2e3", "0.0.6--r42h9f5acd7_7": "sha256:1129cf324330c6a72a428d93bbb5f5a2b1183fbb46210c48da4e9a9394ac8785", "0.0.6--r42h4ac6f70_9": "sha256:1d97ea429ce18212a67ea44ac98ce1805b4b5b32801a98098bfa0d142e268516", "0.0.6--r43h4ac6f70_10": "sha256:f31fab521895779d895c49ad4eff0fbe05d509a6a85fae8dbdefc82ba75d1a44"}, "docker": "quay.io/biocontainers/r-rrbgen"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-rrbgen.
shpc-registry automated BioContainers addition for r-rrbgen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-rrbgen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-rrbgen:0.0.6--r43h4ac6f70_10
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-rrbgen/0.0.6--r43h4ac6f70_10
$ module help quay.io/biocontainers/r-rrbgen/0.0.6--r43h4ac6f70_10
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-rrbgen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-rrbgen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-rrbgen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-rrbgen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-rrbgen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-rrbgen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-rrbgen

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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