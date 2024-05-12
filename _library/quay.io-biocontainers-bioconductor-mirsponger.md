---
layout: container
name:  "quay.io/biocontainers/bioconductor-mirsponger"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mirsponger/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mirsponger/container.yaml"
updated_at: "2024-05-12 02:43:45.778663"
latest: "2.4.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mirsponger"
aliases:
 - "glpsol"
versions:
 - "1.20.1--r41hc247a5b_1"
 - "2.2.0--r42hc247a5b_0"
 - "2.2.0--r42hf17093f_1"
 - "2.4.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mirsponger"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mirsponger", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mirsponger", "latest": {"2.4.0--r43hf17093f_0": "sha256:920646860b1ff182031aa589a577c07d268a78c8f08c029701922bc61042a8f7"}, "tags": {"1.20.1--r41hc247a5b_1": "sha256:f8708faad531ebb77657c78a7aa02bc4b8ea9a9449370e633a9367b07972ce57", "2.2.0--r42hc247a5b_0": "sha256:63c5c4ddf17990837b1e689b9b62ea01a98a7788044b6469e0f482c21baf1f81", "2.2.0--r42hf17093f_1": "sha256:4b8760e4779b32d32cd2cad2861b133c4a684c620740ebd4ab6274b481ed5eaf", "2.4.0--r43hf17093f_0": "sha256:920646860b1ff182031aa589a577c07d268a78c8f08c029701922bc61042a8f7"}, "docker": "quay.io/biocontainers/bioconductor-mirsponger", "aliases": {"glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mirsponger.
shpc-registry automated BioContainers addition for bioconductor-mirsponger
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mirsponger
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mirsponger:2.4.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mirsponger/2.4.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-mirsponger/2.4.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mirsponger-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirsponger-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mirsponger-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mirsponger-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mirsponger-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mirsponger-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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