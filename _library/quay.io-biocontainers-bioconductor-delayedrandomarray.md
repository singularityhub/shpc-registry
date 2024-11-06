---
layout: container
name:  "quay.io/biocontainers/bioconductor-delayedrandomarray"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-delayedrandomarray/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-delayedrandomarray/container.yaml"
updated_at: "2024-11-06 03:15:32.077587"
latest: "1.10.0--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-delayedrandomarray"

versions:
 - "1.2.0--r41hc247a5b_2"
 - "1.6.0--r42hc247a5b_0"
 - "1.6.0--r42hf17093f_1"
 - "1.8.0--r43hf17093f_0"
 - "1.10.0--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-delayedrandomarray"
config: {"url": "https://biocontainers.pro/tools/bioconductor-delayedrandomarray", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-delayedrandomarray", "latest": {"1.10.0--r43hf17093f_0": "sha256:b2627540b8a13f6eb4b97ed41f8dccb97a30a393a83a930737751b8e8ddd940c"}, "tags": {"1.2.0--r41hc247a5b_2": "sha256:d49b6b6f37e09769d6c7a4e6dd59b7879a18f89e89867c6de0c92707a439bb42", "1.6.0--r42hc247a5b_0": "sha256:fe5f0da16b0844a94edf0e0045cdf17fcf3ee209b10ad4a12c1a690921bb5d1b", "1.6.0--r42hf17093f_1": "sha256:140f6c623c569ed8da69abe0d071a5b9c5cfbcf8173b4b2f2fa59eecc1828a87", "1.8.0--r43hf17093f_0": "sha256:9f22064b21eb1c14d1fc16e95a26507737e4aaf20f68cf31022cb604d9b074e9", "1.10.0--r43hf17093f_0": "sha256:b2627540b8a13f6eb4b97ed41f8dccb97a30a393a83a930737751b8e8ddd940c"}, "docker": "quay.io/biocontainers/bioconductor-delayedrandomarray"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-delayedrandomarray.
shpc-registry automated BioContainers addition for bioconductor-delayedrandomarray
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-delayedrandomarray
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-delayedrandomarray:1.10.0--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-delayedrandomarray/1.10.0--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-delayedrandomarray/1.10.0--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-delayedrandomarray-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayedrandomarray-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-delayedrandomarray-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-delayedrandomarray-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-delayedrandomarray-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-delayedrandomarray-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-delayedrandomarray

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