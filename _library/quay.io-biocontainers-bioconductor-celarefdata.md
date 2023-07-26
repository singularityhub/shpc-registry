---
layout: container
name:  "quay.io/biocontainers/bioconductor-celarefdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-celarefdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-celarefdata/container.yaml"
updated_at: "2023-07-26 02:58:29.461114"
latest: "1.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-celarefdata"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r40hdfd78af_1"
 - "1.15.0--r42hdfd78af_0"
 - "1.12.0--r41hdfd78af_1"
 - "1.10.0--r41hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-celarefdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-celarefdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-celarefdata", "latest": {"1.18.0--r43hdfd78af_0": "sha256:b476f61af84c0ac0d1e728ac4f4f1e91198dffe6ea0c182546e33399bbaa3b59"}, "tags": {"1.8.0--r40hdfd78af_1": "sha256:f839a2f6cfff34b5532027f010aadcfc2bc67c542cf0726cf280d1d0dfc3114e", "1.15.0--r42hdfd78af_0": "sha256:5b97d1ba0c5e65effc286ff43faeebdf622c401041d9282656e397e032c025e3", "1.12.0--r41hdfd78af_1": "sha256:9af9b6c2f423f8c18add71f549511edbafadc86411791dac0643bf4698245cc1", "1.10.0--r41hdfd78af_0": "sha256:d9989dccf9279ed7e1bd52617caa97e451c6289d6a6b7589c65e4086598392ba", "1.18.0--r43hdfd78af_0": "sha256:b476f61af84c0ac0d1e728ac4f4f1e91198dffe6ea0c182546e33399bbaa3b59"}, "docker": "quay.io/biocontainers/bioconductor-celarefdata", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-celarefdata.
shpc-registry automated BioContainers addition for bioconductor-celarefdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-celarefdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-celarefdata:1.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-celarefdata/1.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-celarefdata/1.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-celarefdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celarefdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-celarefdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-celarefdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-celarefdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-celarefdata-inspect-deffile:

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