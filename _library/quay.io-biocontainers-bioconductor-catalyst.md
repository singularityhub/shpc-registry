---
layout: container
name:  "quay.io/biocontainers/bioconductor-catalyst"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-catalyst/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-catalyst/container.yaml"
updated_at: "2024-10-22 03:06:54.531585"
latest: "1.26.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-catalyst"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "1.8.6--r36_0"
 - "1.22.0--r42hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r41hdfd78af_0"
 - "1.14.0--r40hdfd78af_1"
 - "1.12.1--r40_0"
 - "1.24.0--r43hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-catalyst"
config: {"url": "https://biocontainers.pro/tools/bioconductor-catalyst", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-catalyst", "latest": {"1.26.0--r43hdfd78af_0": "sha256:250db31df55d22d86d009dd7053aaf630fa9cf73285dae256e630bf7f7bb509b"}, "tags": {"1.8.6--r36_0": "sha256:04d26ad4939f1420ff7e63887904fd1b55e42b95e35a678f7626d8f233502ed3", "1.22.0--r42hdfd78af_0": "sha256:35338520010944d4465bb46c384e1f97d19500601ef4ffabcc7b33a5b23dab6d", "1.18.0--r41hdfd78af_0": "sha256:9a6960a6b8a443d70ed1a81c7046f8b1c1749bb6dbdfd69a527125052d5ab53a", "1.16.0--r41hdfd78af_0": "sha256:7fe3e51bac82cc35b3562ec394831426a918a7a515b174446dec611f9c791fb4", "1.14.0--r40hdfd78af_1": "sha256:e91c5859524bdeca4fa1f8eb5b1cad1191d980b4297ced1cac05975410727112", "1.12.1--r40_0": "sha256:edba069f9d82cdbaac8d8176a3e07dd095b4ba4dba8b9774be11cc7e49e47168", "1.24.0--r43hdfd78af_0": "sha256:d5e3d7046015a7c23673f8ac7b7d76d1fbcb9fec6b831879f5b306c51d4088f2", "1.26.0--r43hdfd78af_0": "sha256:250db31df55d22d86d009dd7053aaf630fa9cf73285dae256e630bf7f7bb509b"}, "docker": "quay.io/biocontainers/bioconductor-catalyst", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-catalyst.
shpc-registry automated BioContainers addition for bioconductor-catalyst
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-catalyst
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-catalyst:1.26.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-catalyst/1.26.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-catalyst/1.26.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-catalyst-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-catalyst-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-catalyst-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-catalyst-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-catalyst-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-catalyst-inspect-deffile:

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