---
layout: container
name:  "quay.io/biocontainers/bioconductor-hthgu133bprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hthgu133bprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hthgu133bprobe/container.yaml"
updated_at: "2023-11-23 02:39:15.061672"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hthgu133bprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hthgu133bprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hthgu133bprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hthgu133bprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:5410ed03b8e4c22aa6a17eb84c06022bf7b39b5a46122c6eb189258eb7db30cb"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:0c561443a8357051973f5142937412c1ae664d7ff30152183d76e809aec1eb6a", "2.18.0--r42hdfd78af_11": "sha256:3ae8e12c0bff3604c27bc78dd271d42147320f4b3386970379ad83ea253b8ae1", "2.18.0--r43hdfd78af_12": "sha256:5410ed03b8e4c22aa6a17eb84c06022bf7b39b5a46122c6eb189258eb7db30cb"}, "docker": "quay.io/biocontainers/bioconductor-hthgu133bprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hthgu133bprobe.
shpc-registry automated BioContainers addition for bioconductor-hthgu133bprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133bprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hthgu133bprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hthgu133bprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hthgu133bprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hthgu133bprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133bprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hthgu133bprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hthgu133bprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hthgu133bprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hthgu133bprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hthgu133bprobe

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