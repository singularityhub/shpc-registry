---
layout: container
name:  "quay.io/biocontainers/bioconductor-systempipetools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-systempipetools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-systempipetools/container.yaml"
updated_at: "2024-10-16 03:38:39.391446"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-systempipetools"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-systempipetools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-systempipetools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-systempipetools", "latest": {"1.10.0--r43hdfd78af_0": "sha256:78f9035bba7ebf2c731839f98e04289e9b70d3355f7ed151bfe42c9dbc86ef8a"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:4686cd35f8d2e1febf2467a2abebbe3def4705c3e3f2171649e0fc62f32f0aea", "1.6.0--r42hdfd78af_0": "sha256:342c491bee1c44bfa4fa85fcf9a11b95e27ac9bb7279df51b0f699fe223a5850", "1.8.0--r43hdfd78af_0": "sha256:73d21565702da8a90186e793beed9f50543a066cc857abf30900f5dc1f78e1e7", "1.10.0--r43hdfd78af_0": "sha256:78f9035bba7ebf2c731839f98e04289e9b70d3355f7ed151bfe42c9dbc86ef8a"}, "docker": "quay.io/biocontainers/bioconductor-systempipetools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-systempipetools.
shpc-registry automated BioContainers addition for bioconductor-systempipetools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-systempipetools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-systempipetools:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-systempipetools/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-systempipetools/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-systempipetools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-systempipetools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-systempipetools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-systempipetools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-systempipetools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-systempipetools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-systempipetools

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