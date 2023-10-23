---
layout: container
name:  "quay.io/biocontainers/svim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svim/container.yaml"
updated_at: "2023-10-23 03:10:36.379045"
latest: "2.0.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/svim"

versions:
 - "1.4.2--py_0"
 - "2.0.0--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for svim"
config: {"url": "https://biocontainers.pro/tools/svim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for svim", "latest": {"2.0.0--pyhdfd78af_0": "sha256:6951593cb962541603943f470225f9e6a770dfd3ae67e7d5d6392c5e797224f3"}, "tags": {"1.4.2--py_0": "sha256:67ad426e01eb0b16c92551a45086d2d25595ff8b82b97a5caac58aa6009a196c", "2.0.0--pyhdfd78af_0": "sha256:6951593cb962541603943f470225f9e6a770dfd3ae67e7d5d6392c5e797224f3"}, "docker": "quay.io/biocontainers/svim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/svim.
shpc-registry automated BioContainers addition for svim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svim:2.0.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svim/2.0.0--pyhdfd78af_0
$ module help quay.io/biocontainers/svim/2.0.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### svim

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