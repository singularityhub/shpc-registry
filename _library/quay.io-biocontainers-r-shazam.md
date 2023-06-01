---
layout: container
name:  "quay.io/biocontainers/r-shazam"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-shazam/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-shazam/container.yaml"
updated_at: "2023-06-01 03:34:19.581322"
latest: "1.1.2--r42h3121a25_1"
container_url: "https://biocontainers.pro/tools/r-shazam"
aliases:
 - "glpsol"
versions:
 - "1.1.2--r41h3121a25_0"
 - "1.1.2--r42h3121a25_1"
description: "shpc-registry automated BioContainers addition for r-shazam"
config: {"url": "https://biocontainers.pro/tools/r-shazam", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-shazam", "latest": {"1.1.2--r42h3121a25_1": "sha256:30e3d7fd8ec1dc542c78cb139bf898c0923c4a95956f68fe8d0cab89476bb5f0"}, "tags": {"1.1.2--r41h3121a25_0": "sha256:8822a48ac9637ee1851b7ab768ab47493f53f1934e2e7964c766258323619beb", "1.1.2--r42h3121a25_1": "sha256:30e3d7fd8ec1dc542c78cb139bf898c0923c4a95956f68fe8d0cab89476bb5f0"}, "docker": "quay.io/biocontainers/r-shazam", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-shazam.
shpc-registry automated BioContainers addition for r-shazam
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-shazam
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-shazam:1.1.2--r42h3121a25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-shazam/1.1.2--r42h3121a25_1
$ module help quay.io/biocontainers/r-shazam/1.1.2--r42h3121a25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-shazam-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-shazam-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-shazam-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-shazam-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-shazam-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-shazam-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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