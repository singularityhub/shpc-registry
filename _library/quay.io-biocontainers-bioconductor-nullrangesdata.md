---
layout: container
name:  "quay.io/biocontainers/bioconductor-nullrangesdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nullrangesdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nullrangesdata/container.yaml"
updated_at: "2023-02-17 03:33:50.329780"
latest: "1.4.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nullrangesdata"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.4.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nullrangesdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nullrangesdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nullrangesdata", "latest": {"1.4.0--r42hdfd78af_0": "sha256:879c0efd1e9bde6ca063ddb32c8ec937181ec9f951d4b596882204c47fdc3ea9"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:897069788213acf60d8430292d3f72d2757fe26e576c890d1dc05acacce414ee", "1.4.0--r42hdfd78af_0": "sha256:879c0efd1e9bde6ca063ddb32c8ec937181ec9f951d4b596882204c47fdc3ea9"}, "docker": "quay.io/biocontainers/bioconductor-nullrangesdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nullrangesdata.
shpc-registry automated BioContainers addition for bioconductor-nullrangesdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nullrangesdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nullrangesdata:1.4.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nullrangesdata/1.4.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nullrangesdata/1.4.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nullrangesdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nullrangesdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nullrangesdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nullrangesdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nullrangesdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nullrangesdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nullrangesdata

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