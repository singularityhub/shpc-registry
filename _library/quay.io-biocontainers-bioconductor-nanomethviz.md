---
layout: container
name:  "quay.io/biocontainers/bioconductor-nanomethviz"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nanomethviz/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nanomethviz/container.yaml"
updated_at: "2025-09-18 03:25:01.677960"
latest: "2.8.1--r43hf17093f_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nanomethviz"

versions:
 - "2.0.0--r41hc247a5b_2"
 - "2.4.0--r42hc247a5b_0"
 - "2.4.0--r42hf17093f_1"
 - "2.6.0--r43hf17093f_0"
 - "2.8.1--r43hf17093f_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nanomethviz"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nanomethviz", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nanomethviz", "latest": {"2.8.1--r43hf17093f_0": "sha256:2851195457e79b47d1297b2232f96daeb9be9a1499c5cef2beb987b4bb31927e"}, "tags": {"2.0.0--r41hc247a5b_2": "sha256:dfa3d49acde10f541a873508f14d3549f2bd01df87b9d7f6e48e205b02afa038", "2.4.0--r42hc247a5b_0": "sha256:6b291e0e453e49a043e5f43861860d76fb722f37bbb30d63c908909f08a52eb7", "2.4.0--r42hf17093f_1": "sha256:7ca56ab94af104b07a542e281cf79b07a32264fc5ca36439cf09b82320997ef8", "2.6.0--r43hf17093f_0": "sha256:39d305606c6b7d2880897dd1f45d56a246297886bc2042ca25fb53017dafbaf2", "2.8.1--r43hf17093f_0": "sha256:2851195457e79b47d1297b2232f96daeb9be9a1499c5cef2beb987b4bb31927e"}, "docker": "quay.io/biocontainers/bioconductor-nanomethviz"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nanomethviz.
shpc-registry automated BioContainers addition for bioconductor-nanomethviz
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nanomethviz
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nanomethviz:2.8.1--r43hf17093f_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nanomethviz/2.8.1--r43hf17093f_0
$ module help quay.io/biocontainers/bioconductor-nanomethviz/2.8.1--r43hf17093f_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nanomethviz-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanomethviz-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanomethviz-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nanomethviz-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nanomethviz-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nanomethviz-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nanomethviz

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