---
layout: container
name:  "quay.io/biocontainers/bioconductor-antiprofilesdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-antiprofilesdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-antiprofilesdata/container.yaml"
updated_at: "2024-12-20 03:31:35.037089"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-antiprofilesdata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-antiprofilesdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-antiprofilesdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-antiprofilesdata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:eabf43e4baa26f9dbbf6662a0ebe03d1400a46a1813ead8a7b2bf728548e1c48"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:8fcff7fb0d5d9eb9f43d3237096d6637fed141a79c00f668b694f7bf01661cef", "1.34.0--r42hdfd78af_0": "sha256:300b6c5d51aae1097355815fa2076933dafc03028fcea432136fef3a2ecf1785", "1.36.0--r43hdfd78af_0": "sha256:5a7b23d21f34f9ddda72f9a4f6388c037362c8295a1a17649cb2a62345874f00", "1.38.0--r43hdfd78af_0": "sha256:eabf43e4baa26f9dbbf6662a0ebe03d1400a46a1813ead8a7b2bf728548e1c48"}, "docker": "quay.io/biocontainers/bioconductor-antiprofilesdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-antiprofilesdata.
shpc-registry automated BioContainers addition for bioconductor-antiprofilesdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-antiprofilesdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-antiprofilesdata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-antiprofilesdata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-antiprofilesdata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-antiprofilesdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-antiprofilesdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-antiprofilesdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-antiprofilesdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-antiprofilesdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-antiprofilesdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-antiprofilesdata

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