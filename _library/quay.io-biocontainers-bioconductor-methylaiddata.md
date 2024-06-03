---
layout: container
name:  "quay.io/biocontainers/bioconductor-methylaiddata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-methylaiddata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-methylaiddata/container.yaml"
updated_at: "2024-06-03 02:35:43.302967"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-methylaiddata"

versions:
 - "1.26.0--r41hdfd78af_1"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-methylaiddata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-methylaiddata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-methylaiddata", "latest": {"1.34.0--r43hdfd78af_0": "sha256:ee66cc3a097af7482d61c856b236d71ccf4e7f2d5a26d77d3599445c1728c9dd"}, "tags": {"1.26.0--r41hdfd78af_1": "sha256:65932b71b54d6e5348fdf8428c918bbdb95bc8d9a1ad7f231ee59cdc34ad100a", "1.30.0--r42hdfd78af_0": "sha256:4e15c57cd59d286880d006e42242d213113fb0ab0ade6e1ff0e7ee8cb6737ef9", "1.32.0--r43hdfd78af_0": "sha256:47f3dadb6274f5a3b651c083453ba13f13ecb4d8cccc738ea27dd47f7969e6a8", "1.34.0--r43hdfd78af_0": "sha256:ee66cc3a097af7482d61c856b236d71ccf4e7f2d5a26d77d3599445c1728c9dd"}, "docker": "quay.io/biocontainers/bioconductor-methylaiddata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-methylaiddata.
shpc-registry automated BioContainers addition for bioconductor-methylaiddata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-methylaiddata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-methylaiddata:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-methylaiddata/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-methylaiddata/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-methylaiddata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylaiddata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-methylaiddata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-methylaiddata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-methylaiddata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-methylaiddata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-methylaiddata

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