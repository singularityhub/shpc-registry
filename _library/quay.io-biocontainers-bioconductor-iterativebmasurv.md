---
layout: container
name:  "quay.io/biocontainers/bioconductor-iterativebmasurv"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-iterativebmasurv/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-iterativebmasurv/container.yaml"
updated_at: "2024-12-01 04:04:08.585583"
latest: "1.60.0--r43hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-iterativebmasurv"

versions:
 - "1.52.0--r41hdfd78af_0"
 - "1.56.0--r42hdfd78af_0"
 - "1.58.0--r43hdfd78af_0"
 - "1.60.0--r43hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-iterativebmasurv"
config: {"url": "https://biocontainers.pro/tools/bioconductor-iterativebmasurv", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-iterativebmasurv", "latest": {"1.60.0--r43hdfd78af_1": "sha256:a72e315806840eb7b6f27d0efa45c980e64a2bdc07d606cee4bdb99d80258db3"}, "tags": {"1.52.0--r41hdfd78af_0": "sha256:581d3b06b722f2c7f2d2e626d056cce3b675ac6dbda3e7390ce7a1104f7e4138", "1.56.0--r42hdfd78af_0": "sha256:d48284301cc9ecbbc32e8a248f027ba486cad4b1e8ca9ffb4630fba0c558f6e8", "1.58.0--r43hdfd78af_0": "sha256:cef0425b508d9b6631a445ccf3f2441ef9fae91a5e84c25e5dff42ea030e7131", "1.60.0--r43hdfd78af_1": "sha256:a72e315806840eb7b6f27d0efa45c980e64a2bdc07d606cee4bdb99d80258db3"}, "docker": "quay.io/biocontainers/bioconductor-iterativebmasurv"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-iterativebmasurv.
shpc-registry automated BioContainers addition for bioconductor-iterativebmasurv
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-iterativebmasurv
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-iterativebmasurv:1.60.0--r43hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-iterativebmasurv/1.60.0--r43hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-iterativebmasurv/1.60.0--r43hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-iterativebmasurv-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iterativebmasurv-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-iterativebmasurv-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-iterativebmasurv-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-iterativebmasurv-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-iterativebmasurv-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-iterativebmasurv

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