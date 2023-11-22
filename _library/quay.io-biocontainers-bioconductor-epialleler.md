---
layout: container
name:  "quay.io/biocontainers/bioconductor-epialleler"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epialleler/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epialleler/container.yaml"
updated_at: "2023-11-22 02:46:51.702492"
latest: "1.8.1--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epialleler"

versions:
 - "1.2.0--r41hc247a5b_2"
 - "1.8.1--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epialleler"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epialleler", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epialleler", "latest": {"1.8.1--r43hf17093f_0": "sha256:d05c7445787cc530f4c06e7d0c482c569391dc48ed335e44a264643190feddfd"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:18a1c72ef0446570273f5b9576452db84e883545cc6cee01a054576552823502", "1.8.1--r43hf17093f_0": "sha256:d05c7445787cc530f4c06e7d0c482c569391dc48ed335e44a264643190feddfd"}, "docker": "quay.io/biocontainers/bioconductor-epialleler"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epialleler.
shpc-registry automated BioContainers addition for bioconductor-epialleler
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epialleler
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epialleler:1.8.1--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epialleler/1.8.1--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-epialleler/1.8.1--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epialleler-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epialleler-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epialleler-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epialleler-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epialleler-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epialleler-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-epialleler

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