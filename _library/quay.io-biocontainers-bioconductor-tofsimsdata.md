---
layout: container
name:  "quay.io/biocontainers/bioconductor-tofsimsdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tofsimsdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tofsimsdata/container.yaml"
updated_at: "2023-10-02 02:45:46.556697"
latest: "1.26.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tofsimsdata"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.26.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tofsimsdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tofsimsdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tofsimsdata", "latest": {"1.26.0--r42hdfd78af_0": "sha256:0da80b4ff076b66ea8379365d85d6af64edf2c8174d5c9c31db21473273065a3"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:99a92d02f0069c86f13bb1c1d0e28b63246a6a59afd0909e4cf0b4d08c74f409", "1.26.0--r42hdfd78af_0": "sha256:0da80b4ff076b66ea8379365d85d6af64edf2c8174d5c9c31db21473273065a3"}, "docker": "quay.io/biocontainers/bioconductor-tofsimsdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tofsimsdata.
shpc-registry automated BioContainers addition for bioconductor-tofsimsdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tofsimsdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tofsimsdata:1.26.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tofsimsdata/1.26.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tofsimsdata/1.26.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tofsimsdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tofsimsdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tofsimsdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tofsimsdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tofsimsdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tofsimsdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tofsimsdata

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