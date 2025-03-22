---
layout: container
name:  "quay.io/biocontainers/bioconductor-variantannotation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-variantannotation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-variantannotation/container.yaml"
updated_at: "2025-03-22 03:33:31.646059"
latest: "1.52.0--r44h15a9599_0"
container_url: "https://biocontainers.pro/tools/bioconductor-variantannotation"

versions:
 - "1.40.0--r41hc0cfd56_2"
 - "1.44.0--r42hc0cfd56_0"
 - "1.44.0--r42ha9d7317_1"
 - "1.46.0--r43ha9d7317_0"
 - "1.48.1--r43ha9d7317_0"
 - "1.52.0--r44h15a9599_0"
description: "shpc-registry automated BioContainers addition for bioconductor-variantannotation"
config: {"url": "https://biocontainers.pro/tools/bioconductor-variantannotation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-variantannotation", "latest": {"1.52.0--r44h15a9599_0": "sha256:ecca3455dc767b969aa175e467c71caab0b20ae8870da0c91d3091d0b6f906b4"}, "tags": {"1.40.0--r41hc0cfd56_2": "sha256:eeccbb621feb9bcdf9b55a02834d9f62ffd3909f4509e2defb0f8d1f5bb22dad", "1.44.0--r42hc0cfd56_0": "sha256:505b9bc00389502deb5aaac8f57e0a540fde55f03cdf76f03eb8876b4ea44d12", "1.44.0--r42ha9d7317_1": "sha256:3db56442078130a4b204f9a8f3aeff4c58a858ce5461ec656643e6906ffd9931", "1.46.0--r43ha9d7317_0": "sha256:8cddd83e028d0cba5ee6f50ac3948b7b38928eebd06c5b5c764774dd806a061e", "1.48.1--r43ha9d7317_0": "sha256:79e5fe260409f903a07780a148623f1d1273c04849b63317401276869525bbf8", "1.52.0--r44h15a9599_0": "sha256:ecca3455dc767b969aa175e467c71caab0b20ae8870da0c91d3091d0b6f906b4"}, "docker": "quay.io/biocontainers/bioconductor-variantannotation"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-variantannotation.
shpc-registry automated BioContainers addition for bioconductor-variantannotation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-variantannotation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-variantannotation:1.52.0--r44h15a9599_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-variantannotation/1.52.0--r44h15a9599_0
$ module help quay.io/biocontainers/bioconductor-variantannotation/1.52.0--r44h15a9599_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-variantannotation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-variantannotation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-variantannotation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-variantannotation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-variantannotation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-variantannotation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-variantannotation

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