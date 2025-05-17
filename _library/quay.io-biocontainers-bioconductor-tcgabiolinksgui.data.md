---
layout: container
name:  "quay.io/biocontainers/bioconductor-tcgabiolinksgui.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tcgabiolinksgui.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tcgabiolinksgui.data/container.yaml"
updated_at: "2025-05-17 03:13:17.482969"
latest: "1.26.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tcgabiolinksgui.data"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.2--r40_0"
 - "1.14.1--r41hdfd78af_0"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.18.0--r42hdfd78af_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
 - "1.26.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tcgabiolinksgui.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tcgabiolinksgui.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tcgabiolinksgui.data", "latest": {"1.26.0--r44hdfd78af_0": "sha256:d912856ffea8fbdc8853335d2be007895cf81495625ea078cc478b45e8367cd8"}, "tags": {"1.9.2--r40_0": "sha256:5204c72eec34329ae4e07c38db9684d986eb14f11cf71b21e63d3dfaa46db7e1", "1.14.1--r41hdfd78af_0": "sha256:673c5044cb349058d145e6feb6b002bcf5e2e56848a895a56e45556c84d060ee", "1.12.0--r41hdfd78af_0": "sha256:7d307cff0fd4b48ba9ea910120267512d15f7097bbc168a61392f170ce01d36e", "1.10.0--r40hdfd78af_1": "sha256:a5d9f50add8ccb4807ecabf9817eb81150e15161b78930ffeca6d44fc4d49c6d", "1.18.0--r42hdfd78af_0": "sha256:4637cf36fc6f6bf5a72d47b325b6bb698dca13cf33fa52c3359a5233ea8976f5", "1.17.0--r42hdfd78af_0": "sha256:e9a0224524e7fe8ba549bed9c50e0059cc47e600f787fc28fcb6f66b2c85352f", "1.20.0--r43hdfd78af_0": "sha256:4d69081deabfb8f98a529d2fc8d6fbea10d0c3922bf23a62f02af29262dbb597", "1.22.0--r43hdfd78af_0": "sha256:d8586b044ab1ccfba928b3b65bd55c1c5c5465879dca50904688909cbe3079cf", "1.26.0--r44hdfd78af_0": "sha256:d912856ffea8fbdc8853335d2be007895cf81495625ea078cc478b45e8367cd8"}, "docker": "quay.io/biocontainers/bioconductor-tcgabiolinksgui.data", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tcgabiolinksgui.data.
shpc-registry automated BioContainers addition for bioconductor-tcgabiolinksgui.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgabiolinksgui.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tcgabiolinksgui.data:1.26.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tcgabiolinksgui.data/1.26.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tcgabiolinksgui.data/1.26.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tcgabiolinksgui.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgabiolinksgui.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tcgabiolinksgui.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tcgabiolinksgui.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tcgabiolinksgui.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tcgabiolinksgui.data-inspect-deffile:

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