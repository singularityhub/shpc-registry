---
layout: container
name:  "quay.io/biocontainers/bioconductor-flowgraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-flowgraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-flowgraph/container.yaml"
updated_at: "2024-01-18 03:04:26.885859"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-flowgraph"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-flowgraph"
config: {"url": "https://biocontainers.pro/tools/bioconductor-flowgraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-flowgraph", "latest": {"1.10.0--r43hdfd78af_0": "sha256:80c1508949a55ff9e59f6efdfea2546c16809c61b82158d5026be516f0a3b1ce"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:492abc66446f7e875174bb84a98685c31d965320ec182504ca929c243efa2444", "1.6.0--r42hdfd78af_0": "sha256:bb5bdb5e11b4349f75ab8a20697f6c97ab0ef52a4d89b7034fcddc570e9e397b", "1.8.0--r43hdfd78af_0": "sha256:b001625b77d1094fa588af4b5ba4f6b86d451920ee2eb7a170da97c83a6b64fe", "1.10.0--r43hdfd78af_0": "sha256:80c1508949a55ff9e59f6efdfea2546c16809c61b82158d5026be516f0a3b1ce"}, "docker": "quay.io/biocontainers/bioconductor-flowgraph"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-flowgraph.
shpc-registry automated BioContainers addition for bioconductor-flowgraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-flowgraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-flowgraph:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-flowgraph/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-flowgraph/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-flowgraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowgraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-flowgraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-flowgraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-flowgraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-flowgraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-flowgraph

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