---
layout: container
name:  "quay.io/biocontainers/bioconductor-fdb.infiniummethylation.hg19"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fdb.infiniummethylation.hg19/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fdb.infiniummethylation.hg19/container.yaml"
updated_at: "2025-10-29 03:40:02.474455"
latest: "2.2.0--r44hdfd78af_17"
container_url: "https://biocontainers.pro/tools/bioconductor-fdb.infiniummethylation.hg19"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "2.2.0--r40_9"
 - "2.2.0--r42hdfd78af_14"
 - "2.2.0--r43hdfd78af_15"
 - "2.2.0--r43hdfd78af_16"
 - "2.2.0--r44hdfd78af_17"
description: "shpc-registry automated BioContainers addition for bioconductor-fdb.infiniummethylation.hg19"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fdb.infiniummethylation.hg19", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fdb.infiniummethylation.hg19", "latest": {"2.2.0--r44hdfd78af_17": "sha256:a0cdc821d914be4df042bd8f3c4fb9deb77c1786a989b30255036747831a9a61"}, "tags": {"2.2.0--r40_9": "sha256:ea7755e7af9c750995e6a07b7a2527ce79fb62e66c67037051c71d9279c40b8b", "2.2.0--r42hdfd78af_14": "sha256:cab4bf7374c9ebb80e5407bc8068f18c79bba90ff13c6ceb96e181195760e627", "2.2.0--r43hdfd78af_15": "sha256:0cd3f309b1aa9c5f4043eaa669102e3a52ead0a6c372ebeddfcdea8192e09500", "2.2.0--r43hdfd78af_16": "sha256:b7030ce8ec8f756572011dfe2a86c5e28871c7e007002d43f7a001707bcb1884", "2.2.0--r44hdfd78af_17": "sha256:a0cdc821d914be4df042bd8f3c4fb9deb77c1786a989b30255036747831a9a61"}, "docker": "quay.io/biocontainers/bioconductor-fdb.infiniummethylation.hg19", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fdb.infiniummethylation.hg19.
shpc-registry automated BioContainers addition for bioconductor-fdb.infiniummethylation.hg19
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fdb.infiniummethylation.hg19
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fdb.infiniummethylation.hg19:2.2.0--r44hdfd78af_17
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fdb.infiniummethylation.hg19/2.2.0--r44hdfd78af_17
$ module help quay.io/biocontainers/bioconductor-fdb.infiniummethylation.hg19/2.2.0--r44hdfd78af_17
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fdb.infiniummethylation.hg19-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fdb.infiniummethylation.hg19-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fdb.infiniummethylation.hg19-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fdb.infiniummethylation.hg19-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fdb.infiniummethylation.hg19-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fdb.infiniummethylation.hg19-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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