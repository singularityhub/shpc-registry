---
layout: container
name:  "quay.io/biocontainers/scikit-learn"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/scikit-learn/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/scikit-learn/container.yaml"
updated_at: "2022-10-27 00:25:03.244498"
latest: "0.20.2"
container_url: "https://biocontainers.pro/tools/scikit-learn"

versions:
 - "0.20.2"
description: "shpc-registry automated BioContainers addition for scikit-learn"
config: {"url": "https://biocontainers.pro/tools/scikit-learn", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for scikit-learn", "latest": {"0.20.2": "sha256:a69a470e71d5823bf38b454b44743eceba694e6c38bab59d21ef38ccc53e20ed"}, "tags": {"0.20.2": "sha256:a69a470e71d5823bf38b454b44743eceba694e6c38bab59d21ef38ccc53e20ed"}, "docker": "quay.io/biocontainers/scikit-learn"}
---

This module is a singularity container wrapper for quay.io/biocontainers/scikit-learn.
shpc-registry automated BioContainers addition for scikit-learn
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/scikit-learn
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/scikit-learn:0.20.2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/scikit-learn/0.20.2
$ module help quay.io/biocontainers/scikit-learn/0.20.2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### scikit-learn-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### scikit-learn-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### scikit-learn-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### scikit-learn-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### scikit-learn-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### scikit-learn-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### scikit-learn

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