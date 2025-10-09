---
layout: container
name:  "quay.io/biocontainers/r-soap-nmr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-soap-nmr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-soap-nmr/container.yaml"
updated_at: "2025-10-09 04:41:37.830107"
latest: "0.1.0.20170207--r44h9ee0642_7"
container_url: "https://biocontainers.pro/tools/r-soap-nmr"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.1.0.20170207--r41h9ee0642_4"
 - "0.1.0.20170207--r42h9ee0642_5"
 - "0.1.0.20170207--r43h9ee0642_6"
 - "0.1.0.20170207--r44h9ee0642_7"
description: "shpc-registry automated BioContainers addition for r-soap-nmr"
config: {"url": "https://biocontainers.pro/tools/r-soap-nmr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-soap-nmr", "latest": {"0.1.0.20170207--r44h9ee0642_7": "sha256:a5147e714dce7f4e1879549dd15d937c14e9f8d4d27ab253e7cbe2d457c6f284"}, "tags": {"0.1.0.20170207--r41h9ee0642_4": "sha256:0e164ad2d89248f0a58ca02d0a8af14747632a257907f67bccbf50f0b0328ef2", "0.1.0.20170207--r42h9ee0642_5": "sha256:b49664587cb2dd6633baa50a54ffff232fe2b59a4cbebf17a8c16057752fa986", "0.1.0.20170207--r43h9ee0642_6": "sha256:58f713d1be9c18e32145ad1d41bdc0ed7f364029941f7d63ec351641cfa9379d", "0.1.0.20170207--r44h9ee0642_7": "sha256:a5147e714dce7f4e1879549dd15d937c14e9f8d4d27ab253e7cbe2d457c6f284"}, "docker": "quay.io/biocontainers/r-soap-nmr", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-soap-nmr.
shpc-registry automated BioContainers addition for r-soap-nmr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-soap-nmr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-soap-nmr:0.1.0.20170207--r44h9ee0642_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-soap-nmr/0.1.0.20170207--r44h9ee0642_7
$ module help quay.io/biocontainers/r-soap-nmr/0.1.0.20170207--r44h9ee0642_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-soap-nmr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-soap-nmr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-soap-nmr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-soap-nmr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-soap-nmr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-soap-nmr-inspect-deffile:

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