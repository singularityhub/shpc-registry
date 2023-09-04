---
layout: container
name:  "quay.io/biocontainers/bioconductor-geosubmission"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geosubmission/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geosubmission/container.yaml"
updated_at: "2023-09-04 04:31:18.137273"
latest: "1.52.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geosubmission"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geosubmission"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geosubmission", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geosubmission", "latest": {"1.52.0--r43hdfd78af_0": "sha256:b8ca0c6a3bdd8074ef1217270959a2d8055344b91b7be656b45461813fdfbc2c"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:6aae8b86c44cfd518f51e280a97a32402381db6a8b0403c6e2b766bb4acc2ee3", "1.50.0--r42hdfd78af_0": "sha256:be91079fb87d30d9d55214085664fa8413cc0d9b29dcd405ef93b95584e90bfe", "1.52.0--r43hdfd78af_0": "sha256:b8ca0c6a3bdd8074ef1217270959a2d8055344b91b7be656b45461813fdfbc2c"}, "docker": "quay.io/biocontainers/bioconductor-geosubmission"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geosubmission.
shpc-registry automated BioContainers addition for bioconductor-geosubmission
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geosubmission
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geosubmission:1.52.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geosubmission/1.52.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geosubmission/1.52.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geosubmission-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geosubmission-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geosubmission-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geosubmission-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geosubmission-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geosubmission-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geosubmission

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