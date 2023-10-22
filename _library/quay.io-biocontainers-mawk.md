---
layout: container
name:  "quay.io/biocontainers/mawk"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mawk/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mawk/container.yaml"
updated_at: "2023-10-22 03:01:31.731703"
latest: "1.3.4--h031d066_7"
container_url: "https://biocontainers.pro/tools/mawk"
aliases:
 - "mawk"
versions:
 - "1.3.4--hec16e2b_5"
 - "1.3.4--h031d066_7"
description: "shpc-registry automated BioContainers addition for mawk"
config: {"url": "https://biocontainers.pro/tools/mawk", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mawk", "latest": {"1.3.4--h031d066_7": "sha256:793a6f7e2f641288585b0714d097c5c6b146d5d54c72eb000de2dc7bef24a784"}, "tags": {"1.3.4--hec16e2b_5": "sha256:e23c6573aea6bcf47dbf05472750c4d540322874ac83de632c6c348826295566", "1.3.4--h031d066_7": "sha256:793a6f7e2f641288585b0714d097c5c6b146d5d54c72eb000de2dc7bef24a784"}, "docker": "quay.io/biocontainers/mawk", "aliases": {"mawk": "/usr/local/bin/mawk"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mawk.
shpc-registry automated BioContainers addition for mawk
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mawk
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mawk:1.3.4--h031d066_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mawk/1.3.4--h031d066_7
$ module help quay.io/biocontainers/mawk/1.3.4--h031d066_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mawk-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mawk-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mawk-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mawk-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mawk-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mawk-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mawk

```bash
$ singularity exec <container> /usr/local/bin/mawk
$ podman run --it --rm --entrypoint /usr/local/bin/mawk   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mawk   -v ${PWD} -w ${PWD} <container> -c " $@"
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