---
layout: container
name:  "quay.io/biocontainers/bioconductor-snapcount"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snapcount/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snapcount/container.yaml"
updated_at: "2024-12-19 03:40:29.163597"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-snapcount"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-snapcount"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snapcount", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snapcount", "latest": {"1.14.0--r43hdfd78af_0": "sha256:8c204f4a79f9e95a62f6bcf01ffe254efb8794c013666f62025cdec46b95a0b8"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:5e39dd10e3d117d1ef47ee28bd452bb8672c6058bb4e4164d978bc5e662abcad", "1.10.0--r42hdfd78af_0": "sha256:408bdf0b4473f499f87e66305aff5e3996c0de13e48d8888793361b6f6722a15", "1.12.0--r43hdfd78af_0": "sha256:8a8c4bc800741d0240ec13dbd5ca080052d3ea14ce995f028cc22bd5d2aabffb", "1.14.0--r43hdfd78af_0": "sha256:8c204f4a79f9e95a62f6bcf01ffe254efb8794c013666f62025cdec46b95a0b8"}, "docker": "quay.io/biocontainers/bioconductor-snapcount"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snapcount.
shpc-registry automated BioContainers addition for bioconductor-snapcount
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snapcount
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snapcount:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snapcount/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-snapcount/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snapcount-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snapcount-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snapcount-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snapcount-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snapcount-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snapcount-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-snapcount

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