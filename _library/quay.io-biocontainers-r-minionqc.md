---
layout: container
name:  "quay.io/biocontainers/r-minionqc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-minionqc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-minionqc/container.yaml"
updated_at: "2024-07-31 02:17:52.941752"
latest: "1.4.2--r43hdfd78af_4"
container_url: "https://biocontainers.pro/tools/r-minionqc"
aliases:
 - "MinIONQC.R"
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.4.2--r41hdfd78af_2"
 - "1.4.2--r42hdfd78af_3"
 - "1.4.2--r43hdfd78af_4"
description: "shpc-registry automated BioContainers addition for r-minionqc"
config: {"url": "https://biocontainers.pro/tools/r-minionqc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-minionqc", "latest": {"1.4.2--r43hdfd78af_4": "sha256:4378201aab8adeda538754c91bafe349dbd6247c24bb7ce2b614f35921087ad1"}, "tags": {"1.4.2--r41hdfd78af_2": "sha256:8d3880d789076b195c107ec2c37c995e47d8f4b392b1157b9ec5fe5110fd455b", "1.4.2--r42hdfd78af_3": "sha256:739e9022bb4669c1dc689eb9e7100c290652424187a74a70c37b5d74c1baf0d8", "1.4.2--r43hdfd78af_4": "sha256:4378201aab8adeda538754c91bafe349dbd6247c24bb7ce2b614f35921087ad1"}, "docker": "quay.io/biocontainers/r-minionqc", "aliases": {"MinIONQC.R": "/usr/local/bin/MinIONQC.R", "x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-minionqc.
shpc-registry automated BioContainers addition for r-minionqc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-minionqc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-minionqc:1.4.2--r43hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-minionqc/1.4.2--r43hdfd78af_4
$ module help quay.io/biocontainers/r-minionqc/1.4.2--r43hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-minionqc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-minionqc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-minionqc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-minionqc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-minionqc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-minionqc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### MinIONQC.R

```bash
$ singularity exec <container> /usr/local/bin/MinIONQC.R
$ podman run --it --rm --entrypoint /usr/local/bin/MinIONQC.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/MinIONQC.R   -v ${PWD} -w ${PWD} <container> -c " $@"
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