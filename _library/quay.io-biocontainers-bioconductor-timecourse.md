---
layout: container
name:  "quay.io/biocontainers/bioconductor-timecourse"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-timecourse/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-timecourse/container.yaml"
updated_at: "2023-12-25 03:05:06.854573"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-timecourse"

versions:
 - "1.66.0--r41hdfd78af_0"
 - "1.70.0--r42hdfd78af_0"
 - "1.72.0--r43hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-timecourse"
config: {"url": "https://biocontainers.pro/tools/bioconductor-timecourse", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-timecourse", "latest": {"1.74.0--r43hdfd78af_0": "sha256:9b7b9352045c55bd1294006c1fd6205bd7c7a801d52efc3cc0cacf6a01ddc4df"}, "tags": {"1.66.0--r41hdfd78af_0": "sha256:ce32d2d93957fbdca9b4283c6e35084c88afe3416b201ba5c61fe1955a1d0de5", "1.70.0--r42hdfd78af_0": "sha256:7f3173680319d2f4e09faeb942163a1bf031d8e4efca638f55b9ef8cdd638449", "1.72.0--r43hdfd78af_0": "sha256:84956c8beba7fe4dea449119aa08b3dcb3e2a0286255efcb27b42c924bf748ec", "1.74.0--r43hdfd78af_0": "sha256:9b7b9352045c55bd1294006c1fd6205bd7c7a801d52efc3cc0cacf6a01ddc4df"}, "docker": "quay.io/biocontainers/bioconductor-timecourse"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-timecourse.
shpc-registry automated BioContainers addition for bioconductor-timecourse
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-timecourse
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-timecourse:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-timecourse/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-timecourse/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-timecourse-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-timecourse-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-timecourse-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-timecourse-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-timecourse-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-timecourse-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-timecourse

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