---
layout: container
name:  "quay.io/biocontainers/bioconductor-frmaexampledata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-frmaexampledata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-frmaexampledata/container.yaml"
updated_at: "2025-12-14 04:15:47.671623"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-frmaexampledata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-frmaexampledata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-frmaexampledata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-frmaexampledata", "latest": {"1.42.0--r44hdfd78af_0": "sha256:2231266516d06e0fba08e7814335a89193287df83606ce98938e09a2315ad408"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:dfc734ac7dfe7c46f171284b02a74cfa5666153ce8cf6e7b282b6c2e397b5477", "1.33.0--r42hdfd78af_0": "sha256:17979361999e4e89d07da1eb40c96f459ab84676ce5cdc3d83cf1d5ff4621605", "1.36.0--r43hdfd78af_0": "sha256:4bcf50884aea4b1ae60629a6034880b7d90a6d3dbec6a511c5e40b9a4f834773", "1.38.0--r43hdfd78af_0": "sha256:c06ef0efa77679d6a812be174a5e1e7e9271363973049a2658e52e660af73ac8", "1.42.0--r44hdfd78af_0": "sha256:2231266516d06e0fba08e7814335a89193287df83606ce98938e09a2315ad408"}, "docker": "quay.io/biocontainers/bioconductor-frmaexampledata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-frmaexampledata.
shpc-registry automated BioContainers addition for bioconductor-frmaexampledata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-frmaexampledata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-frmaexampledata:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-frmaexampledata/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-frmaexampledata/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-frmaexampledata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-frmaexampledata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-frmaexampledata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-frmaexampledata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-frmaexampledata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-frmaexampledata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-frmaexampledata

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