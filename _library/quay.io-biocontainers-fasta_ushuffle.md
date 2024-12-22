---
layout: container
name:  "quay.io/biocontainers/fasta_ushuffle"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/fasta_ushuffle/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/fasta_ushuffle/container.yaml"
updated_at: "2024-12-22 02:58:02.873561"
latest: "0.2--h031d066_6"
container_url: "https://biocontainers.pro/tools/fasta_ushuffle"
aliases:
 - "fasta_ushuffle"
 - "ushuffle"
versions:
 - "0.2--hec16e2b_4"
 - "0.2--h031d066_6"
description: "shpc-registry automated BioContainers addition for fasta_ushuffle"
config: {"url": "https://biocontainers.pro/tools/fasta_ushuffle", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for fasta_ushuffle", "latest": {"0.2--h031d066_6": "sha256:8b682bdbce9c1dbcecc19a57db54e70c51c10bb13e147d1a6eab430cd01c0371"}, "tags": {"0.2--hec16e2b_4": "sha256:fbd097083ae7a15580446ca860d6324f7ed736ff0dfad79490a3d05cacea1f23", "0.2--h031d066_6": "sha256:8b682bdbce9c1dbcecc19a57db54e70c51c10bb13e147d1a6eab430cd01c0371"}, "docker": "quay.io/biocontainers/fasta_ushuffle", "aliases": {"fasta_ushuffle": "/usr/local/bin/fasta_ushuffle", "ushuffle": "/usr/local/bin/ushuffle"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/fasta_ushuffle.
shpc-registry automated BioContainers addition for fasta_ushuffle
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/fasta_ushuffle
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/fasta_ushuffle:0.2--h031d066_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/fasta_ushuffle/0.2--h031d066_6
$ module help quay.io/biocontainers/fasta_ushuffle/0.2--h031d066_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### fasta_ushuffle-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### fasta_ushuffle-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### fasta_ushuffle-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### fasta_ushuffle-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### fasta_ushuffle-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### fasta_ushuffle-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### fasta_ushuffle

```bash
$ singularity exec <container> /usr/local/bin/fasta_ushuffle
$ podman run --it --rm --entrypoint /usr/local/bin/fasta_ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fasta_ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ushuffle

```bash
$ singularity exec <container> /usr/local/bin/ushuffle
$ podman run --it --rm --entrypoint /usr/local/bin/ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ushuffle   -v ${PWD} -w ${PWD} <container> -c " $@"
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