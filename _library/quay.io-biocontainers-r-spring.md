---
layout: container
name:  "quay.io/biocontainers/r-spring"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-spring/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-spring/container.yaml"
updated_at: "2024-09-13 03:04:19.763017"
latest: "1.0.4--r43hdfd78af_2"
container_url: "https://biocontainers.pro/tools/r-spring"
aliases:
 - "glpsol"
versions:
 - "1.0.4--r42hdfd78af_1"
 - "1.0.4--r43hdfd78af_2"
description: "singularity registry hpc automated addition for r-spring"
config: {"url": "https://biocontainers.pro/tools/r-spring", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-spring", "latest": {"1.0.4--r43hdfd78af_2": "sha256:58252cf4d8678d49f50015428ca760592c6cf37c1c57f0f93deed60bcf354090"}, "tags": {"1.0.4--r42hdfd78af_1": "sha256:23e173800f588f5de0b7f24d10f0b9a060fceaee2d77ec68cb1dc663cf98a197", "1.0.4--r43hdfd78af_2": "sha256:58252cf4d8678d49f50015428ca760592c6cf37c1c57f0f93deed60bcf354090"}, "docker": "quay.io/biocontainers/r-spring", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-spring.
singularity registry hpc automated addition for r-spring
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-spring
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-spring:1.0.4--r43hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-spring/1.0.4--r43hdfd78af_2
$ module help quay.io/biocontainers/r-spring/1.0.4--r43hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-spring-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-spring-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-spring-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-spring-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-spring-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-spring-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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