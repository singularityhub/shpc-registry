---
layout: container
name:  "quay.io/biocontainers/r-digest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-digest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-digest/container.yaml"
updated_at: "2023-10-02 03:03:36.512714"
latest: "0.6.12--r3.3.1_0"
container_url: "https://biocontainers.pro/tools/r-digest"
aliases:
 - "uconv"
 - "tclsh8.5"
 - "wish8.5"
 - "ncursesw5-config"
versions:
 - "0.6.9--r3.3.1_1"
 - "0.6.12--r3.3.1_0"
description: "shpc-registry automated BioContainers addition for r-digest"
config: {"url": "https://biocontainers.pro/tools/r-digest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-digest", "latest": {"0.6.12--r3.3.1_0": "sha256:7c2bc626726f403d86c68e7464bbd47a35dcfa7da3aba46f06b46712b12755a0"}, "tags": {"0.6.9--r3.3.1_1": "sha256:9e963354cf354cc6ca06ff24f2e7ce22ae368a569190f5d6028a896db04d2c84", "0.6.12--r3.3.1_0": "sha256:7c2bc626726f403d86c68e7464bbd47a35dcfa7da3aba46f06b46712b12755a0"}, "docker": "quay.io/biocontainers/r-digest", "aliases": {"uconv": "/usr/local/bin/uconv", "tclsh8.5": "/usr/local/bin/tclsh8.5", "wish8.5": "/usr/local/bin/wish8.5", "ncursesw5-config": "/usr/local/bin/ncursesw5-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-digest.
shpc-registry automated BioContainers addition for r-digest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-digest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-digest:0.6.12--r3.3.1_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-digest/0.6.12--r3.3.1_0
$ module help quay.io/biocontainers/r-digest/0.6.12--r3.3.1_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-digest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-digest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-digest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-digest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-digest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-digest-inspect-deffile:

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