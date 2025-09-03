---
layout: container
name:  "quay.io/biocontainers/libstatgen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/libstatgen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/libstatgen/container.yaml"
updated_at: "2025-09-03 03:28:01.410586"
latest: "1.0.15--h077b44d_7"
container_url: "https://biocontainers.pro/tools/libstatgen"

versions:
 - "1.0.5--he941832_0"
 - "1.0.15--hd03093a_3"
 - "1.0.15--hdcf5f25_5"
 - "1.0.15--h077b44d_6"
 - "1.0.15--h077b44d_7"
description: "shpc-registry automated BioContainers addition for libstatgen"
config: {"url": "https://biocontainers.pro/tools/libstatgen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for libstatgen", "latest": {"1.0.15--h077b44d_7": "sha256:31f809d90a0c254824f12a1f3bfc1aa07a72ce0545f5670348768a5607d27b1b"}, "tags": {"1.0.5--he941832_0": "sha256:b8991bec0376d04e468da4cdcc916c39b580bf621cc3a3d68a1199a481c62004", "1.0.15--hd03093a_3": "sha256:c7edf3325763c7a5171120fe6179a7e3316eaf16836a1ac5c7ba8d1451dcb7e4", "1.0.15--hdcf5f25_5": "sha256:4dd8cba1cb201d5e8a4db186d9188a744bb238760b9693fec602d6e866a10302", "1.0.15--h077b44d_6": "sha256:05db6408ce59deeccc18bb9a0829e356401a4c8884eee6932c234c512e07121a", "1.0.15--h077b44d_7": "sha256:31f809d90a0c254824f12a1f3bfc1aa07a72ce0545f5670348768a5607d27b1b"}, "docker": "quay.io/biocontainers/libstatgen"}
---

This module is a singularity container wrapper for quay.io/biocontainers/libstatgen.
shpc-registry automated BioContainers addition for libstatgen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/libstatgen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/libstatgen:1.0.15--h077b44d_7
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/libstatgen/1.0.15--h077b44d_7
$ module help quay.io/biocontainers/libstatgen/1.0.15--h077b44d_7
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### libstatgen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### libstatgen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### libstatgen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### libstatgen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### libstatgen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### libstatgen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### libstatgen

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