---
layout: container
name:  "quay.io/biocontainers/r-genabel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-genabel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-genabel/container.yaml"
updated_at: "2023-08-28 09:33:52.971988"
latest: "1.8_0--r3.4.1_0"
container_url: "https://biocontainers.pro/tools/r-genabel"

versions:
 - "1.8_0--r3.4.1_0"
description: "shpc-registry automated BioContainers addition for r-genabel"
config: {"url": "https://biocontainers.pro/tools/r-genabel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-genabel", "latest": {"1.8_0--r3.4.1_0": "sha256:12912427939d966ea8793e6cd60431ee6e2704dafe510000f611239e5938445e"}, "tags": {"1.8_0--r3.4.1_0": "sha256:12912427939d966ea8793e6cd60431ee6e2704dafe510000f611239e5938445e"}, "docker": "quay.io/biocontainers/r-genabel"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-genabel.
shpc-registry automated BioContainers addition for r-genabel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-genabel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-genabel:1.8_0--r3.4.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-genabel/1.8_0--r3.4.1_0
$ module help quay.io/biocontainers/r-genabel/1.8_0--r3.4.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-genabel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-genabel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-genabel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-genabel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-genabel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-genabel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-genabel

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