---
layout: container
name:  "quay.io/biocontainers/bioconductor-customprodb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-customprodb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-customprodb/container.yaml"
updated_at: "2025-05-13 04:01:10.657105"
latest: "1.46.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-customprodb"

versions:
 - "1.34.0--r41hdfd78af_0"
 - "1.38.0--r42hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
 - "1.41.0--r43hdfd78af_0"
 - "1.46.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-customprodb"
config: {"url": "https://biocontainers.pro/tools/bioconductor-customprodb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-customprodb", "latest": {"1.46.0--r44hdfd78af_0": "sha256:a06cd9e97e99128fc64f266a0b5f508556a9b9f2469603fd080343ca7e362bd5"}, "tags": {"1.34.0--r41hdfd78af_0": "sha256:22ade8f9d023ca31d86189182a9f5de0c94711f0de26c02bc8498d292b748cf2", "1.38.0--r42hdfd78af_0": "sha256:8141d1a0120f1dc73b42512d3c4aa6729e17794ebecd5c07e5a8e00238a83109", "1.40.0--r43hdfd78af_0": "sha256:fe776adb4e4d163cd75bed2c7d52cb65e2d36881311e169310ac7c4d924687af", "1.41.0--r43hdfd78af_0": "sha256:22ab8815097a2bdc52d5cb376498fc32cf11cc7cf9cbdd4529a74eabd999f140", "1.46.0--r44hdfd78af_0": "sha256:a06cd9e97e99128fc64f266a0b5f508556a9b9f2469603fd080343ca7e362bd5"}, "docker": "quay.io/biocontainers/bioconductor-customprodb"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-customprodb.
shpc-registry automated BioContainers addition for bioconductor-customprodb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-customprodb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-customprodb:1.46.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-customprodb/1.46.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-customprodb/1.46.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-customprodb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-customprodb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-customprodb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-customprodb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-customprodb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-customprodb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-customprodb

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