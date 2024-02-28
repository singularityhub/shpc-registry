---
layout: container
name:  "quay.io/biocontainers/bioconductor-mu19ksubbcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mu19ksubbcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mu19ksubbcdf/container.yaml"
updated_at: "2024-02-28 02:26:10.768521"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mu19ksubbcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mu19ksubbcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mu19ksubbcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mu19ksubbcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:8f067247ac20cf9d1dc6d142c320f1c29482c4db9ac80d6bcdb9e188ee39965e"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:956ba0d7f5775075301a7f4e89a43b1daea7aab34dfc05497ea7d31312935807", "2.18.0--r42hdfd78af_10": "sha256:6daeaf2c15b26f596dccb9725ba47e36bf91b63eb614fafaa4484752642e951c", "2.18.0--r43hdfd78af_11": "sha256:5201928233ec562f8b4648bd7c265898c5d859f1b7f4703d23ee45c889746885", "2.18.0--r43hdfd78af_12": "sha256:8f067247ac20cf9d1dc6d142c320f1c29482c4db9ac80d6bcdb9e188ee39965e"}, "docker": "quay.io/biocontainers/bioconductor-mu19ksubbcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mu19ksubbcdf.
shpc-registry automated BioContainers addition for bioconductor-mu19ksubbcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubbcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mu19ksubbcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mu19ksubbcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mu19ksubbcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mu19ksubbcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubbcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mu19ksubbcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mu19ksubbcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mu19ksubbcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mu19ksubbcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mu19ksubbcdf

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