---
layout: container
name:  "quay.io/biocontainers/bioconductor-periodicdna"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-periodicdna/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-periodicdna/container.yaml"
updated_at: "2025-03-12 04:48:50.766134"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-periodicdna"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-periodicdna"
config: {"url": "https://biocontainers.pro/tools/bioconductor-periodicdna", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-periodicdna", "latest": {"1.16.0--r44hdfd78af_0": "sha256:18511f9bdc347d6535808ddf41a347b7a30a361304140e99522c564f3e191a03"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:d5fc613ea0e8bbb7841e5c28428f7d5d03a479d073ed810887115530119e00e7", "1.8.0--r42hdfd78af_0": "sha256:99aa4b0433563bee10b5b79390976ed5d47c1e9347dd636e8c27443ccaa28238", "1.10.0--r43hdfd78af_0": "sha256:78c42d234ddb57cc0b90fbb23e15c9679daaa65ef2a0d9832169cb1307f2ab22", "1.12.0--r43hdfd78af_0": "sha256:0c03fd20870772be97603fd9113f3ceeaa94778102bb68c3599fbf410bc98294", "1.16.0--r44hdfd78af_0": "sha256:18511f9bdc347d6535808ddf41a347b7a30a361304140e99522c564f3e191a03"}, "docker": "quay.io/biocontainers/bioconductor-periodicdna"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-periodicdna.
shpc-registry automated BioContainers addition for bioconductor-periodicdna
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-periodicdna
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-periodicdna:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-periodicdna/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-periodicdna/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-periodicdna-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-periodicdna-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-periodicdna-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-periodicdna-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-periodicdna-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-periodicdna-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-periodicdna

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