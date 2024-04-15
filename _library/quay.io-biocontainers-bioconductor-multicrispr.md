---
layout: container
name:  "quay.io/biocontainers/bioconductor-multicrispr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-multicrispr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-multicrispr/container.yaml"
updated_at: "2024-04-15 06:11:55.388950"
latest: "1.12.3--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-multicrispr"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.1--r43hdfd78af_0"
 - "1.12.3--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-multicrispr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-multicrispr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-multicrispr", "latest": {"1.12.3--r43hdfd78af_0": "sha256:5b9dd3ed26894c07da5f0018bd5bd8283b1f24951dcb222828aa82f3ea74bedd"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:029a74fd0d08f79d8c989706b8be30a957107938db5b7c3aed298c9a2c41837e", "1.8.0--r42hdfd78af_0": "sha256:0b7a02cb38a045d2588ea397682c1c0e7ec066f1036606cea27686951b9f9523", "1.10.1--r43hdfd78af_0": "sha256:fcd2b8d14bc3e59435f46f678ce508847e1ff5998b889f8e3c13bf18ea9d610b", "1.12.3--r43hdfd78af_0": "sha256:5b9dd3ed26894c07da5f0018bd5bd8283b1f24951dcb222828aa82f3ea74bedd"}, "docker": "quay.io/biocontainers/bioconductor-multicrispr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-multicrispr.
shpc-registry automated BioContainers addition for bioconductor-multicrispr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-multicrispr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-multicrispr:1.12.3--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-multicrispr/1.12.3--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-multicrispr/1.12.3--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-multicrispr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multicrispr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-multicrispr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-multicrispr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-multicrispr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-multicrispr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-multicrispr

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