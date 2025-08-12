---
layout: container
name:  "quay.io/biocontainers/bioconductor-aneufinder"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-aneufinder/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-aneufinder/container.yaml"
updated_at: "2025-08-12 03:38:10.840130"
latest: "1.34.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-aneufinder"

versions:
 - "1.22.0--r41hc247a5b_2"
 - "1.26.0--r42hc247a5b_0"
 - "1.26.0--r42hf17093f_1"
 - "1.28.0--r43hf17093f_0"
 - "1.30.0--r43hf17093f_0"
 - "1.34.0--r44he5774e6_0"
description: "shpc-registry automated BioContainers addition for bioconductor-aneufinder"
config: {"url": "https://biocontainers.pro/tools/bioconductor-aneufinder", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-aneufinder", "latest": {"1.34.0--r44he5774e6_0": "sha256:af7a238e5d6a144e4383c68d4387f49514302b3abbcab95f4f2153363fe0c001"}, "tags": {"1.22.0--r41hc247a5b_2": "sha256:445691d858fc40e5acb07da40172cb4d8c3f0e3da1951d57a9e6654bff659df8", "1.26.0--r42hc247a5b_0": "sha256:0c0f5e811558f33dbbb3877a44835ba7949894d31fd81b859e687569385d1d9f", "1.26.0--r42hf17093f_1": "sha256:d3707d7652b87e64a743bfe515415db9e48909e744254fc6c429429d13d84b77", "1.28.0--r43hf17093f_0": "sha256:052432b9f419e53d527d73b3168b96774567b84a4a0eba69743bf7b848b028e8", "1.30.0--r43hf17093f_0": "sha256:1097cd1843f7c1831cb58206221988b966c32916f119f36b8f5a4819b9e59932", "1.34.0--r44he5774e6_0": "sha256:af7a238e5d6a144e4383c68d4387f49514302b3abbcab95f4f2153363fe0c001"}, "docker": "quay.io/biocontainers/bioconductor-aneufinder"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-aneufinder.
shpc-registry automated BioContainers addition for bioconductor-aneufinder
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-aneufinder
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-aneufinder:1.34.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-aneufinder/1.34.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-aneufinder/1.34.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-aneufinder-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aneufinder-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aneufinder-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-aneufinder-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-aneufinder-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-aneufinder-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-aneufinder

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