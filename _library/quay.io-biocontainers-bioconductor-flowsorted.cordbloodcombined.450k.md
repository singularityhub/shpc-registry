---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowsorted.cordbloodcombined.450k"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowsorted.cordbloodcombined.450k/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowsorted.cordbloodcombined.450k/container.yaml"
updated_at: "2023-08-18 02:51:43.390175"
latest: "1.16.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowsorted.cordbloodcombined.450k"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.16.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowsorted.cordbloodcombined.450k"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowsorted.cordbloodcombined.450k", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowsorted.cordbloodcombined.450k", "latest": {"1.16.0--r43hdfd78af_0": "sha256:0ff4ab3862dbd141adab49415c5fec8a0d99cc716989eb3466fc02a24cb5e218"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:6bc0021db4dc576e58cec8d50ec1f00f52c4012d2e9e6a05a671da1f6fed14be", "1.14.0--r42hdfd78af_0": "sha256:202ef62ecf328e89b5f3373719fc47d6700361ad670567bded2707ada5cc21cb", "1.10.0--r41hdfd78af_1": "sha256:9d09ef880e256f499f4f1d0d0ffb2f0e3c1c3e162d9dc88dc6f92fddb3f00b73", "1.16.0--r43hdfd78af_0": "sha256:0ff4ab3862dbd141adab49415c5fec8a0d99cc716989eb3466fc02a24cb5e218"}, "docker": "quay.io/biocontainers/bioconductor-flowsorted.cordbloodcombined.450k", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowsorted.cordbloodcombined.450k.
shpc-registry automated BioContainers addition for bioconductor-flowsorted.cordbloodcombined.450k
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowsorted.cordbloodcombined.450k
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowsorted.cordbloodcombined.450k:1.16.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowsorted.cordbloodcombined.450k/1.16.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowsorted.cordbloodcombined.450k/1.16.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowsorted.cordbloodcombined.450k-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowsorted.cordbloodcombined.450k-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowsorted.cordbloodcombined.450k-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowsorted.cordbloodcombined.450k-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowsorted.cordbloodcombined.450k-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowsorted.cordbloodcombined.450k-inspect-deffile:

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