---
layout: container
name:  "quay.io/biocontainers/miniasm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/miniasm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/miniasm/container.yaml"
updated_at: "2025-03-25 03:16:56.488849"
latest: "0.3_r179--h7132678_3"
container_url: "https://biocontainers.pro/tools/miniasm"
aliases:
 - "miniasm"
 - "minidot"
versions:
 - "0.3_r179--h7132678_3"
 - "0.3"
description: "shpc-registry automated BioContainers addition for miniasm"
config: {"url": "https://biocontainers.pro/tools/miniasm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for miniasm", "latest": {"0.3_r179--h7132678_3": "sha256:8f317be94f1b5e299957daf3a806ee089aac090eb3510766bd3d6a38ac2be9f0"}, "tags": {"0.3_r179--h7132678_3": "sha256:8f317be94f1b5e299957daf3a806ee089aac090eb3510766bd3d6a38ac2be9f0", "0.3": "sha256:33f8c2437d6fcb7fab46ff02fc65fdddc1f79a933b1e0293a24b21daa58e3e22"}, "docker": "quay.io/biocontainers/miniasm", "aliases": {"miniasm": "/usr/local/bin/miniasm", "minidot": "/usr/local/bin/minidot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/miniasm.
shpc-registry automated BioContainers addition for miniasm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/miniasm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/miniasm:0.3_r179--h7132678_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/miniasm/0.3_r179--h7132678_3
$ module help quay.io/biocontainers/miniasm/0.3_r179--h7132678_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### miniasm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### miniasm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### miniasm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### miniasm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### miniasm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### miniasm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### miniasm

```bash
$ singularity exec <container> /usr/local/bin/miniasm
$ podman run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniasm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minidot

```bash
$ singularity exec <container> /usr/local/bin/minidot
$ podman run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minidot   -v ${PWD} -w ${PWD} <container> -c " $@"
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