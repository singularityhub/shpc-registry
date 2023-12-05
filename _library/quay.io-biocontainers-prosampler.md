---
layout: container
name:  "quay.io/biocontainers/prosampler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/prosampler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/prosampler/container.yaml"
updated_at: "2023-12-05 03:11:02.908268"
latest: "1.0--hc9558a2_0"
container_url: "https://biocontainers.pro/tools/prosampler"
aliases:
 - "ProSampler"
versions:
 - "1.0--hc9558a2_0"
description: "shpc-registry automated BioContainers addition for prosampler"
config: {"url": "https://biocontainers.pro/tools/prosampler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for prosampler", "latest": {"1.0--hc9558a2_0": "sha256:ba843787293490ba6ddfd410cb51331966095f4013ce845bdc308fb4183b1a0a"}, "tags": {"1.0--hc9558a2_0": "sha256:ba843787293490ba6ddfd410cb51331966095f4013ce845bdc308fb4183b1a0a"}, "docker": "quay.io/biocontainers/prosampler", "aliases": {"ProSampler": "/usr/local/bin/ProSampler"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/prosampler.
shpc-registry automated BioContainers addition for prosampler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/prosampler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/prosampler:1.0--hc9558a2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/prosampler/1.0--hc9558a2_0
$ module help quay.io/biocontainers/prosampler/1.0--hc9558a2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### prosampler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### prosampler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### prosampler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### prosampler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### prosampler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### prosampler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ProSampler

```bash
$ singularity exec <container> /usr/local/bin/ProSampler
$ podman run --it --rm --entrypoint /usr/local/bin/ProSampler   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ProSampler   -v ${PWD} -w ${PWD} <container> -c " $@"
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