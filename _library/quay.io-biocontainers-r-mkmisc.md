---
layout: container
name:  "quay.io/biocontainers/r-mkmisc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-mkmisc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-mkmisc/container.yaml"
updated_at: "2023-06-14 03:15:49.818944"
latest: "1.9--r42h3342da4_0"
container_url: "https://biocontainers.pro/tools/r-mkmisc"

versions:
 - "1.8--r41h3342da4_0"
 - "1.9--r42h3342da4_0"
 - "1.8--r42h3342da4_1"
description: "shpc-registry automated BioContainers addition for r-mkmisc"
config: {"url": "https://biocontainers.pro/tools/r-mkmisc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-mkmisc", "latest": {"1.9--r42h3342da4_0": "sha256:e54386b64f630fd8596fcb33ef88df09dc7de65239baf034f0473c032e7f119a"}, "tags": {"1.8--r41h3342da4_0": "sha256:957db79721ea570df1992c3e8a8358d18145c4cd075d4eb256fe98ccf6002f2d", "1.9--r42h3342da4_0": "sha256:e54386b64f630fd8596fcb33ef88df09dc7de65239baf034f0473c032e7f119a", "1.8--r42h3342da4_1": "sha256:8a56cd73ed67979eed63845ae80916977a0d90c01927d8dfd4435631da82f90e"}, "docker": "quay.io/biocontainers/r-mkmisc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-mkmisc.
shpc-registry automated BioContainers addition for r-mkmisc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-mkmisc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-mkmisc:1.9--r42h3342da4_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-mkmisc/1.9--r42h3342da4_0
$ module help quay.io/biocontainers/r-mkmisc/1.9--r42h3342da4_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-mkmisc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-mkmisc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-mkmisc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-mkmisc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-mkmisc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-mkmisc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-mkmisc

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