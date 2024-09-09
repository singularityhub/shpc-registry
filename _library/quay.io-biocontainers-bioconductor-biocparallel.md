---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocparallel"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocparallel/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocparallel/container.yaml"
updated_at: "2024-09-09 03:29:52.766923"
latest: "1.36.0--r43hf17093f_1"
container_url: "https://biocontainers.pro/tools/bioconductor-biocparallel"
aliases:
 - "uconv"
 - "tclsh8.5"
 - "wish8.5"
 - "ncursesw5-config"
versions:
 - "1.6.6--r3.3.2_1"
 - "1.32.0--r42hc247a5b_0"
 - "1.28.3--r41hc247a5b_1"
 - "1.26.0--r41h399db7b_0"
 - "1.24.1--r40h399db7b_0"
 - "1.22.0--r40h5f743cb_0"
 - "1.32.5--r42hc247a5b_0"
 - "1.32.5--r42hf17093f_1"
 - "1.34.2--r43hf17093f_0"
 - "1.36.0--r43hf17093f_1"
description: "shpc-registry automated BioContainers addition for bioconductor-biocparallel"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocparallel", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocparallel", "latest": {"1.36.0--r43hf17093f_1": "sha256:cc6be3d50f3e0573f5174c7385c0ab6ee238e41e230ce81c6627723e6eb3152c"}, "tags": {"1.6.6--r3.3.2_1": "sha256:364c3578ee80bc268c22a276ab3e0144c18148dd8caad3aa07fab9baa098fa5d", "1.32.0--r42hc247a5b_0": "sha256:fc6506a976c2dd81be58171b27539f8636113e4e482b3b11b18aecbff88c633f", "1.28.3--r41hc247a5b_1": "sha256:7f815d1e39b2671f182acf5cbac1d35a06521d66278f996677ec7efd5b0277be", "1.26.0--r41h399db7b_0": "sha256:fdb518100c163f37656a90e607a5291384f5c14d1b83b9dee457e017dba31fea", "1.24.1--r40h399db7b_0": "sha256:e21cfa187ba38b198518cafcf5b3b95092524b112519e87c09b24bda9a5c9ef5", "1.22.0--r40h5f743cb_0": "sha256:2c30b8605f6103459edc6b6dc12b977878c43cfb5dc7b4e9b5a41fd4651a94c1", "1.32.5--r42hc247a5b_0": "sha256:bd4d02f2aba30f918b56d0516b3808197192c460ed58ba9139e630fb320de88a", "1.32.5--r42hf17093f_1": "sha256:13644952e8fa6777cfea1b60da73660624d64c852998a03791c2c1e1fe06e2c8", "1.34.2--r43hf17093f_0": "sha256:43cb558f9ad5ec98ffab9f427a4822d8a3e03ccbbc261c566fc293e1f269d14e", "1.36.0--r43hf17093f_1": "sha256:cc6be3d50f3e0573f5174c7385c0ab6ee238e41e230ce81c6627723e6eb3152c"}, "docker": "quay.io/biocontainers/bioconductor-biocparallel", "aliases": {"uconv": "/usr/local/bin/uconv", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocparallel.
shpc-registry automated BioContainers addition for bioconductor-biocparallel
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocparallel
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocparallel:1.36.0--r43hf17093f_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocparallel/1.36.0--r43hf17093f_1
$ module help quay.io/biocontainers/bioconductor-biocparallel/1.36.0--r43hf17093f_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocparallel-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocparallel-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocparallel-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocparallel-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocparallel-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocparallel-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### uconv

```bash
$ singularity exec <container> /usr/local/bin/uconv
$ podman run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/uconv   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tclsh8.5

```bash
$ singularity exec <container> /usr/local/bin/tclsh8.5
$ podman run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tclsh8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wish8.5

```bash
$ singularity exec <container> /usr/local/bin/wish8.5
$ podman run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wish8.5   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncursesw5-config

```bash
$ singularity exec <container> /usr/local/bin/ncursesw5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncursesw5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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