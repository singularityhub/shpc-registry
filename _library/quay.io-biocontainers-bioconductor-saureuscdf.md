---
layout: container
name:  "quay.io/biocontainers/bioconductor-saureuscdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-saureuscdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-saureuscdf/container.yaml"
updated_at: "2023-08-04 03:09:31.552955"
latest: "2.18.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-saureuscdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-saureuscdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-saureuscdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-saureuscdf", "latest": {"2.18.0--r43hdfd78af_11": "sha256:7f489bfc24d0b4e263c721f5cdc393fd2d3a607687fdee4947978fac1db51ed1"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:589e9e85a501cf1747826441091c4f3c00baeb6f735405c024deb730697da284", "2.18.0--r42hdfd78af_10": "sha256:009a51371b3eb785409209ab88ffe3c0b41dedff5bdd1e4b4971c34085024ad1", "2.18.0--r43hdfd78af_11": "sha256:7f489bfc24d0b4e263c721f5cdc393fd2d3a607687fdee4947978fac1db51ed1"}, "docker": "quay.io/biocontainers/bioconductor-saureuscdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-saureuscdf.
shpc-registry automated BioContainers addition for bioconductor-saureuscdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-saureuscdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-saureuscdf:2.18.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-saureuscdf/2.18.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-saureuscdf/2.18.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-saureuscdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-saureuscdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-saureuscdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-saureuscdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-saureuscdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-saureuscdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-saureuscdf

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