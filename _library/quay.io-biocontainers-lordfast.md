---
layout: container
name:  "quay.io/biocontainers/lordfast"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/lordfast/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/lordfast/container.yaml"
updated_at: "2024-11-11 03:34:01.656196"
latest: "0.0.10--h43eeafb_5"
container_url: "https://biocontainers.pro/tools/lordfast"
aliases:
 - "lordfast"
versions:
 - "0.0.9--hd28b015_0"
 - "0.0.10--h5b5514e_3"
 - "0.0.10--h43eeafb_5"
description: "shpc-registry automated BioContainers addition for lordfast"
config: {"url": "https://biocontainers.pro/tools/lordfast", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for lordfast", "latest": {"0.0.10--h43eeafb_5": "sha256:8e0036bfafb534dd6e2229beff286f8a5b1681be3aed42f8a60a86f7018c8cbb"}, "tags": {"0.0.9--hd28b015_0": "sha256:b8244dd1a9c2d103ad16d570e3f19aea0fab209f56b3ca3b14d64f4c1f3a0443", "0.0.10--h5b5514e_3": "sha256:e1b28b25719bb5592bfa8d5918bb12729f9e8b368d94079c03ec27976bedb4dd", "0.0.10--h43eeafb_5": "sha256:8e0036bfafb534dd6e2229beff286f8a5b1681be3aed42f8a60a86f7018c8cbb"}, "docker": "quay.io/biocontainers/lordfast", "aliases": {"lordfast": "/usr/local/bin/lordfast"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/lordfast.
shpc-registry automated BioContainers addition for lordfast
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/lordfast
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/lordfast:0.0.10--h43eeafb_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/lordfast/0.0.10--h43eeafb_5
$ module help quay.io/biocontainers/lordfast/0.0.10--h43eeafb_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### lordfast-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### lordfast-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### lordfast-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### lordfast-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### lordfast-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### lordfast-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lordfast

```bash
$ singularity exec <container> /usr/local/bin/lordfast
$ podman run --it --rm --entrypoint /usr/local/bin/lordfast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lordfast   -v ${PWD} -w ${PWD} <container> -c " $@"
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