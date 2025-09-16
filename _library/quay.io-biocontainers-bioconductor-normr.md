---
layout: container
name:  "quay.io/biocontainers/bioconductor-normr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-normr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-normr/container.yaml"
updated_at: "2025-09-16 04:03:07.689393"
latest: "1.32.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-normr"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351hf484d3e_0"
 - "1.24.0--r42hc247a5b_0"
 - "1.20.0--r41hc247a5b_2"
 - "1.18.0--r41h399db7b_0"
 - "1.16.0--r40h399db7b_1"
 - "1.14.0--r40h5f743cb_0"
 - "1.24.0--r42hf17093f_1"
 - "1.26.0--r43hf17093f_0"
 - "1.28.0--r43hf17093f_0"
 - "1.32.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-normr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-normr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-normr", "latest": {"1.32.0--r44he5774e6_0": "sha256:fb21032ae5ddcba2eac607ca33e68ea42a7c577b1fdf9966af2bb829284be646"}, "tags": {"1.8.0--r351hf484d3e_0": "sha256:6e3a60a5534977282488cddf3b7ab9afa7f7574756ea115b04575ef08cc6a1f4", "1.24.0--r42hc247a5b_0": "sha256:b0f52efb3d246787f3eb0e6840694d6ea970811a5342d80a665348b0ff4b70b9", "1.20.0--r41hc247a5b_2": "sha256:297284c528f9c1c7cae87d2ebbc00853861b9075a20ae62a5906dc76d0888646", "1.18.0--r41h399db7b_0": "sha256:95b5672879fcbcb987342fa8568fc604c56c0792bdff643488e6bebfca4f6fbd", "1.16.0--r40h399db7b_1": "sha256:10d2f92396a19d47c12f819594a369ab39273f9b249e60b6f5657940535f7061", "1.14.0--r40h5f743cb_0": "sha256:76bee8dbb95c8e4868bafe74b7d1aa8212f571aae7b0bd89c580c5f5c8a4a4b6", "1.24.0--r42hf17093f_1": "sha256:a169bd773529f5889b171cf59c59675e818dbd7831f72f685fbee5df83790231", "1.26.0--r43hf17093f_0": "sha256:83e9e3a0ce5fa3bffcc8bad69eb7f25ed960a747cceebaf168d6e3edebd88ba2", "1.28.0--r43hf17093f_0": "sha256:d81965a96ce001c709df8e8d7423aac9621e981429fd173753ae149295016348", "1.32.0--r44he5774e6_0": "sha256:fb21032ae5ddcba2eac607ca33e68ea42a7c577b1fdf9966af2bb829284be646"}, "docker": "quay.io/biocontainers/bioconductor-normr", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-normr.
shpc-registry automated BioContainers addition for bioconductor-normr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-normr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-normr:1.32.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-normr/1.32.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-normr/1.32.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-normr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-normr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-normr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-normr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-normr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-normr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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