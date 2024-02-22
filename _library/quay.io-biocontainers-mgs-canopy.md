---
layout: container
name:  "quay.io/biocontainers/mgs-canopy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mgs-canopy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mgs-canopy/container.yaml"
updated_at: "2024-02-22 03:21:17.793086"
latest: "1.0--h376f1d3_7"
container_url: "https://biocontainers.pro/tools/mgs-canopy"
aliases:
 - "canopy"
 - "cc.bin"
versions:
 - "1.0--h2df963e_5"
 - "1.0--h376f1d3_7"
description: "shpc-registry automated BioContainers addition for mgs-canopy"
config: {"url": "https://biocontainers.pro/tools/mgs-canopy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mgs-canopy", "latest": {"1.0--h376f1d3_7": "sha256:2a504f4d7a4de5883b4d214d4d40982b81b02295a682e33f5c203dc7520b7db3"}, "tags": {"1.0--h2df963e_5": "sha256:82a47c5bf181cd458fda6ff66ddf6e735aa3e1b9f130a90f963f959be1f6d37c", "1.0--h376f1d3_7": "sha256:2a504f4d7a4de5883b4d214d4d40982b81b02295a682e33f5c203dc7520b7db3"}, "docker": "quay.io/biocontainers/mgs-canopy", "aliases": {"canopy": "/usr/local/bin/canopy", "cc.bin": "/usr/local/bin/cc.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mgs-canopy.
shpc-registry automated BioContainers addition for mgs-canopy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mgs-canopy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mgs-canopy:1.0--h376f1d3_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mgs-canopy/1.0--h376f1d3_7
$ module help quay.io/biocontainers/mgs-canopy/1.0--h376f1d3_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mgs-canopy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mgs-canopy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mgs-canopy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mgs-canopy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mgs-canopy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mgs-canopy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### canopy

```bash
$ singularity exec <container> /usr/local/bin/canopy
$ podman run --it --rm --entrypoint /usr/local/bin/canopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/canopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cc.bin

```bash
$ singularity exec <container> /usr/local/bin/cc.bin
$ podman run --it --rm --entrypoint /usr/local/bin/cc.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cc.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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