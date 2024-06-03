---
layout: container
name:  "quay.io/biocontainers/bioconductor-ygs98probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ygs98probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ygs98probe/container.yaml"
updated_at: "2024-06-03 02:57:16.421516"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-ygs98probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-ygs98probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ygs98probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ygs98probe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:b4500f9f4fc8c12c022d11c6d7ca9eb97bc5ba313d286ad742f8cf5560c429ec"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:5f3ff961c65028132dd68b363488197753e428356127d79ad7cd70a79538e991", "2.18.0--r42hdfd78af_10": "sha256:a14568f91d0ff0cbd3aedcabccc2c89f3efb6830481126d04292a876b7ecc98c", "2.18.0--r43hdfd78af_11": "sha256:119c4cd2c96c42319568131c9b34c039dfb06cbca49861d7961b507a4c95b117", "2.18.0--r43hdfd78af_12": "sha256:b4500f9f4fc8c12c022d11c6d7ca9eb97bc5ba313d286ad742f8cf5560c429ec"}, "docker": "quay.io/biocontainers/bioconductor-ygs98probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ygs98probe.
shpc-registry automated BioContainers addition for bioconductor-ygs98probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ygs98probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ygs98probe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ygs98probe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-ygs98probe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ygs98probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ygs98probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ygs98probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ygs98probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ygs98probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ygs98probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ygs98probe

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