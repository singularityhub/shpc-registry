---
layout: container
name:  "quay.io/biocontainers/orfm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/orfm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/orfm/container.yaml"
updated_at: "2025-12-12 03:50:25.900007"
latest: "1.4.0--h577a1d6_0"
container_url: "https://biocontainers.pro/tools/orfm"
aliases:
 - "orfm"
versions:
 - "1.3--hed695b0_0"
 - "1.4.0--h577a1d6_0"
description: "shpc-registry automated BioContainers addition for orfm"
config: {"url": "https://biocontainers.pro/tools/orfm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for orfm", "latest": {"1.4.0--h577a1d6_0": "sha256:713cae6b8335f816acbed1df532f85d083de9aba4bacb4888537735dc36846bf"}, "tags": {"1.3--hed695b0_0": "sha256:17657fd85d06a2710df0d969e29b8e0f3185c08825cb249fff7fb9a2976c8301", "1.4.0--h577a1d6_0": "sha256:713cae6b8335f816acbed1df532f85d083de9aba4bacb4888537735dc36846bf"}, "docker": "quay.io/biocontainers/orfm", "aliases": {"orfm": "/usr/local/bin/orfm"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/orfm.
shpc-registry automated BioContainers addition for orfm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/orfm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/orfm:1.4.0--h577a1d6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/orfm/1.4.0--h577a1d6_0
$ module help quay.io/biocontainers/orfm/1.4.0--h577a1d6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### orfm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### orfm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### orfm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### orfm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### orfm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### orfm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### orfm

```bash
$ singularity exec <container> /usr/local/bin/orfm
$ podman run --it --rm --entrypoint /usr/local/bin/orfm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orfm   -v ${PWD} -w ${PWD} <container> -c " $@"
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