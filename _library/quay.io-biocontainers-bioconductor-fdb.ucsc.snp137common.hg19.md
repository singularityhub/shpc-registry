---
layout: container
name:  "quay.io/biocontainers/bioconductor-fdb.ucsc.snp137common.hg19"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fdb.ucsc.snp137common.hg19/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fdb.ucsc.snp137common.hg19/container.yaml"
updated_at: "2025-03-07 03:43:44.943159"
latest: "1.0.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-fdb.ucsc.snp137common.hg19"

versions:
 - "1.0.0--r41hdfd78af_9"
 - "1.0.0--r42hdfd78af_10"
 - "1.0.0--r43hdfd78af_11"
 - "1.0.0--r43hdfd78af_12"
 - "1.0.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-fdb.ucsc.snp137common.hg19"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fdb.ucsc.snp137common.hg19", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fdb.ucsc.snp137common.hg19", "latest": {"1.0.0--r44hdfd78af_13": "sha256:fa97ff035469b0f30750bda74b89ca1d1e3967a9fba4a4f75d5426f77d55f87e"}, "tags": {"1.0.0--r41hdfd78af_9": "sha256:604eb1278b8dd555b27888c93c4d9ca0ece8e999863b9f33f852a616340616d9", "1.0.0--r42hdfd78af_10": "sha256:76396c0a1c5a414d4e94b312a3b21cf48766541824a7b054c9d6d2506b272292", "1.0.0--r43hdfd78af_11": "sha256:bcde86ee9650f7c3ffbe9587d505d152e38ff9e6072d8e8afdacf95101a6f5cc", "1.0.0--r43hdfd78af_12": "sha256:5343ae03a9c094f84133101656e0fd85478be43e30a98286f1fdce41cbbb57ee", "1.0.0--r44hdfd78af_13": "sha256:fa97ff035469b0f30750bda74b89ca1d1e3967a9fba4a4f75d5426f77d55f87e"}, "docker": "quay.io/biocontainers/bioconductor-fdb.ucsc.snp137common.hg19"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fdb.ucsc.snp137common.hg19.
shpc-registry automated BioContainers addition for bioconductor-fdb.ucsc.snp137common.hg19
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fdb.ucsc.snp137common.hg19
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fdb.ucsc.snp137common.hg19:1.0.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fdb.ucsc.snp137common.hg19/1.0.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-fdb.ucsc.snp137common.hg19/1.0.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fdb.ucsc.snp137common.hg19-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fdb.ucsc.snp137common.hg19-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fdb.ucsc.snp137common.hg19-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fdb.ucsc.snp137common.hg19-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fdb.ucsc.snp137common.hg19-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fdb.ucsc.snp137common.hg19-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fdb.ucsc.snp137common.hg19

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