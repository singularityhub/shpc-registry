---
layout: container
name:  "quay.io/biocontainers/r-matlab"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-matlab/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/r-matlab/container.yaml"
updated_at: "2022-10-27 00:37:44.921420"
latest: "1.0.2--r3.3.2_0"
container_url: "https://biocontainers.pro/tools/r-matlab"

versions:
 - "1.0.2--r3.3.2_0"
description: "shpc-registry automated BioContainers addition for r-matlab"
config: {"url": "https://biocontainers.pro/tools/r-matlab", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-matlab", "latest": {"1.0.2--r3.3.2_0": "sha256:7d7211689481d64e02ffd88d361c5a32dc7836b89f48ea03732a9c6270d0c2e7"}, "tags": {"1.0.2--r3.3.2_0": "sha256:7d7211689481d64e02ffd88d361c5a32dc7836b89f48ea03732a9c6270d0c2e7"}, "docker": "quay.io/biocontainers/r-matlab"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-matlab.
shpc-registry automated BioContainers addition for r-matlab
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-matlab
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-matlab:1.0.2--r3.3.2_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-matlab/1.0.2--r3.3.2_0
$ module help quay.io/biocontainers/r-matlab/1.0.2--r3.3.2_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-matlab-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-matlab-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-matlab-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-matlab-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-matlab-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-matlab-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-matlab

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