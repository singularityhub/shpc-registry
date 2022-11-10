---
layout: container
name:  "quay.io/biocontainers/r-gkmsvm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-gkmsvm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-gkmsvm/container.yaml"
updated_at: "2022-11-09 23:37:20.512758"
latest: "0.81.0--r41h87f3376_3"
container_url: "https://biocontainers.pro/tools/r-gkmsvm"

versions:
 - "0.81.0--r41h87f3376_3"
description: "shpc-registry automated BioContainers addition for r-gkmsvm"
config: {"url": "https://biocontainers.pro/tools/r-gkmsvm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-gkmsvm", "latest": {"0.81.0--r41h87f3376_3": "sha256:76bb60f5402414c4c95086be4cdcac98a2c8f73fbec887c37368a109fd5f06b4"}, "tags": {"0.81.0--r41h87f3376_3": "sha256:76bb60f5402414c4c95086be4cdcac98a2c8f73fbec887c37368a109fd5f06b4"}, "docker": "quay.io/biocontainers/r-gkmsvm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-gkmsvm.
shpc-registry automated BioContainers addition for r-gkmsvm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-gkmsvm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-gkmsvm:0.81.0--r41h87f3376_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-gkmsvm/0.81.0--r41h87f3376_3
$ module help quay.io/biocontainers/r-gkmsvm/0.81.0--r41h87f3376_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-gkmsvm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-gkmsvm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-gkmsvm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-gkmsvm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-gkmsvm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-gkmsvm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-gkmsvm

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