---
layout: container
name:  "quay.io/biocontainers/bioconductor-worm.db0"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-worm.db0/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-worm.db0/container.yaml"
updated_at: "2024-08-24 02:40:20.400144"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-worm.db0"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.0--r40hdfd78af_1"
 - "3.11.2--r40_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-worm.db0"
config: {"url": "https://biocontainers.pro/tools/bioconductor-worm.db0", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-worm.db0", "latest": {"3.18.0--r43hdfd78af_0": "sha256:5cffff4a039aaca9cd317a159516f76258f6de3596c6c55c9eae4c3b7c1ebcca"}, "tags": {"3.8.2--r36_1": "sha256:d6e14fe868384ff78e083d6a670c24ffa2c8cd28a3c0faab4aed6cbb3227830c", "3.16.0--r42hdfd78af_0": "sha256:d00ac48e7110b69e50891df5f59f70adc070cc3107738c7da97c3bbd3ce3d6e2", "3.14.0--r41hdfd78af_1": "sha256:5754ca5c09fda1183f6a257b557499bded9fc548a71f4ba2c9bc46f88e9a6ca8", "3.13.0--r41hdfd78af_0": "sha256:d63243ae318b444e325043e91fee191d80b121d845e643eb25f1ae397f37f662", "3.12.0--r40hdfd78af_1": "sha256:077f674121ed47a63158b5969277f3d1e74eaf82fb51a784fcc2918fdfcf8f0f", "3.11.2--r40_0": "sha256:0de158937caa4715b7b5fa1932a294ba72dfb1d795279cc7b25e69fa912662bb", "3.17.0--r43hdfd78af_0": "sha256:b541e50e45021cc7abcc8fa770a0c55101923115cccc8c20f25d6cabf44e4685", "3.18.0--r43hdfd78af_0": "sha256:5cffff4a039aaca9cd317a159516f76258f6de3596c6c55c9eae4c3b7c1ebcca"}, "docker": "quay.io/biocontainers/bioconductor-worm.db0", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-worm.db0.
shpc-registry automated BioContainers addition for bioconductor-worm.db0
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-worm.db0
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-worm.db0:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-worm.db0/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-worm.db0/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-worm.db0-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-worm.db0-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-worm.db0-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-worm.db0-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-worm.db0-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-worm.db0-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gio-launch-desktop

```bash
$ singularity exec <container> /usr/local/bin/gio-launch-desktop
$ podman run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gio-launch-desktop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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