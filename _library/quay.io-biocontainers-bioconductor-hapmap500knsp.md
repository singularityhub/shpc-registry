---
layout: container
name:  "quay.io/biocontainers/bioconductor-hapmap500knsp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hapmap500knsp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hapmap500knsp/container.yaml"
updated_at: "2025-03-06 03:06:47.665720"
latest: "1.48.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-hapmap500knsp"

versions:
 - "1.36.0--r41hdfd78af_1"
 - "1.39.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.48.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-hapmap500knsp"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hapmap500knsp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hapmap500knsp", "latest": {"1.48.0--r44hdfd78af_0": "sha256:86ee1465a7ca3244ddf9510a95ef5e8c397b2996a2108ba7fa71e95667969376"}, "tags": {"1.36.0--r41hdfd78af_1": "sha256:7be9f09ead5401f6623b93305fa2e15cd2650c76588a506a475e3a819f6d1192", "1.39.0--r42hdfd78af_0": "sha256:f8942af63253a1186eba8161607e0dce5d406ac7e10ffb85313d727683035daf", "1.42.0--r43hdfd78af_0": "sha256:8ebd87163f55098e3eada02a42a253474be19056ea9b646eed18f3d82b20156d", "1.44.0--r43hdfd78af_0": "sha256:0bcdcb7da1e397ad3fececb7e66852791f18e2615a7d0c3350fbf44eb7fbe761", "1.48.0--r44hdfd78af_0": "sha256:86ee1465a7ca3244ddf9510a95ef5e8c397b2996a2108ba7fa71e95667969376"}, "docker": "quay.io/biocontainers/bioconductor-hapmap500knsp"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hapmap500knsp.
shpc-registry automated BioContainers addition for bioconductor-hapmap500knsp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap500knsp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hapmap500knsp:1.48.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hapmap500knsp/1.48.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-hapmap500knsp/1.48.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hapmap500knsp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap500knsp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hapmap500knsp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hapmap500knsp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hapmap500knsp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hapmap500knsp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hapmap500knsp

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