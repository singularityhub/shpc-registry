---
layout: container
name:  "quay.io/biocontainers/bioconductor-opencyto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-opencyto/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-opencyto/container.yaml"
updated_at: "2024-02-22 04:46:41.001474"
latest: "2.14.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-opencyto"

versions:
 - "2.6.0--r41hc247a5b_2"
 - "2.10.0--r42hc247a5b_0"
 - "2.10.0--r42hf17093f_1"
 - "2.12.0--r43hf17093f_0"
 - "2.14.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-opencyto"
config: {"url": "https://biocontainers.pro/tools/bioconductor-opencyto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-opencyto", "latest": {"2.14.0--r43hf17093f_0": "sha256:534bbb7843a744fd0706258f2fd5b6973973aa877f2342a8792a70249a885478"}, "tags": {"2.6.0--r41hc247a5b_2": "sha256:6c7d537b410551a19de9ba08df57662701ea75c6af6a07f68503bcaa8e34d292", "2.10.0--r42hc247a5b_0": "sha256:372a11aa99315b16e878c5ff3d5ed7c71adf243eae01a9f556d9c906bfb0fbb9", "2.10.0--r42hf17093f_1": "sha256:db289347b6b0ec5c773b6fe870538d0115b14c529bb7f75b671bdc927e86b9c4", "2.12.0--r43hf17093f_0": "sha256:b294bb41bf527907eeb382a8f4758e3b0645df5d55a5317da036c3dd7421dfc8", "2.14.0--r43hf17093f_0": "sha256:534bbb7843a744fd0706258f2fd5b6973973aa877f2342a8792a70249a885478"}, "docker": "quay.io/biocontainers/bioconductor-opencyto"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-opencyto.
shpc-registry automated BioContainers addition for bioconductor-opencyto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-opencyto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-opencyto:2.14.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-opencyto/2.14.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-opencyto/2.14.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-opencyto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-opencyto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-opencyto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-opencyto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-opencyto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-opencyto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-opencyto

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