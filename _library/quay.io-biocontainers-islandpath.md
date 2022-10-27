---
layout: container
name:  "quay.io/biocontainers/islandpath"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/islandpath/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/islandpath/container.yaml"
updated_at: "2022-10-27 00:40:38.696025"
latest: "1.0.6--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/islandpath"
aliases:
 - "islandpath"
versions:
 - "1.0.6--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for islandpath"
config: {"url": "https://biocontainers.pro/tools/islandpath", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for islandpath", "latest": {"1.0.6--hdfd78af_0": "sha256:aaeac1727ebbd2c2bc4c872f0ccfaa99a639834af95975ea326a514b2e080c17"}, "tags": {"1.0.6--hdfd78af_0": "sha256:aaeac1727ebbd2c2bc4c872f0ccfaa99a639834af95975ea326a514b2e080c17"}, "docker": "quay.io/biocontainers/islandpath", "aliases": {"islandpath": "/usr/local/bin/islandpath"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/islandpath.
shpc-registry automated BioContainers addition for islandpath
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/islandpath
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/islandpath:1.0.6--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/islandpath/1.0.6--hdfd78af_0
$ module help quay.io/biocontainers/islandpath/1.0.6--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### islandpath-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### islandpath-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### islandpath-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### islandpath-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### islandpath-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### islandpath-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### islandpath

```bash
$ singularity exec <container> /usr/local/bin/islandpath
$ podman run --it --rm --entrypoint /usr/local/bin/islandpath   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/islandpath   -v ${PWD} -w ${PWD} <container> -c " $@"
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