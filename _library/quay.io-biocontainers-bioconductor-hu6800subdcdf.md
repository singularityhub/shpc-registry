---
layout: container
name:  "quay.io/biocontainers/bioconductor-hu6800subdcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hu6800subdcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hu6800subdcdf/container.yaml"
updated_at: "2024-10-23 03:21:26.187862"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hu6800subdcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hu6800subdcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hu6800subdcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hu6800subdcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:46315b0a8b9e0932b98ddcc52cc25d80364d4475a840d85a10c67dc6c561542f"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:231f0fee5309df8a8baf4b683bff4be22b73ea822647884f8e52af9bd886e3de", "2.18.0--r42hdfd78af_10": "sha256:de8d901523a0e632b16989651e42e626f0d28d72f86771d67c4079f00a9210a0", "2.18.0--r43hdfd78af_11": "sha256:d113d638956232f038381c7f63c9a08daa8517c3a0ddcf0b705f9f1f13e3270b", "2.18.0--r43hdfd78af_12": "sha256:46315b0a8b9e0932b98ddcc52cc25d80364d4475a840d85a10c67dc6c561542f"}, "docker": "quay.io/biocontainers/bioconductor-hu6800subdcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hu6800subdcdf.
shpc-registry automated BioContainers addition for bioconductor-hu6800subdcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800subdcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800subdcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hu6800subdcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hu6800subdcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hu6800subdcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800subdcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800subdcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hu6800subdcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hu6800subdcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hu6800subdcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hu6800subdcdf

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