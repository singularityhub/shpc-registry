---
layout: container
name:  "quay.io/biocontainers/bioconductor-mygene"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mygene/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mygene/container.yaml"
updated_at: "2023-10-25 02:43:13.056181"
latest: "1.36.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mygene"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mygene"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mygene", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mygene", "latest": {"1.36.0--r43hdfd78af_0": "sha256:d875ac6501cc1c93fd686738f339bd09f87feb7ee41fa00bad6451d62b835e33"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:efeaf564c12d756f95a4b0e35a7add88b80ed4a3cb56b8130441aebf3d2efe9e", "1.34.0--r42hdfd78af_0": "sha256:4f51231bf450cc493ec75c03c2921552364ac0cfae34a11c93a7802ff61b804d", "1.36.0--r43hdfd78af_0": "sha256:d875ac6501cc1c93fd686738f339bd09f87feb7ee41fa00bad6451d62b835e33"}, "docker": "quay.io/biocontainers/bioconductor-mygene"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mygene.
shpc-registry automated BioContainers addition for bioconductor-mygene
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mygene
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mygene:1.36.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mygene/1.36.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mygene/1.36.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mygene-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mygene-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mygene-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mygene-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mygene-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mygene-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mygene

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