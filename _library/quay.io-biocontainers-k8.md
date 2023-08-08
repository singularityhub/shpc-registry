---
layout: container
name:  "quay.io/biocontainers/k8"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/k8/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/k8/container.yaml"
updated_at: "2023-08-08 02:40:58.306618"
latest: "0.2.5--hdcf5f25_4"
container_url: "https://biocontainers.pro/tools/k8"
aliases:
 - "k8"
versions:
 - "0.2.5--hd03093a_2"
 - "0.2.5--hdcf5f25_4"
description: "shpc-registry automated BioContainers addition for k8"
config: {"url": "https://biocontainers.pro/tools/k8", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for k8", "latest": {"0.2.5--hdcf5f25_4": "sha256:d75f340daccef624e8e0b69beb94ebbe47253506391183dbba347a099972e14a"}, "tags": {"0.2.5--hd03093a_2": "sha256:a38324382ff30253f5765d7012f49447c79e7887188e2f37c5167206620074c9", "0.2.5--hdcf5f25_4": "sha256:d75f340daccef624e8e0b69beb94ebbe47253506391183dbba347a099972e14a"}, "docker": "quay.io/biocontainers/k8", "aliases": {"k8": "/usr/local/bin/k8"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/k8.
shpc-registry automated BioContainers addition for k8
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/k8
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/k8:0.2.5--hdcf5f25_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/k8/0.2.5--hdcf5f25_4
$ module help quay.io/biocontainers/k8/0.2.5--hdcf5f25_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### k8-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### k8-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### k8-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### k8-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### k8-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### k8-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### k8

```bash
$ singularity exec <container> /usr/local/bin/k8
$ podman run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/k8   -v ${PWD} -w ${PWD} <container> -c " $@"
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