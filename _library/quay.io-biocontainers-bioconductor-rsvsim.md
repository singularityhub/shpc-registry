---
layout: container
name:  "quay.io/biocontainers/bioconductor-rsvsim"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rsvsim/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rsvsim/container.yaml"
updated_at: "2025-11-14 05:26:22.442982"
latest: "1.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-rsvsim"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-rsvsim"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rsvsim", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rsvsim", "latest": {"1.46.0--r44hdfd78af_0": "sha256:88281478daa998786ea9fed80c45bf5679fc1d6df5b75d9a3b6f74a286d7907c"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:0cfede6bcf00bc476d226edc08e39f4f184dfed4f25cde1b2fc844b1aedcff85", "1.38.0--r42hdfd78af_0": "sha256:db18a070c9c0006e7c04162a7a4741d7bf074e016086e6f21b8e6405b5d748d4", "1.40.0--r43hdfd78af_0": "sha256:192c01fce02748bff513563b3ac09dd11817349381e812771899fb27ef4e1406", "1.42.0--r43hdfd78af_0": "sha256:1b9a1dd94ec9aa60ec82d73011a2847e33348f9ff7e0ae5428b88785379b1150", "1.46.0--r44hdfd78af_0": "sha256:88281478daa998786ea9fed80c45bf5679fc1d6df5b75d9a3b6f74a286d7907c"}, "docker": "quay.io/biocontainers/bioconductor-rsvsim"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rsvsim.
shpc-registry automated BioContainers addition for bioconductor-rsvsim
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rsvsim
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rsvsim:1.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rsvsim/1.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-rsvsim/1.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rsvsim-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsvsim-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rsvsim-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rsvsim-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rsvsim-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rsvsim-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rsvsim

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