---
layout: container
name:  "quay.io/biocontainers/perl-math-random"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/perl-math-random/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/perl-math-random/container.yaml"
updated_at: "2025-03-08 02:49:12.190283"
latest: "0.72--pl5321h7b50bb2_8"
container_url: "https://biocontainers.pro/tools/perl-math-random"

versions:
 - "0.72--pl5321hec16e2b_4"
 - "0.72--pl5321h031d066_6"
 - "0.72--pl5321h031d066_7"
 - "0.72--pl5321h7b50bb2_8"
description: "shpc-registry automated BioContainers addition for perl-math-random"
config: {"url": "https://biocontainers.pro/tools/perl-math-random", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for perl-math-random", "latest": {"0.72--pl5321h7b50bb2_8": "sha256:b31050c48d18b67abded63846a1b437fb2c9caf2a6c9f31f0519f61f16226e34"}, "tags": {"0.72--pl5321hec16e2b_4": "sha256:36ddf2b0c722a0d1648c7902092610da9ae7272c81cb54dadeebee9e7226ac5e", "0.72--pl5321h031d066_6": "sha256:33a3651b4b8bd52c513fb9a5dae04756e1744c219bcfabcdf8b2bc704c62a4ec", "0.72--pl5321h031d066_7": "sha256:a283ec1fbf0e76b303808291dc8ee12b41c3323579b5e1d67b1c6055f48f59b9", "0.72--pl5321h7b50bb2_8": "sha256:b31050c48d18b67abded63846a1b437fb2c9caf2a6c9f31f0519f61f16226e34"}, "docker": "quay.io/biocontainers/perl-math-random"}
---

This module is a singularity container wrapper for quay.io/biocontainers/perl-math-random.
shpc-registry automated BioContainers addition for perl-math-random
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/perl-math-random
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/perl-math-random:0.72--pl5321h7b50bb2_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/perl-math-random/0.72--pl5321h7b50bb2_8
$ module help quay.io/biocontainers/perl-math-random/0.72--pl5321h7b50bb2_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### perl-math-random-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### perl-math-random-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### perl-math-random-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### perl-math-random-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### perl-math-random-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### perl-math-random-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### perl-math-random

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