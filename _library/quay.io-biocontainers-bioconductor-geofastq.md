---
layout: container
name:  "quay.io/biocontainers/bioconductor-geofastq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geofastq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geofastq/container.yaml"
updated_at: "2025-12-09 03:43:35.008396"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geofastq"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geofastq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geofastq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geofastq", "latest": {"1.14.0--r44hdfd78af_0": "sha256:e89dbae86db38e855322aad43100351d8c67befe77e188da42122e3c4101ea15"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:68c4ad38c5f9db54280ff4d8088ec57fcf75db46ae2a841304137830244434b9", "1.6.0--r42hdfd78af_0": "sha256:7049934b64556a47a70c0be67aeb1543dfeb7808ee4d52662a2367e9e9b149d9", "1.8.0--r43hdfd78af_0": "sha256:f448ec4e228c7b7c5e2d20d630385df8702e91c38e476af56b22d1a16f364a22", "1.10.0--r43hdfd78af_0": "sha256:176cc320b571d297bff1ca9fb5fbadf87a720f63ba6e5b166f5e04aa71b5c540", "1.14.0--r44hdfd78af_0": "sha256:e89dbae86db38e855322aad43100351d8c67befe77e188da42122e3c4101ea15"}, "docker": "quay.io/biocontainers/bioconductor-geofastq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geofastq.
shpc-registry automated BioContainers addition for bioconductor-geofastq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geofastq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geofastq:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geofastq/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geofastq/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geofastq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geofastq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geofastq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geofastq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geofastq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geofastq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geofastq

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