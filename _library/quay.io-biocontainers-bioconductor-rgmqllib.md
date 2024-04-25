---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgmqllib"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgmqllib/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgmqllib/container.yaml"
updated_at: "2024-04-25 02:40:30.096765"
latest: "1.22.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rgmqllib"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "1.9.0--r40_0"
 - "1.17.0--r42hdfd78af_0"
 - "1.14.0--r41hdfd78af_1"
 - "1.12.0--r41hdfd78af_0"
 - "1.10.0--r40hdfd78af_1"
 - "1.18.0--r42hdfd78af_0"
 - "1.20.0--r43hdfd78af_0"
 - "1.22.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rgmqllib"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgmqllib", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgmqllib", "latest": {"1.22.0--r43hdfd78af_0": "sha256:c43e0474cfa3836403e910548cf8e9af0a061eef35749712c1b3d424882bee37"}, "tags": {"1.9.0--r40_0": "sha256:be444842e11e228abb46f9e0ba7b5f68fcec86a5a4fe947c3e96bbf94eb89a74", "1.17.0--r42hdfd78af_0": "sha256:f29fe4f30d030496aceb87a2cd35bba6aaf8566bf5bff82f40f2ee32b3cebb19", "1.14.0--r41hdfd78af_1": "sha256:715deb6b0922f0dd304d4eaa08bbcf2700bf2e95deb8b1e2add0ef1b19dcd9f7", "1.12.0--r41hdfd78af_0": "sha256:24f08a40ff2288a6b45ed1a688f5d3efffe5290838896fb03268b1e456edb91d", "1.10.0--r40hdfd78af_1": "sha256:5f26aa8b22708be0aa82b2f7e81a83ac8f15492393c02a82b14b0da6e799c115", "1.18.0--r42hdfd78af_0": "sha256:fc079bd3f59114810f0c81fade76e679016ce0715cb7b446e8a5452648d7c101", "1.20.0--r43hdfd78af_0": "sha256:88f1db67081f8e67cdcc08b37a961714927896a9aa5c7fbc4161be0337fd8afe", "1.22.0--r43hdfd78af_0": "sha256:c43e0474cfa3836403e910548cf8e9af0a061eef35749712c1b3d424882bee37"}, "docker": "quay.io/biocontainers/bioconductor-rgmqllib", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgmqllib.
shpc-registry automated BioContainers addition for bioconductor-rgmqllib
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgmqllib
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgmqllib:1.22.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgmqllib/1.22.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rgmqllib/1.22.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgmqllib-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgmqllib-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgmqllib-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgmqllib-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgmqllib-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgmqllib-inspect-deffile:

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