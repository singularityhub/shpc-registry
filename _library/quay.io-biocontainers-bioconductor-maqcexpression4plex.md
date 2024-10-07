---
layout: container
name:  "quay.io/biocontainers/bioconductor-maqcexpression4plex"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maqcexpression4plex/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maqcexpression4plex/container.yaml"
updated_at: "2024-10-07 03:26:02.379799"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-maqcexpression4plex"

versions:
 - "1.38.0--r41hdfd78af_1"
 - "1.41.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-maqcexpression4plex"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maqcexpression4plex", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maqcexpression4plex", "latest": {"1.46.0--r43hdfd78af_0": "sha256:c01092b8d55be74061679e01ac9bf4d92c2df2ae363a12a91f05f044855f8fb1"}, "tags": {"1.38.0--r41hdfd78af_1": "sha256:4bd24c105de6e22b8b5014b54bd4b00b6fe55b47b8e8ab65c204b541c7484b20", "1.41.0--r42hdfd78af_0": "sha256:b331b00ffd9bde0b558f8474fb92eb77f5291b1c614eaec3c4dcdabe442efb81", "1.44.0--r43hdfd78af_0": "sha256:ff974d83b5c76412e11f4d2c673181cc02d03503aad4d332d7551079f6718b8c", "1.46.0--r43hdfd78af_0": "sha256:c01092b8d55be74061679e01ac9bf4d92c2df2ae363a12a91f05f044855f8fb1"}, "docker": "quay.io/biocontainers/bioconductor-maqcexpression4plex"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maqcexpression4plex.
shpc-registry automated BioContainers addition for bioconductor-maqcexpression4plex
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maqcexpression4plex
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maqcexpression4plex:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maqcexpression4plex/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-maqcexpression4plex/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maqcexpression4plex-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maqcexpression4plex-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maqcexpression4plex-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maqcexpression4plex-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maqcexpression4plex-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maqcexpression4plex-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-maqcexpression4plex

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