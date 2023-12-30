---
layout: container
name:  "quay.io/biocontainers/bioconductor-dvddata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dvddata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dvddata/container.yaml"
updated_at: "2023-12-30 02:46:08.843135"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dvddata"

versions:
 - "1.30.0--r41hdfd78af_1"
 - "1.33.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dvddata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dvddata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dvddata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:40f03a1b353465882dfaccbc71e426f15e806a32b41226fdaec4ad4e9883e0bc"}, "tags": {"1.30.0--r41hdfd78af_1": "sha256:56ce7efc91f34603c04bc9526cdf8a041d732e47aa3df7854cc2586f07fc7b35", "1.33.0--r42hdfd78af_0": "sha256:1f494c0155dbac8a168197ef3bf853d46ea6ab62be0847b67217f8be961867e5", "1.36.0--r43hdfd78af_0": "sha256:bbb9f1ddbeec8bc161a1f56839b50e72174bf3c28c95d811025ebc1bddb26347", "1.38.0--r43hdfd78af_0": "sha256:40f03a1b353465882dfaccbc71e426f15e806a32b41226fdaec4ad4e9883e0bc"}, "docker": "quay.io/biocontainers/bioconductor-dvddata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dvddata.
shpc-registry automated BioContainers addition for bioconductor-dvddata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dvddata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dvddata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dvddata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dvddata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dvddata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dvddata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dvddata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dvddata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dvddata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dvddata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dvddata

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