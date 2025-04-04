---
layout: container
name:  "quay.io/biocontainers/bioconductor-mafdb.gnomad.r2.1.hs37d5"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mafdb.gnomad.r2.1.hs37d5/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mafdb.gnomad.r2.1.hs37d5/container.yaml"
updated_at: "2025-04-04 03:12:41.266143"
latest: "3.10.0--r41hdfd78af_6"
container_url: "https://biocontainers.pro/tools/bioconductor-mafdb.gnomad.r2.1.hs37d5"

versions:
 - "3.10.0--r41hdfd78af_6"
description: "shpc-registry automated BioContainers addition for bioconductor-mafdb.gnomad.r2.1.hs37d5"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mafdb.gnomad.r2.1.hs37d5", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mafdb.gnomad.r2.1.hs37d5", "latest": {"3.10.0--r41hdfd78af_6": "sha256:97da9d05420127019e86de4d1167a9299ded9b2ee3b108a54de4b6e8efed08aa"}, "tags": {"3.10.0--r41hdfd78af_6": "sha256:97da9d05420127019e86de4d1167a9299ded9b2ee3b108a54de4b6e8efed08aa"}, "docker": "quay.io/biocontainers/bioconductor-mafdb.gnomad.r2.1.hs37d5"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mafdb.gnomad.r2.1.hs37d5.
shpc-registry automated BioContainers addition for bioconductor-mafdb.gnomad.r2.1.hs37d5
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.gnomad.r2.1.hs37d5
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mafdb.gnomad.r2.1.hs37d5:3.10.0--r41hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mafdb.gnomad.r2.1.hs37d5/3.10.0--r41hdfd78af_6
$ module help quay.io/biocontainers/bioconductor-mafdb.gnomad.r2.1.hs37d5/3.10.0--r41hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mafdb.gnomad.r2.1.hs37d5-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.gnomad.r2.1.hs37d5-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mafdb.gnomad.r2.1.hs37d5-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mafdb.gnomad.r2.1.hs37d5-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mafdb.gnomad.r2.1.hs37d5-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mafdb.gnomad.r2.1.hs37d5-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mafdb.gnomad.r2.1.hs37d5

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