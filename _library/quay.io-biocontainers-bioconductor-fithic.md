---
layout: container
name:  "quay.io/biocontainers/bioconductor-fithic"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fithic/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fithic/container.yaml"
updated_at: "2024-02-19 03:09:15.945400"
latest: "1.28.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fithic"
aliases:
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351hf484d3e_0"
 - "1.24.0--r42hc247a5b_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.16.0--r40h399db7b_1"
 - "1.14.0--r40h5f743cb_0"
 - "1.24.0--r42hf17093f_2"
 - "1.26.0--r43hf17093f_0"
 - "1.28.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fithic"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fithic", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fithic", "latest": {"1.28.0--r43hf17093f_0": "sha256:d69f38451c1473e773719794901adcc71b09454c50bc813ba7688330c21a8c0a"}, "tags": {"1.8.0--r351hf484d3e_0": "sha256:fdacd86bff25ae93ff36ed55acac886d5fbc93a084e12e4bd19aab9ed35176c1", "1.24.0--r42hc247a5b_0": "sha256:3023fd7844ea97769343c4ce5879006940b3f64ac66489db25f9a170d6b4813e", "1.20.0--r41hc247a5b_2": "sha256:7e88980c0dc939d0b08b17299b8272aa4d60e9cd81c7ddb95dc1c6bde475269c", "1.18.0--r41h399db7b_0": "sha256:7030bcca8e2dbf049f352023b4892ca6d6a096d2d4077a6ca2499e37bf6cf6c4", "1.16.0--r40h399db7b_1": "sha256:f40968c41e01fdda2b906d5236f266a3ba448dece5135a1fcaaa69bf231308d6", "1.14.0--r40h5f743cb_0": "sha256:d176950b2f934359a7d1d1593bcd2f0a7b2602c13eb3b785369813f209b0891d", "1.24.0--r42hf17093f_2": "sha256:7b885df90be9f0d076143108302256a5dc079ad8e3da121970f28e7a4b87e18b", "1.26.0--r43hf17093f_0": "sha256:36e0a49f7d5291fc0ca654931284ab71eb49b9a066afce9eca903a6322899322", "1.28.0--r43hf17093f_0": "sha256:d69f38451c1473e773719794901adcc71b09454c50bc813ba7688330c21a8c0a"}, "docker": "quay.io/biocontainers/bioconductor-fithic", "aliases": {"c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fithic.
shpc-registry automated BioContainers addition for bioconductor-fithic
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fithic
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fithic:1.28.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fithic/1.28.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-fithic/1.28.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fithic-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fithic-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fithic-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fithic-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fithic-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fithic-inspect-deffile:

```bash
$ singularity inspect -d <container>
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