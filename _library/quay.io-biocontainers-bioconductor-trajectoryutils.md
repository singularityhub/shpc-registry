---
layout: container
name:  "quay.io/biocontainers/bioconductor-trajectoryutils"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-trajectoryutils/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-trajectoryutils/container.yaml"
updated_at: "2025-02-15 03:29:16.244921"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-trajectoryutils"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-trajectoryutils"
config: {"url": "https://biocontainers.pro/tools/bioconductor-trajectoryutils", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-trajectoryutils", "latest": {"1.14.0--r44hdfd78af_0": "sha256:904bc981d91b867aa53a307de1265304e2ddb2d246607e31a62d4b5352e85142"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:d99f95c7da52371fea4cd36ab8299142c4b6a6ec289d9a09a33adc1d2d39f9f1", "1.6.0--r42hdfd78af_0": "sha256:080888683cc123b6fa30cbd4ec25a19daf52a14a486acf7c59be34c513c99f26", "1.8.0--r43hdfd78af_0": "sha256:94a1bfc83633e1f84c387ead3b1a02508e1487eb82c9e449e224be808cb59be3", "1.10.0--r43hdfd78af_0": "sha256:c7f92e9d9ba33bfbeccd7617dc33ba38219c4a3d0e5b6f97444c2266230d1819", "1.14.0--r44hdfd78af_0": "sha256:904bc981d91b867aa53a307de1265304e2ddb2d246607e31a62d4b5352e85142"}, "docker": "quay.io/biocontainers/bioconductor-trajectoryutils"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-trajectoryutils.
shpc-registry automated BioContainers addition for bioconductor-trajectoryutils
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-trajectoryutils
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-trajectoryutils:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-trajectoryutils/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-trajectoryutils/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-trajectoryutils-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trajectoryutils-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-trajectoryutils-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-trajectoryutils-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-trajectoryutils-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-trajectoryutils-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-trajectoryutils

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