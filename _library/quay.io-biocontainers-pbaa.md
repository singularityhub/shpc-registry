---
layout: container
name:  "quay.io/biocontainers/pbaa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbaa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbaa/container.yaml"
updated_at: "2023-11-21 02:38:18.867327"
latest: "1.0.3--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pbaa"
aliases:
 - "pbaa"
versions:
 - "1.0.3--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for pbaa"
config: {"url": "https://biocontainers.pro/tools/pbaa", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for pbaa", "latest": {"1.0.3--hdfd78af_0": "sha256:6cf5bd5b509c8e65a994a8ba53d8724d5e49cb34ac980cf6363ff92f64dfe4f8"}, "tags": {"1.0.3--hdfd78af_0": "sha256:6cf5bd5b509c8e65a994a8ba53d8724d5e49cb34ac980cf6363ff92f64dfe4f8"}, "docker": "quay.io/biocontainers/pbaa", "aliases": {"pbaa": "/usr/local/bin/pbaa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbaa.
shpc-registry automated BioContainers addition for pbaa
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbaa
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbaa:1.0.3--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbaa/1.0.3--hdfd78af_0
$ module help quay.io/biocontainers/pbaa/1.0.3--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbaa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbaa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbaa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbaa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbaa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbaa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pbaa

```bash
$ singularity exec <container> /usr/local/bin/pbaa
$ podman run --it --rm --entrypoint /usr/local/bin/pbaa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbaa   -v ${PWD} -w ${PWD} <container> -c " $@"
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