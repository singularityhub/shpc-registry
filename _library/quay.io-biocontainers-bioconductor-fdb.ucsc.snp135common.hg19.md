---
layout: container
name:  "quay.io/biocontainers/bioconductor-fdb.ucsc.snp135common.hg19"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fdb.ucsc.snp135common.hg19/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fdb.ucsc.snp135common.hg19/container.yaml"
updated_at: "2023-09-25 03:06:51.930504"
latest: "1.0.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-fdb.ucsc.snp135common.hg19"

versions:
 - "1.0.0--r41hdfd78af_9"
 - "1.0.0--r42hdfd78af_10"
 - "1.0.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-fdb.ucsc.snp135common.hg19"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fdb.ucsc.snp135common.hg19", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fdb.ucsc.snp135common.hg19", "latest": {"1.0.0--r43hdfd78af_11": "sha256:ac53f40b1b1c08cf1c926019389ab6e36ebe3804500b123ed8878e2dd842819a"}, "tags": {"1.0.0--r41hdfd78af_9": "sha256:780422840664c5a2daa3f9fed1a1042e6443a34861db5eb769b849215dd5b3da", "1.0.0--r42hdfd78af_10": "sha256:5e7a589dbeaf5f71a5d97a7ff484bedfdc1c7553b742c5d4660b8c7c657539f6", "1.0.0--r43hdfd78af_11": "sha256:ac53f40b1b1c08cf1c926019389ab6e36ebe3804500b123ed8878e2dd842819a"}, "docker": "quay.io/biocontainers/bioconductor-fdb.ucsc.snp135common.hg19"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fdb.ucsc.snp135common.hg19.
shpc-registry automated BioContainers addition for bioconductor-fdb.ucsc.snp135common.hg19
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fdb.ucsc.snp135common.hg19
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fdb.ucsc.snp135common.hg19:1.0.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fdb.ucsc.snp135common.hg19/1.0.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-fdb.ucsc.snp135common.hg19/1.0.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fdb.ucsc.snp135common.hg19-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fdb.ucsc.snp135common.hg19-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fdb.ucsc.snp135common.hg19-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fdb.ucsc.snp135common.hg19-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fdb.ucsc.snp135common.hg19-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fdb.ucsc.snp135common.hg19-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fdb.ucsc.snp135common.hg19

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