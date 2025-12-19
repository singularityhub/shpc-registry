---
layout: container
name:  "quay.io/biocontainers/bioconductor-mogene10stv1cdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mogene10stv1cdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mogene10stv1cdf/container.yaml"
updated_at: "2025-12-19 05:08:38.949558"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mogene10stv1cdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mogene10stv1cdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mogene10stv1cdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mogene10stv1cdf", "latest": {"2.18.0--r44hdfd78af_13": "sha256:6ca1e1991a3640ca8fcb415ef0d48d7a6a293ed36d65079732e655178141187a"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:d9dcb5d1959b12c66ffbb6379be9d5ff07f2534a3171b9b988b2a8443ac76e84", "2.18.0--r42hdfd78af_10": "sha256:2e4145b303e483cd5f20a77a71ec70c85a32f0afeb9e6175d86b883e0682bb6a", "2.18.0--r43hdfd78af_11": "sha256:72930f4f2d20a95019006cebdfa38f912e5922c54c2ddcf235817947ad37f835", "2.18.0--r43hdfd78af_12": "sha256:9c7e8e7bdc4aaf38aff0383400afbeaca3a3daeb7ab253c084ac68849f4ae43b", "2.18.0--r44hdfd78af_13": "sha256:6ca1e1991a3640ca8fcb415ef0d48d7a6a293ed36d65079732e655178141187a"}, "docker": "quay.io/biocontainers/bioconductor-mogene10stv1cdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mogene10stv1cdf.
shpc-registry automated BioContainers addition for bioconductor-mogene10stv1cdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene10stv1cdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mogene10stv1cdf:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mogene10stv1cdf/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mogene10stv1cdf/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mogene10stv1cdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene10stv1cdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mogene10stv1cdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mogene10stv1cdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mogene10stv1cdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mogene10stv1cdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mogene10stv1cdf

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