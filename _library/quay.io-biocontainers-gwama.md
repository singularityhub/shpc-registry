---
layout: container
name:  "quay.io/biocontainers/gwama"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gwama/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gwama/container.yaml"
updated_at: "2024-01-22 02:41:10.534311"
latest: "2.2.2--hdcf5f25_4"
container_url: "https://biocontainers.pro/tools/gwama"
aliases:
 - "GWAMA"
versions:
 - "2.2.2--hd03093a_2"
 - "2.2.2--hdcf5f25_4"
description: "shpc-registry automated BioContainers addition for gwama"
config: {"url": "https://biocontainers.pro/tools/gwama", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gwama", "latest": {"2.2.2--hdcf5f25_4": "sha256:09f8629fb9ed99761a83c45bdfd0d2ecad62c7783532c239412f41aa4563b351"}, "tags": {"2.2.2--hd03093a_2": "sha256:15ee1d375ef88f4c186063c8cc69070bcfb3f81b91e87c83b296c6ae2bb1b0e4", "2.2.2--hdcf5f25_4": "sha256:09f8629fb9ed99761a83c45bdfd0d2ecad62c7783532c239412f41aa4563b351"}, "docker": "quay.io/biocontainers/gwama", "aliases": {"GWAMA": "/usr/local/bin/GWAMA"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gwama.
shpc-registry automated BioContainers addition for gwama
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gwama
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gwama:2.2.2--hdcf5f25_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gwama/2.2.2--hdcf5f25_4
$ module help quay.io/biocontainers/gwama/2.2.2--hdcf5f25_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gwama-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gwama-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gwama-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gwama-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gwama-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gwama-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### GWAMA

```bash
$ singularity exec <container> /usr/local/bin/GWAMA
$ podman run --it --rm --entrypoint /usr/local/bin/GWAMA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/GWAMA   -v ${PWD} -w ${PWD} <container> -c " $@"
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