---
layout: container
name:  "quay.io/biocontainers/terminus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/terminus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/terminus/container.yaml"
updated_at: "2025-12-29 04:49:45.805563"
latest: "0.1.0--hff1259d_8"
container_url: "https://biocontainers.pro/tools/terminus"
aliases:
 - "terminus"
versions:
 - "v0.1.0--h2db0a6b_0"
 - "0.1.0--hbd16fde_5"
 - "0.1.0--h1c7ca24_7"
 - "0.1.0--hff1259d_8"
description: "shpc-registry automated BioContainers addition for terminus"
config: {"url": "https://biocontainers.pro/tools/terminus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for terminus", "latest": {"0.1.0--hff1259d_8": "sha256:915727887fa6bf2be9fe9162c8d38ccbba47e74e18ef0005c0f14b7fbc2d4ff4"}, "tags": {"v0.1.0--h2db0a6b_0": "sha256:d697cdff1ac8396bbe362e3436073c5bc850c3b79bb6d40cdba5fb9e5ee009fa", "0.1.0--hbd16fde_5": "sha256:8d8d1f377af0a5959e9b32ba53cff31a7aa3488f752456f873c5cdd9d4ad5558", "0.1.0--h1c7ca24_7": "sha256:e9efc616500cdc1f5d873396a19186bdde07ce58cdcb313e890c21b651c7bebc", "0.1.0--hff1259d_8": "sha256:915727887fa6bf2be9fe9162c8d38ccbba47e74e18ef0005c0f14b7fbc2d4ff4"}, "docker": "quay.io/biocontainers/terminus", "aliases": {"terminus": "/usr/local/bin/terminus"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/terminus.
shpc-registry automated BioContainers addition for terminus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/terminus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/terminus:0.1.0--hff1259d_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/terminus/0.1.0--hff1259d_8
$ module help quay.io/biocontainers/terminus/0.1.0--hff1259d_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### terminus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### terminus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### terminus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### terminus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### terminus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### terminus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### terminus

```bash
$ singularity exec <container> /usr/local/bin/terminus
$ podman run --it --rm --entrypoint /usr/local/bin/terminus   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/terminus   -v ${PWD} -w ${PWD} <container> -c " $@"
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