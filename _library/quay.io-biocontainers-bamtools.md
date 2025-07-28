---
layout: container
name:  "quay.io/biocontainers/bamtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bamtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bamtools/container.yaml"
updated_at: "2025-07-28 04:26:57.088660"
latest: "2.5.3--he132191_0"
container_url: "https://biocontainers.pro/tools/bamtools"
aliases:
 - "bamtools"
versions:
 - "2.5.2--hd03093a_0"
 - "2.5.2--hd03093a_1"
 - "2.5.2--hdcf5f25_2"
 - "2.5.2--hdcf5f25_3"
 - "2.5.2--hdcf5f25_5"
 - "2.5.2--h077b44d_6"
 - "2.5.3--he132191_0"
description: "shpc-registry automated BioContainers addition for bamtools"
config: {"url": "https://biocontainers.pro/tools/bamtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bamtools", "latest": {"2.5.3--he132191_0": "sha256:b25c726fb17f173d0971615b5d907b11bfc12021b7a7744e36a630906998689b"}, "tags": {"2.5.2--hd03093a_0": "sha256:599e39895bf24cd8cbbccda2a09609dc54435523298147d872267d94dfa19804", "2.5.2--hd03093a_1": "sha256:9eb87f5ff78176c78fab5677976373ab86cabf9ddb0b1ae764ad4009858f417f", "2.5.2--hdcf5f25_2": "sha256:2a6a12c50661287d5605d04e1ab7a67fe9b15994fac26371b52099fd5c59166a", "2.5.2--hdcf5f25_3": "sha256:b4009a6dcec42401b9574902a917c79e955af0f54bf6d14456d2db8dd759f2f7", "2.5.2--hdcf5f25_5": "sha256:36cf305f9dd59d02e33a9fd69543f6f8146b4b7efd1104836d0f847b83db009b", "2.5.2--h077b44d_6": "sha256:1ca40c89e968555209952d40719ee231d7f6e8bdf89dc9f041809d5266ffe4d1", "2.5.3--he132191_0": "sha256:b25c726fb17f173d0971615b5d907b11bfc12021b7a7744e36a630906998689b"}, "docker": "quay.io/biocontainers/bamtools", "aliases": {"bamtools": "/usr/local/bin/bamtools"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bamtools.
shpc-registry automated BioContainers addition for bamtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bamtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bamtools:2.5.3--he132191_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bamtools/2.5.3--he132191_0
$ module help quay.io/biocontainers/bamtools/2.5.3--he132191_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bamtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bamtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bamtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bamtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bamtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bamtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bamtools

```bash
$ singularity exec <container> /usr/local/bin/bamtools
$ podman run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamtools   -v ${PWD} -w ${PWD} <container> -c " $@"
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