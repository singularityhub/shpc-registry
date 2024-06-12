---
layout: container
name:  "quay.io/biocontainers/genion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genion/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/genion/container.yaml"
updated_at: "2024-06-12 02:57:39.824440"
latest: "1.2.3--hdcf5f25_1"
container_url: "https://biocontainers.pro/tools/genion"
aliases:
 - "genion"
versions:
 - "1.1.1--hd03093a_1"
 - "1.2.1--hd03093a_0"
 - "1.1.1--hdcf5f25_3"
 - "1.2.3--hdcf5f25_1"
description: "singularity registry hpc automated addition for genion"
config: {"url": "https://biocontainers.pro/tools/genion", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for genion", "latest": {"1.2.3--hdcf5f25_1": "sha256:c8ea3d4c9894b0459e2e0704fd3f7b1d43f2f42bb023c39a03608b4589f009f7"}, "tags": {"1.1.1--hd03093a_1": "sha256:1989da37f4a02cacc6f0484e36e3a155dc70dc74d37ad9b4d930a6df767fe1ab", "1.2.1--hd03093a_0": "sha256:9f5c6a6f7c338dea3df2d065a9eae4356c8e5e3c75b02f35ecc9e544c7fc5e33", "1.1.1--hdcf5f25_3": "sha256:9ff38a22e5ca26e9a86c85ac4e6f23e26f1ce3c922b3ab48be2f091908654cac", "1.2.3--hdcf5f25_1": "sha256:c8ea3d4c9894b0459e2e0704fd3f7b1d43f2f42bb023c39a03608b4589f009f7"}, "docker": "quay.io/biocontainers/genion", "aliases": {"genion": "/usr/local/bin/genion"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genion.
singularity registry hpc automated addition for genion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genion:1.2.3--hdcf5f25_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genion/1.2.3--hdcf5f25_1
$ module help quay.io/biocontainers/genion/1.2.3--hdcf5f25_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genion-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genion

```bash
$ singularity exec <container> /usr/local/bin/genion
$ podman run --it --rm --entrypoint /usr/local/bin/genion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genion   -v ${PWD} -w ${PWD} <container> -c " $@"
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