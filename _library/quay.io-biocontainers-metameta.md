---
layout: container
name:  "quay.io/biocontainers/metameta"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/metameta/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/metameta/container.yaml"
updated_at: "2022-10-27 00:58:08.430480"
latest: "1.2.0--hdfd78af_4"
container_url: "https://biocontainers.pro/tools/metameta"
aliases:
 - "metameta"
versions:
 - "1.2.0--hdfd78af_4"
description: "shpc-registry automated BioContainers addition for metameta"
config: {"url": "https://biocontainers.pro/tools/metameta", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for metameta", "latest": {"1.2.0--hdfd78af_4": "sha256:3a4adf2fc791c07556eb5da0aeae44761293ac0f2d730ffecb178a6a03bfc60a"}, "tags": {"1.2.0--hdfd78af_4": "sha256:3a4adf2fc791c07556eb5da0aeae44761293ac0f2d730ffecb178a6a03bfc60a"}, "docker": "quay.io/biocontainers/metameta", "aliases": {"metameta": "/usr/local/bin/metameta"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/metameta.
shpc-registry automated BioContainers addition for metameta
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/metameta
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/metameta:1.2.0--hdfd78af_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/metameta/1.2.0--hdfd78af_4
$ module help quay.io/biocontainers/metameta/1.2.0--hdfd78af_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### metameta-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### metameta-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### metameta-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### metameta-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### metameta-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### metameta-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### metameta

```bash
$ singularity exec <container> /usr/local/bin/metameta
$ podman run --it --rm --entrypoint /usr/local/bin/metameta   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/metameta   -v ${PWD} -w ${PWD} <container> -c " $@"
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