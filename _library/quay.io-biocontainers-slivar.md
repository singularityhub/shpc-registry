---
layout: container
name:  "quay.io/biocontainers/slivar"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/slivar/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/slivar/container.yaml"
updated_at: "2023-05-27 03:09:58.430735"
latest: "0.2.9--h2eeb373_0"
container_url: "https://biocontainers.pro/tools/slivar"
aliases:
 - "pslivar"
 - "slivar"
versions:
 - "0.2.7--h2eeb373_0"
 - "0.2.8--h2eeb373_0"
 - "0.2.9--h2eeb373_0"
description: "shpc-registry automated BioContainers addition for slivar"
config: {"url": "https://biocontainers.pro/tools/slivar", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for slivar", "latest": {"0.2.9--h2eeb373_0": "sha256:cc2a9a52e1f67dc70d10a4fe493cb04adbc4d746601aad11684eddf5767bc13d"}, "tags": {"0.2.7--h2eeb373_0": "sha256:2b821cf760c580d6a4da342129a0039706f1d6be335dcf3ef9f649fdc1232b10", "0.2.8--h2eeb373_0": "sha256:0ecd57e5a35977964d0394aa6b7a30039df11b3d74efcd28267d023bb81369b3", "0.2.9--h2eeb373_0": "sha256:cc2a9a52e1f67dc70d10a4fe493cb04adbc4d746601aad11684eddf5767bc13d"}, "docker": "quay.io/biocontainers/slivar", "aliases": {"pslivar": "/usr/local/bin/pslivar", "slivar": "/usr/local/bin/slivar"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/slivar.
shpc-registry automated BioContainers addition for slivar
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/slivar
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/slivar:0.2.9--h2eeb373_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/slivar/0.2.9--h2eeb373_0
$ module help quay.io/biocontainers/slivar/0.2.9--h2eeb373_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### slivar-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### slivar-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### slivar-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### slivar-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### slivar-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### slivar-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pslivar

```bash
$ singularity exec <container> /usr/local/bin/pslivar
$ podman run --it --rm --entrypoint /usr/local/bin/pslivar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pslivar   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### slivar

```bash
$ singularity exec <container> /usr/local/bin/slivar
$ podman run --it --rm --entrypoint /usr/local/bin/slivar   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/slivar   -v ${PWD} -w ${PWD} <container> -c " $@"
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