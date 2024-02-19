---
layout: container
name:  "quay.io/biocontainers/bioconductor-bcseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bcseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bcseq/container.yaml"
updated_at: "2024-02-19 02:26:09.732927"
latest: "1.22.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bcseq"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r36he1b5a44_0"
 - "1.16.0--r41hc247a5b_2"
 - "1.14.0--r41h399db7b_0"
 - "1.12.0--r40h399db7b_1"
 - "1.10.0--r40h5f743cb_0"
 - "1.20.0--r42hc247a5b_0"
 - "1.20.0--r42hf17093f_1"
 - "1.22.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bcseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bcseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bcseq", "latest": {"1.22.0--r43hf17093f_0": "sha256:5fdb0569e74df0a4d717448611de2d01b8b65420d072f7e699129e777ed9f5fb"}, "tags": {"1.8.0--r36he1b5a44_0": "sha256:358cb61a6df6c6913683df60e5ebacfd19ad4ddfac20e02053460ba49c4bf03d", "1.16.0--r41hc247a5b_2": "sha256:7ae68f28a7f476d3f72cfb782bed2c487b858871d344b837633b45ee2412b2a9", "1.14.0--r41h399db7b_0": "sha256:ef9f39b4b1c798c964279d2108cafffc27b3b079488b0211931f93998ff1badf", "1.12.0--r40h399db7b_1": "sha256:76d1b74890485c68e205636893b8a73e4ce6ae0745c0d2ba82e45c55f96d2d99", "1.10.0--r40h5f743cb_0": "sha256:5c3898b6b1fc2be44d48892d6c4622f9823bbe239fd82abfcd058e2759ecfc9a", "1.20.0--r42hc247a5b_0": "sha256:30620a92dae2cfe31763b5575433c594681951390065072b4ca537b1fc95982a", "1.20.0--r42hf17093f_1": "sha256:272280a3fab7dd8ef497c58e074ea193a91e24d01ac17c14799e6fcbefa3e9d0", "1.22.0--r43hf17093f_0": "sha256:5fdb0569e74df0a4d717448611de2d01b8b65420d072f7e699129e777ed9f5fb"}, "docker": "quay.io/biocontainers/bioconductor-bcseq", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bcseq.
shpc-registry automated BioContainers addition for bioconductor-bcseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bcseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bcseq:1.22.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bcseq/1.22.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-bcseq/1.22.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bcseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bcseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bcseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bcseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bcseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bcseq-inspect-deffile:

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