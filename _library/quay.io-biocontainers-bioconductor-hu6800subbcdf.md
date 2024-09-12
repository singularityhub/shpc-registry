---
layout: container
name:  "quay.io/biocontainers/bioconductor-hu6800subbcdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hu6800subbcdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hu6800subbcdf/container.yaml"
updated_at: "2024-09-12 17:21:19.076889"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hu6800subbcdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hu6800subbcdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hu6800subbcdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hu6800subbcdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:2549448faac0389fcd61f0e504c11bb351d44b3e8d180eafd854dc5f9baca1d3"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:c3773efaae946318ea55422d5f053b7f6dfd810c8b1b5498b1c3864cc9b39be8", "2.18.0--r42hdfd78af_10": "sha256:94319b3a99e2857eff35144b33120792e5976bbee60c07d979d54f1075c7c730", "2.18.0--r43hdfd78af_11": "sha256:585033fddae3d15f8e40c2e51899e756daa08e657422adb1de787f40e8554090", "2.18.0--r43hdfd78af_12": "sha256:2549448faac0389fcd61f0e504c11bb351d44b3e8d180eafd854dc5f9baca1d3"}, "docker": "quay.io/biocontainers/bioconductor-hu6800subbcdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hu6800subbcdf.
shpc-registry automated BioContainers addition for bioconductor-hu6800subbcdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800subbcdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hu6800subbcdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hu6800subbcdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hu6800subbcdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hu6800subbcdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800subbcdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu6800subbcdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hu6800subbcdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hu6800subbcdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hu6800subbcdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hu6800subbcdf

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