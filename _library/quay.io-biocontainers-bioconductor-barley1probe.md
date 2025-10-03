---
layout: container
name:  "quay.io/biocontainers/bioconductor-barley1probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-barley1probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-barley1probe/container.yaml"
updated_at: "2025-10-03 03:02:02.885027"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-barley1probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-barley1probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-barley1probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-barley1probe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:d65e7f66ef12320e157d81910639aff4459093322bc56c109f67fbee4c10c05d"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:c0a20eb886ee3161cfe84ce95a69633b2822f2f241785a9512eae89fda92fff1", "2.18.0--r42hdfd78af_10": "sha256:0737e2a7a6a3a11f56e81c8029b2b341ddc97fe910d88381b5465a7f174a49ef", "2.18.0--r43hdfd78af_11": "sha256:a14cb34255b93578e64b49fb474afdd0f212eb07adc5175b183237cfe4f983e7", "2.18.0--r43hdfd78af_12": "sha256:a35fb5368112259944136ec7884367dc3f6db8014e2653ddd7f2beaf5239605a", "2.18.0--r44hdfd78af_13": "sha256:d65e7f66ef12320e157d81910639aff4459093322bc56c109f67fbee4c10c05d"}, "docker": "quay.io/biocontainers/bioconductor-barley1probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-barley1probe.
shpc-registry automated BioContainers addition for bioconductor-barley1probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-barley1probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-barley1probe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-barley1probe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-barley1probe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-barley1probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-barley1probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-barley1probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-barley1probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-barley1probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-barley1probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-barley1probe

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