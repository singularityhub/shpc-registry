---
layout: container
name:  "quay.io/biocontainers/r-xmlrpc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-xmlrpc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-xmlrpc/container.yaml"
updated_at: "2025-01-19 03:09:45.650042"
latest: "0.2_4--r44h9ee0642_8"
container_url: "https://biocontainers.pro/tools/r-xmlrpc"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.2_4--r41h9ee0642_5"
 - "0.2_4--r42h9ee0642_6"
 - "0.2_4--r43h9ee0642_7"
 - "0.2_4--r44h9ee0642_8"
description: "shpc-registry automated BioContainers addition for r-xmlrpc"
config: {"url": "https://biocontainers.pro/tools/r-xmlrpc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-xmlrpc", "latest": {"0.2_4--r44h9ee0642_8": "sha256:3a2ffe323746bfd337faa68cebc586d4606418accf453d2175bfaddfcf2bfdb5"}, "tags": {"0.2_4--r41h9ee0642_5": "sha256:188f1c730cfccd39953522ea81c197695839a63d4b884d79b438647a213ba4ca", "0.2_4--r42h9ee0642_6": "sha256:0a7a24ef9dd26c28cb6dcd7435ad5d0b16e7e52ef74526065a151f155cc00342", "0.2_4--r43h9ee0642_7": "sha256:2848373f9732da6f8c7779f18e737a950243eaca85c026fafe60cfcd8d6ecbc0", "0.2_4--r44h9ee0642_8": "sha256:3a2ffe323746bfd337faa68cebc586d4606418accf453d2175bfaddfcf2bfdb5"}, "docker": "quay.io/biocontainers/r-xmlrpc", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-xmlrpc.
shpc-registry automated BioContainers addition for r-xmlrpc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-xmlrpc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-xmlrpc:0.2_4--r44h9ee0642_8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-xmlrpc/0.2_4--r44h9ee0642_8
$ module help quay.io/biocontainers/r-xmlrpc/0.2_4--r44h9ee0642_8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-xmlrpc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-xmlrpc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-xmlrpc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-xmlrpc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-xmlrpc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-xmlrpc-inspect-deffile:

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