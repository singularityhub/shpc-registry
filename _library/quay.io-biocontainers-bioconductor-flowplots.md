---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowplots"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowplots/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowplots/container.yaml"
updated_at: "2025-10-15 03:34:13.456407"
latest: "1.54.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowplots"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.54.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowplots"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowplots", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowplots", "latest": {"1.54.0--r44hdfd78af_0": "sha256:2546951be42b3cb514d5a0073054266a3288326b5dfd4e52c6c5e17d7e08fa32"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:6ea6f9a9c89f7e310761354fa30eda014ae3ca8137e143bd1136d6b1e59dd631", "1.46.0--r42hdfd78af_0": "sha256:2b93832564ed1bf797e0b3fa27e1fcdd74933e7fe02e031731bafd3935fc636c", "1.48.0--r43hdfd78af_0": "sha256:727936a2e1e325ce3adabc7c374084f1ffe3f283ab7bf99be05b747625c2ece9", "1.50.0--r43hdfd78af_0": "sha256:309d6850be3e150f03c616a5f52432942ea7864e8af99bee722cf82c7da0b636", "1.54.0--r44hdfd78af_0": "sha256:2546951be42b3cb514d5a0073054266a3288326b5dfd4e52c6c5e17d7e08fa32"}, "docker": "quay.io/biocontainers/bioconductor-flowplots"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowplots.
shpc-registry automated BioContainers addition for bioconductor-flowplots
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowplots
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowplots:1.54.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowplots/1.54.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowplots/1.54.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowplots-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowplots-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowplots-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowplots-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowplots-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowplots-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowplots

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