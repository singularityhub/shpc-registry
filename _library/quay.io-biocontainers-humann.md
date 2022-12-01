---
layout: container
name:  "quay.io/biocontainers/humann"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/humann/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/humann/container.yaml"
updated_at: "2022-12-01 02:30:58.026684"
latest: "3.6--pyh7cba7a3_0"
container_url: "https://biocontainers.pro/tools/humann"

versions:
 - "3.6--pyh7cba7a3_0"
description: "shpc-registry automated BioContainers addition for humann"
config: {"url": "https://biocontainers.pro/tools/humann", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for humann", "latest": {"3.6--pyh7cba7a3_0": "sha256:7b9093898aa115471daf054d4baf0aa4ab4d1af39d077812f7445d5b3fd766f0"}, "tags": {"3.6--pyh7cba7a3_0": "sha256:7b9093898aa115471daf054d4baf0aa4ab4d1af39d077812f7445d5b3fd766f0"}, "docker": "quay.io/biocontainers/humann"}
---

This module is a singularity container wrapper for quay.io/biocontainers/humann.
shpc-registry automated BioContainers addition for humann
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/humann
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/humann:3.6--pyh7cba7a3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/humann/3.6--pyh7cba7a3_0
$ module help quay.io/biocontainers/humann/3.6--pyh7cba7a3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### humann-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### humann-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### humann-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### humann-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### humann-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### humann-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### humann

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