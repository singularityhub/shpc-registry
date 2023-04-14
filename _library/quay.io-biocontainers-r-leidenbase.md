---
layout: container
name:  "quay.io/biocontainers/r-leidenbase"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-leidenbase/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-leidenbase/container.yaml"
updated_at: "2023-04-14 03:11:37.877252"
latest: "0.1.12--r42h6efe872_0"
container_url: "https://biocontainers.pro/tools/r-leidenbase"

versions:
 - "0.1.3--r41h1aed7a7_2"
 - "0.1.12--r42h6efe872_0"
description: "shpc-registry automated BioContainers addition for r-leidenbase"
config: {"url": "https://biocontainers.pro/tools/r-leidenbase", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-leidenbase", "latest": {"0.1.12--r42h6efe872_0": "sha256:213a1dbd67ec2ec223be713c0d72b673a03fa94926e40f9bc803b02eebcfdce1"}, "tags": {"0.1.3--r41h1aed7a7_2": "sha256:43657706238343db9e63c8e1f93281e483ac596397e1053d76667a1390a37d7b", "0.1.12--r42h6efe872_0": "sha256:213a1dbd67ec2ec223be713c0d72b673a03fa94926e40f9bc803b02eebcfdce1"}, "docker": "quay.io/biocontainers/r-leidenbase"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-leidenbase.
shpc-registry automated BioContainers addition for r-leidenbase
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-leidenbase
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-leidenbase:0.1.12--r42h6efe872_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-leidenbase/0.1.12--r42h6efe872_0
$ module help quay.io/biocontainers/r-leidenbase/0.1.12--r42h6efe872_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-leidenbase-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-leidenbase-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-leidenbase-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-leidenbase-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-leidenbase-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-leidenbase-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-leidenbase

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