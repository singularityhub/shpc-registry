---
layout: container
name:  "quay.io/biocontainers/mirtrace"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mirtrace/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/mirtrace/container.yaml"
updated_at: "2022-10-27 00:30:44.823682"
latest: "1.0.1--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/mirtrace"
aliases:
 - "mirtrace"
 - "mirtrace.jar"
versions:
 - "1.0.1--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for mirtrace"
config: {"url": "https://biocontainers.pro/tools/mirtrace", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mirtrace", "latest": {"1.0.1--hdfd78af_1": "sha256:b5295e1ede22b5f9588f2673f2a1d381935845060798055b3be2f41dc93b5ec4"}, "tags": {"1.0.1--hdfd78af_1": "sha256:b5295e1ede22b5f9588f2673f2a1d381935845060798055b3be2f41dc93b5ec4"}, "docker": "quay.io/biocontainers/mirtrace", "aliases": {"mirtrace": "/usr/local/bin/mirtrace", "mirtrace.jar": "/usr/local/bin/mirtrace.jar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mirtrace.
shpc-registry automated BioContainers addition for mirtrace
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mirtrace
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mirtrace:1.0.1--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mirtrace/1.0.1--hdfd78af_1
$ module help quay.io/biocontainers/mirtrace/1.0.1--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mirtrace-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mirtrace-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mirtrace-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mirtrace-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mirtrace-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mirtrace-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mirtrace

```bash
$ singularity exec <container> /usr/local/bin/mirtrace
$ podman run --it --rm --entrypoint /usr/local/bin/mirtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mirtrace.jar

```bash
$ singularity exec <container> /usr/local/bin/mirtrace.jar
$ podman run --it --rm --entrypoint /usr/local/bin/mirtrace.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mirtrace.jar   -v ${PWD} -w ${PWD} <container> -c " $@"
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