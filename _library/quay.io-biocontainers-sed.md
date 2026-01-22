---
layout: container
name:  "quay.io/biocontainers/sed"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sed/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/sed/container.yaml"
updated_at: "2026-01-22 04:37:55.256947"
latest: "4.8"
container_url: "https://biocontainers.pro/tools/sed"
aliases:
 - "sed"
versions:
 - "4.7.0"
 - "4.8"
description: "shpc-registry automated BioContainers addition for sed"
config: {"url": "https://biocontainers.pro/tools/sed", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sed", "latest": {"4.8": "sha256:662193598f523ed45056fe71556377fc42e6d53a9b7b807421050475a630fc5a"}, "tags": {"4.7.0": "sha256:cae5cdb96d0480c92fc2162ea63955877694512542a33cd6b345d9e5be4b07e7", "4.8": "sha256:662193598f523ed45056fe71556377fc42e6d53a9b7b807421050475a630fc5a"}, "docker": "quay.io/biocontainers/sed", "aliases": {"sed": "/usr/local/bin/sed"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sed.
shpc-registry automated BioContainers addition for sed
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sed
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sed:4.8
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sed/4.8
$ module help quay.io/biocontainers/sed/4.8
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sed-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sed-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sed-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sed-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sed-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sed-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### sed

```bash
$ singularity exec <container> /usr/local/bin/sed
$ podman run --it --rm --entrypoint /usr/local/bin/sed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sed   -v ${PWD} -w ${PWD} <container> -c " $@"
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