---
layout: container
name:  "quay.io/biocontainers/bioconductor-tweedeseqcountdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tweedeseqcountdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tweedeseqcountdata/container.yaml"
updated_at: "2024-03-20 02:47:51.393048"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tweedeseqcountdata"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tweedeseqcountdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tweedeseqcountdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tweedeseqcountdata", "latest": {"1.38.0--r43hdfd78af_0": "sha256:79b1185bddbe5ba2ebcf19ff9d10827576b2d8010d39d2507def5ee5d8f335dd"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:0a063dfb7e484d887023a4ff33b8bd38c6afcdc8b4851d4c048da779648dbf40", "1.36.0--r42hdfd78af_0": "sha256:d240cbf12ced94353a9d3ddf02269e5f36b1603e0875a6ec6193d59b85ef69e2", "1.38.0--r43hdfd78af_0": "sha256:79b1185bddbe5ba2ebcf19ff9d10827576b2d8010d39d2507def5ee5d8f335dd"}, "docker": "quay.io/biocontainers/bioconductor-tweedeseqcountdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tweedeseqcountdata.
shpc-registry automated BioContainers addition for bioconductor-tweedeseqcountdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tweedeseqcountdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tweedeseqcountdata:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tweedeseqcountdata/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tweedeseqcountdata/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tweedeseqcountdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tweedeseqcountdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tweedeseqcountdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tweedeseqcountdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tweedeseqcountdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tweedeseqcountdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tweedeseqcountdata

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