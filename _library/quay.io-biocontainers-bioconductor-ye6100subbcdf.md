---
layout: container
name:  "quay.io/biocontainers/bioconductor-ye6100subbcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ye6100subbcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ye6100subbcdf/container.yaml"
updated_at: "2024-07-04 04:10:45.953862"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-ye6100subbcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-ye6100subbcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ye6100subbcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ye6100subbcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:f70658a0bdd3a072c3630908e0754d96e540dc620d259b6a93008cb96a042d03"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:ef6710409b0ccd73da5143cb16280368dd7a6813cf64a5d390fee2b5a705c2e9", "2.18.0--r42hdfd78af_10": "sha256:3c9d312131433bf2e20e96d195af4c214311d795cfe40f8955a37bd364149390", "2.18.0--r43hdfd78af_11": "sha256:cf02334a79920ba7a5b56ced3a9117f10475711a7c6fe95cfbaadfb603be2092", "2.18.0--r43hdfd78af_12": "sha256:f70658a0bdd3a072c3630908e0754d96e540dc620d259b6a93008cb96a042d03"}, "docker": "quay.io/biocontainers/bioconductor-ye6100subbcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ye6100subbcdf.
shpc-registry automated BioContainers addition for bioconductor-ye6100subbcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ye6100subbcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ye6100subbcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ye6100subbcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-ye6100subbcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ye6100subbcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ye6100subbcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ye6100subbcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ye6100subbcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ye6100subbcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ye6100subbcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ye6100subbcdf

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