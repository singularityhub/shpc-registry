---
layout: container
name:  "quay.io/biocontainers/bioconductor-trajectorygeometry"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-trajectorygeometry/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-trajectorygeometry/container.yaml"
updated_at: "2024-08-17 03:06:34.538144"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-trajectorygeometry"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-trajectorygeometry"
config: {"url": "https://biocontainers.pro/tools/bioconductor-trajectorygeometry", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-trajectorygeometry", "latest": {"1.10.0--r43hdfd78af_0": "sha256:f069db8c4127eb25b3a918f2611d1349cf88a992f56d538d9d0999976e90c121"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:67a1b5ec12277fac7cbcfff3909299a85ff356cfb1656380ba08cbc0c06c7fbd", "1.6.0--r42hdfd78af_0": "sha256:bfa370f7f10a1c36ed69c26b746a6d33dabeba7bf689471c2586963eb179c79d", "1.8.0--r43hdfd78af_0": "sha256:64b4d9ffcebcedeeb8205c1c25a30fdf4a15870368929f6912cec3c5a73b85c5", "1.10.0--r43hdfd78af_0": "sha256:f069db8c4127eb25b3a918f2611d1349cf88a992f56d538d9d0999976e90c121"}, "docker": "quay.io/biocontainers/bioconductor-trajectorygeometry"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-trajectorygeometry.
shpc-registry automated BioContainers addition for bioconductor-trajectorygeometry
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-trajectorygeometry
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-trajectorygeometry:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-trajectorygeometry/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-trajectorygeometry/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-trajectorygeometry-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trajectorygeometry-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trajectorygeometry-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-trajectorygeometry-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-trajectorygeometry-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-trajectorygeometry-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-trajectorygeometry

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