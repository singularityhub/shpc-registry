---
layout: container
name:  "quay.io/biocontainers/bioconductor-fscanr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fscanr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fscanr/container.yaml"
updated_at: "2023-10-08 03:10:40.808738"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fscanr"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fscanr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fscanr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fscanr", "latest": {"1.10.0--r43hdfd78af_0": "sha256:768aa38242d132ba8eef17eada72eb2b6dc6f91750ec2b5b7c0e0d4a07fdd8f8"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:c7ba85a2d37689acbeabbaeb2f8160ae7b89c7de5139255b0ee16778391589b9", "1.8.0--r42hdfd78af_0": "sha256:5252fe04429357d83f487a2941dc75dc4148d452546efae95088fc985958741a", "1.10.0--r43hdfd78af_0": "sha256:768aa38242d132ba8eef17eada72eb2b6dc6f91750ec2b5b7c0e0d4a07fdd8f8"}, "docker": "quay.io/biocontainers/bioconductor-fscanr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fscanr.
shpc-registry automated BioContainers addition for bioconductor-fscanr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fscanr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fscanr:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fscanr/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fscanr/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fscanr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fscanr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fscanr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fscanr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fscanr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fscanr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fscanr

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