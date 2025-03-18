---
layout: container
name:  "quay.io/biocontainers/bioconductor-switchde"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-switchde/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-switchde/container.yaml"
updated_at: "2025-03-18 03:43:58.851035"
latest: "1.32.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-switchde"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.12.0--r36_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.32.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-switchde"
config: {"url": "https://biocontainers.pro/tools/bioconductor-switchde", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-switchde", "latest": {"1.32.0--r44hdfd78af_0": "sha256:447f89882f20105f0bd157426e7c2e8ce292783b54be47360f59cffa0fa192e8"}, "tags": {"1.8.0--r351_0": "sha256:d4384560777222e818f7c1d0a78be44376b13d531a545f6d6f12a5b89910180f", "1.20.0--r41hdfd78af_0": "sha256:4a1139066b2a1e465b2bedecf11f7f788dcd2b5e21fc009828273aa03331012f", "1.18.0--r41hdfd78af_0": "sha256:2bdfb9fe29530e9d5308e566b4bee317b4b215969bb0ed38ebe017eb47846b47", "1.16.0--r40hdfd78af_1": "sha256:c04a05ba83aff6dcd792af81381d926fea768f9096df8cccfc8d73afb620159a", "1.14.0--r40_0": "sha256:7ec6d17d0f2e64fd2bda87ffbbdd627982089929fc71f6f24a564cfe27bbbb6b", "1.12.0--r36_0": "sha256:8768ec02147f2d2101baffaaae1ff188af7cb2e1fbdea647ed16bc24f34d841b", "1.24.0--r42hdfd78af_0": "sha256:628aeda99b6a27c82d4196ead89f70b6f24383d1338d7b7c95ec3da957bbc5c3", "1.26.0--r43hdfd78af_0": "sha256:9e21153eea1347c1ecf50a6bab548725e0bddcd3ada00b67b23d271403b00ea7", "1.28.0--r43hdfd78af_0": "sha256:ce56b220f824ec6d2a48ac380075b603ef88ce59b1e8fe90434abeadd3431aa5", "1.32.0--r44hdfd78af_0": "sha256:447f89882f20105f0bd157426e7c2e8ce292783b54be47360f59cffa0fa192e8"}, "docker": "quay.io/biocontainers/bioconductor-switchde", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-switchde.
shpc-registry automated BioContainers addition for bioconductor-switchde
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-switchde
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-switchde:1.32.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-switchde/1.32.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-switchde/1.32.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-switchde-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-switchde-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-switchde-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-switchde-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-switchde-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-switchde-inspect-deffile:

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