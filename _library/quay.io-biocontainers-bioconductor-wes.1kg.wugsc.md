---
layout: container
name:  "quay.io/biocontainers/bioconductor-wes.1kg.wugsc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-wes.1kg.wugsc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-wes.1kg.wugsc/container.yaml"
updated_at: "2023-07-06 03:36:48.556716"
latest: "1.29.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-wes.1kg.wugsc"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.29.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-wes.1kg.wugsc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-wes.1kg.wugsc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-wes.1kg.wugsc", "latest": {"1.29.0--r42hdfd78af_0": "sha256:c4d6811b7ea65754b1bcc8a362bdab326efcb415a32f3cb867e2dededf734d1f"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:ae22077dd3067c8096cc7c6d9ad0a9cdfd197f34c3ce98cc1664e3fcc17d957a", "1.29.0--r42hdfd78af_0": "sha256:c4d6811b7ea65754b1bcc8a362bdab326efcb415a32f3cb867e2dededf734d1f"}, "docker": "quay.io/biocontainers/bioconductor-wes.1kg.wugsc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-wes.1kg.wugsc.
shpc-registry automated BioContainers addition for bioconductor-wes.1kg.wugsc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-wes.1kg.wugsc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-wes.1kg.wugsc:1.29.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-wes.1kg.wugsc/1.29.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-wes.1kg.wugsc/1.29.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-wes.1kg.wugsc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wes.1kg.wugsc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-wes.1kg.wugsc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-wes.1kg.wugsc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-wes.1kg.wugsc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-wes.1kg.wugsc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-wes.1kg.wugsc

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