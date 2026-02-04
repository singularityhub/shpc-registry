---
layout: container
name:  "quay.io/biocontainers/cosigt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cosigt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cosigt/container.yaml"
updated_at: "2026-02-04 04:23:04.211273"
latest: "0.1.2--he881be0_0"
container_url: "https://biocontainers.pro/tools/cosigt"
aliases:
 - "cosigt"
versions:
 - "0.1.2--he881be0_0"
description: "singularity registry hpc automated addition for cosigt"
config: {"url": "https://biocontainers.pro/tools/cosigt", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for cosigt", "latest": {"0.1.2--he881be0_0": "sha256:c80ecefd2216bf6cb1fd8f0d9effb51662d8cc561dad34d2dea60fe5e407caff"}, "tags": {"0.1.2--he881be0_0": "sha256:c80ecefd2216bf6cb1fd8f0d9effb51662d8cc561dad34d2dea60fe5e407caff"}, "docker": "quay.io/biocontainers/cosigt", "aliases": {"cosigt": "/usr/local/bin/cosigt"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cosigt.
singularity registry hpc automated addition for cosigt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cosigt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cosigt:0.1.2--he881be0_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cosigt/0.1.2--he881be0_0
$ module help quay.io/biocontainers/cosigt/0.1.2--he881be0_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cosigt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cosigt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cosigt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cosigt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cosigt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cosigt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### cosigt

```bash
$ singularity exec <container> /usr/local/bin/cosigt
$ podman run --it --rm --entrypoint /usr/local/bin/cosigt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cosigt   -v ${PWD} -w ${PWD} <container> -c " $@"
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