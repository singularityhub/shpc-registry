---
layout: container
name:  "quay.io/biocontainers/bioconductor-go.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-go.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-go.db/container.yaml"
updated_at: "2023-02-07 03:17:31.471084"
latest: "3.16.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-go.db"
aliases:
 - "gio-launch-desktop"
 - "c89"
 - "c99"
versions:
 - "3.8.2--r36_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.14.0--r41hdfd78af_1"
 - "3.13.0--r41hdfd78af_0"
 - "3.12.1--r40hdfd78af_1"
 - "3.11.4--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-go.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-go.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-go.db", "latest": {"3.16.0--r42hdfd78af_0": "sha256:7a59ae7269667f6857315b9b28bee02b8dfae8204ad453482e161ca531bc4138"}, "tags": {"3.8.2--r36_1": "sha256:b83401a4f80d6954659ef664e7f3c3b146ef250d6f4a35b5a35aef19ad4fe921", "3.16.0--r42hdfd78af_0": "sha256:7a59ae7269667f6857315b9b28bee02b8dfae8204ad453482e161ca531bc4138", "3.14.0--r41hdfd78af_1": "sha256:49c0eba2f643972c6b684bd9b62447bd5282a96cef946730a52b2e3b0c2205ce", "3.13.0--r41hdfd78af_0": "sha256:b7c858988d529ca092d5df304348f61d60b2ea2b2945674dc3e523ff99ff0236", "3.12.1--r40hdfd78af_1": "sha256:af5c97f9e2f7cb9e03869373d49748b2812c09fcb7cbbc08fa2f6218a0ec8302", "3.11.4--r40_0": "sha256:a4fc7475bc81d8e71f2c7d4f21be15f782f3b577722164387c42dd06202e3719"}, "docker": "quay.io/biocontainers/bioconductor-go.db", "aliases": {"gio-launch-desktop": "/usr/local/bin/gio-launch-desktop", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-go.db.
shpc-registry automated BioContainers addition for bioconductor-go.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-go.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-go.db:3.16.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-go.db/3.16.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-go.db/3.16.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-go.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-go.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-go.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-go.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-go.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-go.db-inspect-deffile:

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