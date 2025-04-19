---
layout: container
name:  "quay.io/biocontainers/bioconductor-bodymaprat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bodymaprat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bodymaprat/container.yaml"
updated_at: "2025-04-19 03:07:58.221141"
latest: "1.22.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bodymaprat"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.8.0--r41hdfd78af_0"
 - "1.14.0--r42hdfd78af_0"
 - "1.10.0--r41hdfd78af_1"
 - "1.16.0--r43hdfd78af_0"
 - "1.18.0--r43hdfd78af_0"
 - "1.22.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bodymaprat"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bodymaprat", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bodymaprat", "latest": {"1.22.0--r44hdfd78af_0": "sha256:987d89fbe50fa36b86f6445a65d774652e39e1546ca3a5a821b860cdf8736675"}, "tags": {"1.8.0--r41hdfd78af_0": "sha256:cbb2f7b43b236016763c592cb69fed230499b0d3d6332ebfc0f55d2778fa0f04", "1.14.0--r42hdfd78af_0": "sha256:3f4cf9bc86a6b185d62ecfcc6fa77caf76d0908e507b27b4fc8ee048a7b35beb", "1.10.0--r41hdfd78af_1": "sha256:f80413521129380d75e81ef28e526dbaf35981c4800e7db9167e996cabe6304f", "1.16.0--r43hdfd78af_0": "sha256:5e42d5424863a1f10ca7cf6a0995a6775e7bbadd4ef9959da630b26bb321fe16", "1.18.0--r43hdfd78af_0": "sha256:78ffc81df3139acc451c2a0cde5350bd2ca0345da3f34e5b1eb591da9e270e05", "1.22.0--r44hdfd78af_0": "sha256:987d89fbe50fa36b86f6445a65d774652e39e1546ca3a5a821b860cdf8736675"}, "docker": "quay.io/biocontainers/bioconductor-bodymaprat", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bodymaprat.
shpc-registry automated BioContainers addition for bioconductor-bodymaprat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bodymaprat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bodymaprat:1.22.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bodymaprat/1.22.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bodymaprat/1.22.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bodymaprat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bodymaprat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bodymaprat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bodymaprat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bodymaprat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bodymaprat-inspect-deffile:

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