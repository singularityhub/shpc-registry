---
layout: container
name:  "quay.io/biocontainers/bioconductor-lpsymphony"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lpsymphony/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lpsymphony/container.yaml"
updated_at: "2024-05-21 03:16:06.220895"
latest: "1.28.1--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lpsymphony"
aliases:
 - "ncurses5-config"
 - "ncursesw5-config"
versions:
 - "1.8.0--r341hfc679d8_0"
 - "1.22.0--r41hc247a5b_2"
 - "1.20.0--r41h399db7b_0"
 - "1.18.0--r40h399db7b_1"
 - "1.14.0--r36he1b5a44_0"
 - "1.12.0--r36he1b5a44_1"
 - "1.26.0--r42h38f54d8_0"
 - "1.26.0--r42ha1e849b_1"
 - "1.28.1--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lpsymphony"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lpsymphony", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lpsymphony", "latest": {"1.28.1--r43hf17093f_0": "sha256:9b559d96140f7e21b05bb7506e14915f733eb50204a19a7c8af8b9386168f7a4"}, "tags": {"1.8.0--r341hfc679d8_0": "sha256:a4f6bb16081254b99909e7d960be7c44bac839f9380d8b536705a1c5afc51239", "1.22.0--r41hc247a5b_2": "sha256:24d1ce7e7398e857afba7990373eb8bd33189fe7d0e207adabc89f317b451465", "1.20.0--r41h399db7b_0": "sha256:1607e09b4a265e3dd69686113fff420d105a961b7434cbd97857a54484996544", "1.18.0--r40h399db7b_1": "sha256:6987c63a6dfbaf29d208fafd4fbbc01d446c603b214802f1cfe311c5551e2466", "1.14.0--r36he1b5a44_0": "sha256:af599539596d594f06333e876a304ba6c77853a87c6831270b6f8358d7e7c3c5", "1.12.0--r36he1b5a44_1": "sha256:a2b8942a05204685f2700eb7bd7fcc5089a8dcdd83aed8c43010d7f8d204f0a1", "1.26.0--r42h38f54d8_0": "sha256:70ae93a32fb7393bf415691d4a4eac90f8d43a53bb8dc7c9eeb6339f598700ca", "1.26.0--r42ha1e849b_1": "sha256:9212b4d2a95ffcf105a2c625b481ed4e9a47ca83a3c0a8b746a7df6eea31afa0", "1.28.1--r43hf17093f_0": "sha256:9b559d96140f7e21b05bb7506e14915f733eb50204a19a7c8af8b9386168f7a4"}, "docker": "quay.io/biocontainers/bioconductor-lpsymphony", "aliases": {"ncurses5-config": "/usr/local/bin/ncurses5-config", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lpsymphony.
shpc-registry automated BioContainers addition for bioconductor-lpsymphony
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lpsymphony
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lpsymphony:1.28.1--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lpsymphony/1.28.1--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-lpsymphony/1.28.1--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lpsymphony-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lpsymphony-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lpsymphony-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lpsymphony-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lpsymphony-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lpsymphony-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ncurses5-config

```bash
$ singularity exec <container> /usr/local/bin/ncurses5-config
$ podman run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncurses5-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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