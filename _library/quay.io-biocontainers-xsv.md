---
layout: container
name:  "quay.io/biocontainers/xsv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/xsv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/xsv/container.yaml"
updated_at: "2023-12-09 03:00:29.236779"
latest: "0.10.3--0"
container_url: "https://biocontainers.pro/tools/xsv"
aliases:
 - "xsv"
versions:
 - "0.9.8--0"
 - "0.10.3--0"
description: "shpc-registry automated BioContainers addition for xsv"
config: {"url": "https://biocontainers.pro/tools/xsv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for xsv", "latest": {"0.10.3--0": "sha256:3531553a778de8d442a25136a0a579f6bda4d61f8e1140a99bf4a3f2fd40d639"}, "tags": {"0.9.8--0": "sha256:2570fab538bce6762431f3abfd27e99b9f3de61b0e279bc4d1fbff53ecb8dbcb", "0.10.3--0": "sha256:3531553a778de8d442a25136a0a579f6bda4d61f8e1140a99bf4a3f2fd40d639"}, "docker": "quay.io/biocontainers/xsv", "aliases": {"xsv": "/usr/local/bin/xsv"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/xsv.
shpc-registry automated BioContainers addition for xsv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/xsv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/xsv:0.10.3--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/xsv/0.10.3--0
$ module help quay.io/biocontainers/xsv/0.10.3--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### xsv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### xsv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### xsv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### xsv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### xsv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### xsv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### xsv

```bash
$ singularity exec <container> /usr/local/bin/xsv
$ podman run --it --rm --entrypoint /usr/local/bin/xsv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsv   -v ${PWD} -w ${PWD} <container> -c " $@"
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