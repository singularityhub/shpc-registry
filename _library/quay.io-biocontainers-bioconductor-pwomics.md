---
layout: container
name:  "quay.io/biocontainers/bioconductor-pwomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pwomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pwomics/container.yaml"
updated_at: "2025-03-17 03:28:19.822544"
latest: "1.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pwomics"

versions:
 - "1.26.0--r41hdfd78af_0"
 - "1.30.0--r42hdfd78af_0"
 - "1.32.0--r43hdfd78af_0"
 - "1.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pwomics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pwomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pwomics", "latest": {"1.34.0--r43hdfd78af_0": "sha256:89d7645f92e1fab03542966f253f608edcf76628cbceb4e5ad9f776478ceb4d3"}, "tags": {"1.26.0--r41hdfd78af_0": "sha256:a80027c51b015de83c15fe392a6a1e11fc0829a1555088106b4149ebff104f34", "1.30.0--r42hdfd78af_0": "sha256:6f4a750788c29b329076c5d2afab73f70389796bcce46464c3015cea85faa883", "1.32.0--r43hdfd78af_0": "sha256:2444c5476ef69eaab567af925dc47d69bc673569796e6861fbd86382cace8dec", "1.34.0--r43hdfd78af_0": "sha256:89d7645f92e1fab03542966f253f608edcf76628cbceb4e5ad9f776478ceb4d3"}, "docker": "quay.io/biocontainers/bioconductor-pwomics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pwomics.
shpc-registry automated BioContainers addition for bioconductor-pwomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pwomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pwomics:1.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pwomics/1.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pwomics/1.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pwomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pwomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pwomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pwomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pwomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pwomics

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