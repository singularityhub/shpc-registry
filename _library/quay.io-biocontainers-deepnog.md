---
layout: container
name:  "quay.io/biocontainers/deepnog"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deepnog/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/deepnog/container.yaml"
updated_at: "2022-10-27 01:00:04.342394"
latest: "1.2.3--pyh3252c3a_1"
container_url: "https://biocontainers.pro/tools/deepnog"
aliases:
 - "deepnog"
versions:
 - "1.2.3--pyh3252c3a_1"
description: "shpc-registry automated BioContainers addition for deepnog"
config: {"url": "https://biocontainers.pro/tools/deepnog", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for deepnog", "latest": {"1.2.3--pyh3252c3a_1": "sha256:02093134a3896469e933407d8ef7136d9361bed30ed06d0e70243fecdcdf501d"}, "tags": {"1.2.3--pyh3252c3a_1": "sha256:02093134a3896469e933407d8ef7136d9361bed30ed06d0e70243fecdcdf501d"}, "docker": "quay.io/biocontainers/deepnog", "aliases": {"deepnog": "/usr/local/bin/deepnog"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deepnog.
shpc-registry automated BioContainers addition for deepnog
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deepnog
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deepnog:1.2.3--pyh3252c3a_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deepnog/1.2.3--pyh3252c3a_1
$ module help quay.io/biocontainers/deepnog/1.2.3--pyh3252c3a_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deepnog-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deepnog-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deepnog-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deepnog-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deepnog-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deepnog-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deepnog

```bash
$ singularity exec <container> /usr/local/bin/deepnog
$ podman run --it --rm --entrypoint /usr/local/bin/deepnog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deepnog   -v ${PWD} -w ${PWD} <container> -c " $@"
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