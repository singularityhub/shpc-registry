---
layout: container
name:  "quay.io/biocontainers/bioconductor-human370quadv3ccrlmm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-human370quadv3ccrlmm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-human370quadv3ccrlmm/container.yaml"
updated_at: "2024-11-19 03:05:21.639368"
latest: "1.0.3--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-human370quadv3ccrlmm"

versions:
 - "1.0.3--r41hdfd78af_9"
 - "1.0.3--r42hdfd78af_10"
 - "1.0.3--r43hdfd78af_11"
 - "1.0.3--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-human370quadv3ccrlmm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-human370quadv3ccrlmm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-human370quadv3ccrlmm", "latest": {"1.0.3--r43hdfd78af_12": "sha256:4cee6531e982350262dec99a662f70198aeeb55bbad7de1dcf33351b5b5b6d59"}, "tags": {"1.0.3--r41hdfd78af_9": "sha256:53c5e270ce3ae6d895ea2cc78c974be778f80fd8934ac72649dcdadd92e24b59", "1.0.3--r42hdfd78af_10": "sha256:80b09e7b9ccc6b213e8efa8c272256b630269eee80dccc3ce576f6999e0664d8", "1.0.3--r43hdfd78af_11": "sha256:7291670708a11ebbfa91db4ae3cb41fe878655013ec83642f75a330986a4db9c", "1.0.3--r43hdfd78af_12": "sha256:4cee6531e982350262dec99a662f70198aeeb55bbad7de1dcf33351b5b5b6d59"}, "docker": "quay.io/biocontainers/bioconductor-human370quadv3ccrlmm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-human370quadv3ccrlmm.
shpc-registry automated BioContainers addition for bioconductor-human370quadv3ccrlmm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-human370quadv3ccrlmm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-human370quadv3ccrlmm:1.0.3--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-human370quadv3ccrlmm/1.0.3--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-human370quadv3ccrlmm/1.0.3--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-human370quadv3ccrlmm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human370quadv3ccrlmm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-human370quadv3ccrlmm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-human370quadv3ccrlmm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-human370quadv3ccrlmm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-human370quadv3ccrlmm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-human370quadv3ccrlmm

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