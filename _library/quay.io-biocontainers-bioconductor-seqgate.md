---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqgate"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqgate/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqgate/container.yaml"
updated_at: "2025-08-21 03:48:59.204224"
latest: "1.16.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-seqgate"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.16.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-seqgate"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqgate", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqgate", "latest": {"1.16.0--r44hdfd78af_0": "sha256:ad86fef0ad203a5e417f8ac3e9f294531560f0875da2f9ac16fbe0032cd4e894"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:6412bafa8c4fe69362170abf69c35ed305b26aeca2e12dafcf15f81e46e4fa58", "1.8.0--r42hdfd78af_0": "sha256:c0974771f9aafc75ea61b794cb55d388a5ec4d78481576bccff99d8e4f3fe37a", "1.10.0--r43hdfd78af_0": "sha256:c06c98ce2024e8707f163ac8fd624dff524745d722f3367ec41327051307d9bc", "1.12.0--r43hdfd78af_0": "sha256:380b9d96325aca7a96a2086d5efa2749476d9de77e763af9faf50ab249b21f7c", "1.16.0--r44hdfd78af_0": "sha256:ad86fef0ad203a5e417f8ac3e9f294531560f0875da2f9ac16fbe0032cd4e894"}, "docker": "quay.io/biocontainers/bioconductor-seqgate"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqgate.
shpc-registry automated BioContainers addition for bioconductor-seqgate
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqgate
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqgate:1.16.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqgate/1.16.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-seqgate/1.16.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqgate-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqgate-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqgate-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqgate-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqgate-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqgate-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seqgate

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