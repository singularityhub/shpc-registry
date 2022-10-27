---
layout: container
name:  "quay.io/biocontainers/medusa-data-fusion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/medusa-data-fusion/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/medusa-data-fusion/container.yaml"
updated_at: "2022-10-27 00:59:44.586942"
latest: "0.1--pyh5ca1d4c_3"
container_url: "https://biocontainers.pro/tools/medusa-data-fusion"

versions:
 - "0.1--pyh5ca1d4c_3"
description: "shpc-registry automated BioContainers addition for medusa-data-fusion"
config: {"url": "https://biocontainers.pro/tools/medusa-data-fusion", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for medusa-data-fusion", "latest": {"0.1--pyh5ca1d4c_3": "sha256:8bee5762bb4972426f6ad99e314aa4981369e1f4c66fce23fd2eb0586747a00d"}, "tags": {"0.1--pyh5ca1d4c_3": "sha256:8bee5762bb4972426f6ad99e314aa4981369e1f4c66fce23fd2eb0586747a00d"}, "docker": "quay.io/biocontainers/medusa-data-fusion"}
---

This module is a singularity container wrapper for quay.io/biocontainers/medusa-data-fusion.
shpc-registry automated BioContainers addition for medusa-data-fusion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/medusa-data-fusion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/medusa-data-fusion:0.1--pyh5ca1d4c_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/medusa-data-fusion/0.1--pyh5ca1d4c_3
$ module help quay.io/biocontainers/medusa-data-fusion/0.1--pyh5ca1d4c_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### medusa-data-fusion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### medusa-data-fusion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### medusa-data-fusion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### medusa-data-fusion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### medusa-data-fusion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### medusa-data-fusion-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### medusa-data-fusion

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