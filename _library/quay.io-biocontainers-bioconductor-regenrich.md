---
layout: container
name:  "quay.io/biocontainers/bioconductor-regenrich"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-regenrich/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-regenrich/container.yaml"
updated_at: "2024-05-28 03:01:54.276211"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-regenrich"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-regenrich"
config: {"url": "https://biocontainers.pro/tools/bioconductor-regenrich", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-regenrich", "latest": {"1.10.0--r43hdfd78af_0": "sha256:95fb0448962242fde71d3ee6ba0716c8486afc2151eda21b5db61adbbc29617c"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:806564c719a5b70a680f7395c76e669957937d760781605b97e3ef72ee4bf8aa", "1.8.0--r42hdfd78af_0": "sha256:43a907bb5820f53b7edcdafd37a07af7d59b06d902bfe32e82b7753a892e89b7", "1.10.0--r43hdfd78af_0": "sha256:95fb0448962242fde71d3ee6ba0716c8486afc2151eda21b5db61adbbc29617c"}, "docker": "quay.io/biocontainers/bioconductor-regenrich"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-regenrich.
shpc-registry automated BioContainers addition for bioconductor-regenrich
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-regenrich
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-regenrich:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-regenrich/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-regenrich/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-regenrich-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regenrich-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-regenrich-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-regenrich-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-regenrich-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-regenrich-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-regenrich

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