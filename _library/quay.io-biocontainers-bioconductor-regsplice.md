---
layout: container
name:  "quay.io/biocontainers/bioconductor-regsplice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-regsplice/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-regsplice/container.yaml"
updated_at: "2025-03-07 03:13:40.632297"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-regsplice"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-regsplice"
config: {"url": "https://biocontainers.pro/tools/bioconductor-regsplice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-regsplice", "latest": {"1.32.0--r44hdfd78af_0": "sha256:debdfe74e9a38d8b965884fff44b1d43f54f1f1a0f0ec0ccea981a9a7cbae0f7"}, "tags": {"1.8.0--r351_0": "sha256:630b8874218256948cca924788ec6f39fa8d1ae79e4f7af04234912799af1aeb", "1.24.0--r42hdfd78af_0": "sha256:fa769052e0c3ca611b4d121feeb21982b2e90dcb8d7d1ff3c15463aac2c6fd53", "1.20.0--r41hdfd78af_0": "sha256:dd696425441a48a0af5cad4f7b08c360ed40b42078b75249c1f6b9ebb99a8602", "1.18.0--r41hdfd78af_0": "sha256:5b85991a60b4e33c2040d92f17dd5c96956532047d2d0e33ea560d68aaef51aa", "1.16.0--r40hdfd78af_1": "sha256:c68475896c4b6ceac49e526cb7e725fcb6a379163842a6a459089aaec968c67b", "1.14.0--r40_0": "sha256:4d53e31df28dacfae4968b9f7fcdf9bc5548f8f6f88f5dc28ef19d69596b5d93", "1.26.0--r43hdfd78af_0": "sha256:d8d34f785f6610712906e7aa79947ab6cd3800de09a00d05a2f1b340dd4a3931", "1.28.0--r43hdfd78af_0": "sha256:9d27bac5307b3ec18937c1f14ac04b14ab0c5a7ed7d920f896754fc4ce83e490", "1.32.0--r44hdfd78af_0": "sha256:debdfe74e9a38d8b965884fff44b1d43f54f1f1a0f0ec0ccea981a9a7cbae0f7"}, "docker": "quay.io/biocontainers/bioconductor-regsplice", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-regsplice.
shpc-registry automated BioContainers addition for bioconductor-regsplice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-regsplice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-regsplice:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-regsplice/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-regsplice/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-regsplice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regsplice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regsplice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-regsplice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-regsplice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-regsplice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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