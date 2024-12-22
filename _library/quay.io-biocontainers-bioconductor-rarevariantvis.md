---
layout: container
name:  "quay.io/biocontainers/bioconductor-rarevariantvis"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rarevariantvis/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rarevariantvis/container.yaml"
updated_at: "2024-12-22 03:40:48.912024"
latest: "2.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rarevariantvis"
aliases:
 - "wget"
versions:
 - "2.8.0--r351_0"
 - "2.26.0--r42hdfd78af_0"
 - "2.22.0--r41hdfd78af_0"
 - "2.20.0--r41hdfd78af_0"
 - "2.18.0--r40hdfd78af_1"
 - "2.16.0--r40_0"
 - "2.28.0--r43hdfd78af_0"
 - "2.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rarevariantvis"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rarevariantvis", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rarevariantvis", "latest": {"2.30.0--r43hdfd78af_0": "sha256:695b25e332f605cb58f07bc14c95481a223b41484a00dd6f4599517857e26ded"}, "tags": {"2.8.0--r351_0": "sha256:1f1eb9a7b5b313e9321ca8830a4007521511d0801052b4026c46eb119bdd9a0e", "2.26.0--r42hdfd78af_0": "sha256:d9d62d8d469dcc95353ab236aebeccf4284870884b9575e6880b5227f36f1438", "2.22.0--r41hdfd78af_0": "sha256:5c55fb17d4de01d0971ab57c93e990886dc45e458c3ab1a72a2f50b807b1d9f6", "2.20.0--r41hdfd78af_0": "sha256:5ec4aa17d33e9cb5b14e053d4681484f4c0b5fb6f94de57f0d2477829f133791", "2.18.0--r40hdfd78af_1": "sha256:fa545df8692c4cfd46cb9d597a51130886661aef3995d1c62e2eff80be087af3", "2.16.0--r40_0": "sha256:76d619efa5759cf6876f3e4888a33866301c3154d321c151cf178499f3a732d0", "2.28.0--r43hdfd78af_0": "sha256:58a0b80f4b6f92681a634d62e79640e2927abe744c409def2b24f0a1b0be1183", "2.30.0--r43hdfd78af_0": "sha256:695b25e332f605cb58f07bc14c95481a223b41484a00dd6f4599517857e26ded"}, "docker": "quay.io/biocontainers/bioconductor-rarevariantvis", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rarevariantvis.
shpc-registry automated BioContainers addition for bioconductor-rarevariantvis
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rarevariantvis
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rarevariantvis:2.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rarevariantvis/2.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rarevariantvis/2.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rarevariantvis-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rarevariantvis-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rarevariantvis-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rarevariantvis-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rarevariantvis-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rarevariantvis-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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