---
layout: container
name:  "quay.io/biocontainers/fates-emerald"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fates-emerald/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fates-emerald/container.yaml"
updated_at: "2024-12-13 03:32:59.368004"
latest: "2.0.1"
container_url: "https://biocontainers.pro/tools/fates-emerald"

versions:
 - "2.0.1"
description: "shpc-registry automated BioContainers addition for fates-emerald"
config: {"url": "https://biocontainers.pro/tools/fates-emerald", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fates-emerald", "latest": {"2.0.1": "sha256:7e0ecb484cee940a96ac10cd59f94591aa46e944596f02022de6ffdc40aeb2ba"}, "tags": {"2.0.1": "sha256:7e0ecb484cee940a96ac10cd59f94591aa46e944596f02022de6ffdc40aeb2ba"}, "docker": "quay.io/biocontainers/fates-emerald"}
---

This module is a singularity container wrapper for quay.io/biocontainers/fates-emerald.
shpc-registry automated BioContainers addition for fates-emerald
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fates-emerald
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fates-emerald:2.0.1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fates-emerald/2.0.1
$ module help quay.io/biocontainers/fates-emerald/2.0.1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fates-emerald-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fates-emerald-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fates-emerald-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fates-emerald-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fates-emerald-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fates-emerald-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### fates-emerald

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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