---
layout: container
name:  "quay.io/biocontainers/ngsep"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngsep/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/ngsep/container.yaml"
updated_at: "2022-10-27 00:55:14.981793"
latest: "4.0.1--0"
container_url: "https://biocontainers.pro/tools/ngsep"
aliases:
 - "ngsep"
versions:
 - "4.0.1--0"
description: "shpc-registry automated BioContainers addition for ngsep"
config: {"url": "https://biocontainers.pro/tools/ngsep", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ngsep", "latest": {"4.0.1--0": "sha256:2dc30fe5e877473536883be51b06ddf6a6cc62dcd3179c62d338dee9c3f7293b"}, "tags": {"4.0.1--0": "sha256:2dc30fe5e877473536883be51b06ddf6a6cc62dcd3179c62d338dee9c3f7293b"}, "docker": "quay.io/biocontainers/ngsep", "aliases": {"ngsep": "/usr/local/bin/ngsep"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngsep.
shpc-registry automated BioContainers addition for ngsep
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngsep
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngsep:4.0.1--0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngsep/4.0.1--0
$ module help quay.io/biocontainers/ngsep/4.0.1--0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngsep-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngsep-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngsep-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngsep-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngsep-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngsep-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ngsep

```bash
$ singularity exec <container> /usr/local/bin/ngsep
$ podman run --it --rm --entrypoint /usr/local/bin/ngsep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngsep   -v ${PWD} -w ${PWD} <container> -c " $@"
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