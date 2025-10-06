---
layout: container
name:  "quay.io/biocontainers/bioconductor-netomics"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-netomics/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-netomics/container.yaml"
updated_at: "2025-10-06 06:48:13.425689"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-netomics"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-netomics"
config: {"url": "https://biocontainers.pro/tools/bioconductor-netomics", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-netomics", "latest": {"1.8.0--r43hdfd78af_0": "sha256:675f573ca653b0cbf6006d05d7cab22ce2098f2fca2b6adb8319ee19318e55cf"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:b42134db517f9d5b5c1231c0a3ed79168ef6f966201da1cbedab2cd5fa5f550a", "1.4.0--r42hdfd78af_0": "sha256:53680ac1bfa8139b8c1bf533f4934dabc37ddf829943c13aece0a5fd549e172f", "1.6.0--r43hdfd78af_0": "sha256:6a2a3bdf1723dcc9c76219737a10aa9954363c84031ca9f7a65a70a203178442", "1.8.0--r43hdfd78af_0": "sha256:675f573ca653b0cbf6006d05d7cab22ce2098f2fca2b6adb8319ee19318e55cf"}, "docker": "quay.io/biocontainers/bioconductor-netomics"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-netomics.
shpc-registry automated BioContainers addition for bioconductor-netomics
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-netomics
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-netomics:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-netomics/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-netomics/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-netomics-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netomics-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-netomics-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-netomics-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-netomics-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-netomics-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-netomics

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