---
layout: container
name:  "quay.io/biocontainers/bioconductor-cancerdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cancerdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cancerdata/container.yaml"
updated_at: "2023-07-25 03:25:29.127381"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cancerdata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cancerdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cancerdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cancerdata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:85b4297264916ab7fdefdb74b993e2f13b7855f3f6e51bf0d68123fdb927d230"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:eef6b8e0c4624468dc57df979f4b5ecd6282514567067745abc880174b8bfd02", "1.36.0--r42hdfd78af_0": "sha256:ecd3d477b2376c6a15de20a20f8ffc13925dbd092de34478f8a33a827eb53cef", "1.38.0--r43hdfd78af_0": "sha256:85b4297264916ab7fdefdb74b993e2f13b7855f3f6e51bf0d68123fdb927d230"}, "docker": "quay.io/biocontainers/bioconductor-cancerdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cancerdata.
shpc-registry automated BioContainers addition for bioconductor-cancerdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cancerdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cancerdata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cancerdata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cancerdata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cancerdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cancerdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cancerdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cancerdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cancerdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cancerdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-cancerdata

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