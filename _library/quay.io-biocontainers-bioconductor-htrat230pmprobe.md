---
layout: container
name:  "quay.io/biocontainers/bioconductor-htrat230pmprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-htrat230pmprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-htrat230pmprobe/container.yaml"
updated_at: "2024-02-27 02:33:02.853237"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-htrat230pmprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-htrat230pmprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-htrat230pmprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-htrat230pmprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:1c3f4e8cfd9cd8a044b6ca278c839789d5516006013c539cba8ac0b190f63043"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:59bcdd084d22e3a3cbf29c0fba7ca4b1c401579ed7910e7bc14e9b1dee5b081c", "2.18.0--r42hdfd78af_10": "sha256:24b34948cb5f5e1f8f3b9811c78c6f8b14833e054f52c45df26d12a6904e5f4a", "2.18.0--r43hdfd78af_11": "sha256:7df6ca07fd6c07e67e6a9adcc5176fedb2d3203f0be97bbe8cd617b6066a9961", "2.18.0--r43hdfd78af_12": "sha256:1c3f4e8cfd9cd8a044b6ca278c839789d5516006013c539cba8ac0b190f63043"}, "docker": "quay.io/biocontainers/bioconductor-htrat230pmprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-htrat230pmprobe.
shpc-registry automated BioContainers addition for bioconductor-htrat230pmprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-htrat230pmprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-htrat230pmprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-htrat230pmprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-htrat230pmprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-htrat230pmprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htrat230pmprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-htrat230pmprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-htrat230pmprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-htrat230pmprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-htrat230pmprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-htrat230pmprobe

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