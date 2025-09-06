---
layout: container
name:  "quay.io/biocontainers/bioconductor-receptloss"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-receptloss/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-receptloss/container.yaml"
updated_at: "2025-09-06 03:01:48.015605"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-receptloss"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-receptloss"
config: {"url": "https://biocontainers.pro/tools/bioconductor-receptloss", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-receptloss", "latest": {"1.18.0--r44hdfd78af_0": "sha256:34d09906796b209a017beb36857d034a3b72c7ba1deffb89459b3cdebcf2672d"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:c77e7ebfc1556f498f39528bf9adc1d349b5df4fffe6d7e4d37a86579abe539a", "1.10.0--r42hdfd78af_0": "sha256:6f3b4bc0b2c428b7a44cc02e2e4e2e1067eeb898e7032681bb943a82bee38d0c", "1.12.0--r43hdfd78af_0": "sha256:35c5a55fb59b3cf84620f66094cf6d978f2fe72d31fc20dbc21fb76faec374b2", "1.14.0--r43hdfd78af_0": "sha256:95b67300a5a1c5f61cfedb6481380fb6313b15cecc730ea45ff1e3b098399f1e", "1.18.0--r44hdfd78af_0": "sha256:34d09906796b209a017beb36857d034a3b72c7ba1deffb89459b3cdebcf2672d"}, "docker": "quay.io/biocontainers/bioconductor-receptloss"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-receptloss.
shpc-registry automated BioContainers addition for bioconductor-receptloss
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-receptloss
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-receptloss:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-receptloss/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-receptloss/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-receptloss-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-receptloss-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-receptloss-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-receptloss-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-receptloss-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-receptloss-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-receptloss

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