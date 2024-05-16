---
layout: container
name:  "quay.io/biocontainers/nxtrim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nxtrim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nxtrim/container.yaml"
updated_at: "2024-05-16 02:43:09.735082"
latest: "0.4.3--hdcf5f25_4"
container_url: "https://biocontainers.pro/tools/nxtrim"
aliases:
 - "nxtrim"
versions:
 - "0.4.3--hd03093a_2"
 - "0.4.3--hdcf5f25_4"
description: "shpc-registry automated BioContainers addition for nxtrim"
config: {"url": "https://biocontainers.pro/tools/nxtrim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nxtrim", "latest": {"0.4.3--hdcf5f25_4": "sha256:74667439721e0b95fae644bbdc7f9abe5018cfd9eb6bb7209915751332ceaa10"}, "tags": {"0.4.3--hd03093a_2": "sha256:e566bf32a083a96884efd201bc88aa2390a7e80ba023949ef1515cebb9933353", "0.4.3--hdcf5f25_4": "sha256:74667439721e0b95fae644bbdc7f9abe5018cfd9eb6bb7209915751332ceaa10"}, "docker": "quay.io/biocontainers/nxtrim", "aliases": {"nxtrim": "/usr/local/bin/nxtrim"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nxtrim.
shpc-registry automated BioContainers addition for nxtrim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nxtrim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nxtrim:0.4.3--hdcf5f25_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nxtrim/0.4.3--hdcf5f25_4
$ module help quay.io/biocontainers/nxtrim/0.4.3--hdcf5f25_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nxtrim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nxtrim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nxtrim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nxtrim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nxtrim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nxtrim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nxtrim

```bash
$ singularity exec <container> /usr/local/bin/nxtrim
$ podman run --it --rm --entrypoint /usr/local/bin/nxtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nxtrim   -v ${PWD} -w ${PWD} <container> -c " $@"
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