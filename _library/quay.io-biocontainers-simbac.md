---
layout: container
name:  "quay.io/biocontainers/simbac"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/simbac/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/simbac/container.yaml"
updated_at: "2023-05-28 03:01:02.090384"
latest: "0.1a--h5e66344_4"
container_url: "https://biocontainers.pro/tools/simbac"
aliases:
 - "SimBac"
versions:
 - "0.1a--h5e66344_3"
 - "0.1a--h5e66344_4"
description: "shpc-registry automated BioContainers addition for simbac"
config: {"url": "https://biocontainers.pro/tools/simbac", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for simbac", "latest": {"0.1a--h5e66344_4": "sha256:d6f334cc7d9c9c8440e2a1a2c328de457280dd9b9a4363ac4513862e8a84761a"}, "tags": {"0.1a--h5e66344_3": "sha256:b8974e0721471901c6e3fc5c15469e98196c33ef7fa55e885abd6b65d5800f2b", "0.1a--h5e66344_4": "sha256:d6f334cc7d9c9c8440e2a1a2c328de457280dd9b9a4363ac4513862e8a84761a"}, "docker": "quay.io/biocontainers/simbac", "aliases": {"SimBac": "/usr/local/bin/SimBac"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/simbac.
shpc-registry automated BioContainers addition for simbac
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/simbac
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/simbac:0.1a--h5e66344_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/simbac/0.1a--h5e66344_4
$ module help quay.io/biocontainers/simbac/0.1a--h5e66344_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### simbac-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### simbac-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### simbac-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### simbac-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### simbac-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### simbac-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### SimBac

```bash
$ singularity exec <container> /usr/local/bin/SimBac
$ podman run --it --rm --entrypoint /usr/local/bin/SimBac   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SimBac   -v ${PWD} -w ${PWD} <container> -c " $@"
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