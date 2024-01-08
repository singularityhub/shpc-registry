---
layout: container
name:  "quay.io/biocontainers/roguenarok"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/roguenarok/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/roguenarok/container.yaml"
updated_at: "2024-01-08 02:40:27.876873"
latest: "1.0.1--h031d066_3"
container_url: "https://biocontainers.pro/tools/roguenarok"
aliases:
 - "RogueNaRok"
 - "RogueNaRok-parallel"
 - "rnr-lsi"
 - "rnr-mast"
 - "rnr-prune"
 - "rnr-tii"
versions:
 - "1.0.1--hec16e2b_1"
 - "1.0.1--h031d066_3"
description: "shpc-registry automated BioContainers addition for roguenarok"
config: {"url": "https://biocontainers.pro/tools/roguenarok", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for roguenarok", "latest": {"1.0.1--h031d066_3": "sha256:dadf83db2e4879de33806f03b1e75e57b1edf6cbafcce8a6cd9fba88b194e511"}, "tags": {"1.0.1--hec16e2b_1": "sha256:371cfa16e827812d40d4fd7292b42531f2f4d3a0b8fa496624c500e909c62b2c", "1.0.1--h031d066_3": "sha256:dadf83db2e4879de33806f03b1e75e57b1edf6cbafcce8a6cd9fba88b194e511"}, "docker": "quay.io/biocontainers/roguenarok", "aliases": {"RogueNaRok": "/usr/local/bin/RogueNaRok", "RogueNaRok-parallel": "/usr/local/bin/RogueNaRok-parallel", "rnr-lsi": "/usr/local/bin/rnr-lsi", "rnr-mast": "/usr/local/bin/rnr-mast", "rnr-prune": "/usr/local/bin/rnr-prune", "rnr-tii": "/usr/local/bin/rnr-tii"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/roguenarok.
shpc-registry automated BioContainers addition for roguenarok
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/roguenarok
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/roguenarok:1.0.1--h031d066_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/roguenarok/1.0.1--h031d066_3
$ module help quay.io/biocontainers/roguenarok/1.0.1--h031d066_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### roguenarok-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### roguenarok-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### roguenarok-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### roguenarok-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### roguenarok-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### roguenarok-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### RogueNaRok

```bash
$ singularity exec <container> /usr/local/bin/RogueNaRok
$ podman run --it --rm --entrypoint /usr/local/bin/RogueNaRok   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RogueNaRok   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### RogueNaRok-parallel

```bash
$ singularity exec <container> /usr/local/bin/RogueNaRok-parallel
$ podman run --it --rm --entrypoint /usr/local/bin/RogueNaRok-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/RogueNaRok-parallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnr-lsi

```bash
$ singularity exec <container> /usr/local/bin/rnr-lsi
$ podman run --it --rm --entrypoint /usr/local/bin/rnr-lsi   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnr-lsi   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnr-mast

```bash
$ singularity exec <container> /usr/local/bin/rnr-mast
$ podman run --it --rm --entrypoint /usr/local/bin/rnr-mast   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnr-mast   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnr-prune

```bash
$ singularity exec <container> /usr/local/bin/rnr-prune
$ podman run --it --rm --entrypoint /usr/local/bin/rnr-prune   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnr-prune   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rnr-tii

```bash
$ singularity exec <container> /usr/local/bin/rnr-tii
$ podman run --it --rm --entrypoint /usr/local/bin/rnr-tii   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rnr-tii   -v ${PWD} -w ${PWD} <container> -c " $@"
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