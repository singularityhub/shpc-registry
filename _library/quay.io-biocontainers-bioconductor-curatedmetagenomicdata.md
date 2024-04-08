---
layout: container
name:  "quay.io/biocontainers/bioconductor-curatedmetagenomicdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-curatedmetagenomicdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-curatedmetagenomicdata/container.yaml"
updated_at: "2024-04-08 02:38:08.067444"
latest: "3.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-curatedmetagenomicdata"

versions:
 - "3.4.1--r41hdfd78af_0"
 - "3.6.0--r42hdfd78af_0"
 - "3.8.0--r43hdfd78af_0"
 - "3.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-curatedmetagenomicdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-curatedmetagenomicdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-curatedmetagenomicdata", "latest": {"3.10.0--r43hdfd78af_0": "sha256:baef849ee5f897bf0a5a0c9c0989f47b992178c3d2a6b30040716f987c1b1e29"}, "tags": {"3.4.1--r41hdfd78af_0": "sha256:d3c247b75974daf12767e546f3e13d3112804af86d2a7d045066e9644e11b28e", "3.6.0--r42hdfd78af_0": "sha256:6ac329afb9c6a44b1daad9de8f79bd4a3f950cf003f0aa41160cec7aa63b6b81", "3.8.0--r43hdfd78af_0": "sha256:d08710ffa4db2fa4869abb747a64d8425d9d2386e92988755b4af1b62c3a7fe8", "3.10.0--r43hdfd78af_0": "sha256:baef849ee5f897bf0a5a0c9c0989f47b992178c3d2a6b30040716f987c1b1e29"}, "docker": "quay.io/biocontainers/bioconductor-curatedmetagenomicdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-curatedmetagenomicdata.
shpc-registry automated BioContainers addition for bioconductor-curatedmetagenomicdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedmetagenomicdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedmetagenomicdata:3.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-curatedmetagenomicdata/3.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-curatedmetagenomicdata/3.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-curatedmetagenomicdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedmetagenomicdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedmetagenomicdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-curatedmetagenomicdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-curatedmetagenomicdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-curatedmetagenomicdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-curatedmetagenomicdata

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