---
layout: container
name:  "quay.io/biocontainers/bioconductor-curatedadipoarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-curatedadipoarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-curatedadipoarray/container.yaml"
updated_at: "2025-11-05 03:24:09.968676"
latest: "1.18.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-curatedadipoarray"

versions:
 - "1.6.0--r41hdfd78af_1"
 - "1.9.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.18.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-curatedadipoarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-curatedadipoarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-curatedadipoarray", "latest": {"1.18.0--r44hdfd78af_0": "sha256:f038ef4a948448f4d96bbe3833087f3f036041adc704c870b968cb474c97abc2"}, "tags": {"1.6.0--r41hdfd78af_1": "sha256:b7713835449de27a5dee8699ff583723b9bba6ae2c28f756b7477ab794b2b169", "1.9.0--r42hdfd78af_0": "sha256:eb917b94b3562dbc44f8def14895e4c335986eed0f2433f736ac45e5654df15b", "1.12.0--r43hdfd78af_0": "sha256:fa162a767f9efa895ecdd8057d67f9e6dc8aad0c9ff0a1d43f196d36f1793f92", "1.14.0--r43hdfd78af_0": "sha256:323474807ba2401d11426355dbb3331e59b828eadf6ff1f67762286285a55149", "1.18.0--r44hdfd78af_0": "sha256:f038ef4a948448f4d96bbe3833087f3f036041adc704c870b968cb474c97abc2"}, "docker": "quay.io/biocontainers/bioconductor-curatedadipoarray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-curatedadipoarray.
shpc-registry automated BioContainers addition for bioconductor-curatedadipoarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedadipoarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-curatedadipoarray:1.18.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-curatedadipoarray/1.18.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-curatedadipoarray/1.18.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-curatedadipoarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedadipoarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-curatedadipoarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-curatedadipoarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-curatedadipoarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-curatedadipoarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-curatedadipoarray

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