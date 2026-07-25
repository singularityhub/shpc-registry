---
layout: container
name:  "quay.io/biocontainers/sam-subsampler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sam-subsampler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sam-subsampler/container.yaml"
updated_at: "2026-07-25 07:16:07.056347"
latest: "0.1.0--hf71e60c_0"
container_url: "https://biocontainers.pro/tools/sam-subsampler"
aliases:
 - "sam-subsampler"
versions:
 - "0.1.0--hf71e60c_0"
description: "singularity registry hpc automated addition for sam-subsampler"
config: {"url": "https://biocontainers.pro/tools/sam-subsampler", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for sam-subsampler", "latest": {"0.1.0--hf71e60c_0": "sha256:637ad49a88c0912418640b286ae958b0a87fd736e4370e11b5879cf3f3de6011"}, "tags": {"0.1.0--hf71e60c_0": "sha256:637ad49a88c0912418640b286ae958b0a87fd736e4370e11b5879cf3f3de6011"}, "docker": "quay.io/biocontainers/sam-subsampler", "aliases": {"sam-subsampler": "/usr/local/bin/sam-subsampler"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sam-subsampler.
singularity registry hpc automated addition for sam-subsampler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sam-subsampler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sam-subsampler:0.1.0--hf71e60c_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sam-subsampler/0.1.0--hf71e60c_0
$ module help quay.io/biocontainers/sam-subsampler/0.1.0--hf71e60c_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sam-subsampler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sam-subsampler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sam-subsampler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sam-subsampler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sam-subsampler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sam-subsampler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sam-subsampler

```bash
$ singularity exec <container> /usr/local/bin/sam-subsampler
$ podman run --it --rm --entrypoint /usr/local/bin/sam-subsampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sam-subsampler   -v ${PWD} -w ${PWD} <container> -c " $@"
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