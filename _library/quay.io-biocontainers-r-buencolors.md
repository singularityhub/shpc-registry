---
layout: container
name:  "quay.io/biocontainers/r-buencolors"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-buencolors/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-buencolors/container.yaml"
updated_at: "2025-04-26 03:30:27.480282"
latest: "0.5.6--r44hdfd78af_1"
container_url: "https://biocontainers.pro/tools/r-buencolors"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "0.5.6--r43hdfd78af_0"
 - "0.5.6--r44hdfd78af_1"
description: "singularity registry hpc automated addition for r-buencolors"
config: {"url": "https://biocontainers.pro/tools/r-buencolors", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-buencolors", "latest": {"0.5.6--r44hdfd78af_1": "sha256:5e4676d8aedc6ea09806c2a0b2bfa3fe3154a41585de1e4d315946b255017236"}, "tags": {"0.5.6--r43hdfd78af_0": "sha256:88d7d0f064f2a11c05d6084c89521d30a24e732a610f917fcdcf67ed7e2c2196", "0.5.6--r44hdfd78af_1": "sha256:5e4676d8aedc6ea09806c2a0b2bfa3fe3154a41585de1e4d315946b255017236"}, "docker": "quay.io/biocontainers/r-buencolors", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-buencolors.
singularity registry hpc automated addition for r-buencolors
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-buencolors
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-buencolors:0.5.6--r44hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-buencolors/0.5.6--r44hdfd78af_1
$ module help quay.io/biocontainers/r-buencolors/0.5.6--r44hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-buencolors-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-buencolors-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-buencolors-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-buencolors-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-buencolors-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-buencolors-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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