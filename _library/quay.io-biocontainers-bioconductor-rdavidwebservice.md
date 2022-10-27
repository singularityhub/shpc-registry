---
layout: container
name:  "quay.io/biocontainers/bioconductor-rdavidwebservice"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rdavidwebservice/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rdavidwebservice/container.yaml"
updated_at: "2022-10-27 00:56:23.532407"
latest: "1.28.0--r40hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-rdavidwebservice"

versions:
 - "1.28.0--r40hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-rdavidwebservice"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rdavidwebservice", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rdavidwebservice", "latest": {"1.28.0--r40hdfd78af_1": "sha256:ccc535cd45b08fcbe6597e1cd9f0aefc820b953fc0c5e19bcb91691c5e038407"}, "tags": {"1.28.0--r40hdfd78af_1": "sha256:ccc535cd45b08fcbe6597e1cd9f0aefc820b953fc0c5e19bcb91691c5e038407"}, "docker": "quay.io/biocontainers/bioconductor-rdavidwebservice"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rdavidwebservice.
shpc-registry automated BioContainers addition for bioconductor-rdavidwebservice
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rdavidwebservice
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rdavidwebservice:1.28.0--r40hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rdavidwebservice/1.28.0--r40hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-rdavidwebservice/1.28.0--r40hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rdavidwebservice-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rdavidwebservice-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rdavidwebservice-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rdavidwebservice-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rdavidwebservice-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rdavidwebservice-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rdavidwebservice

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