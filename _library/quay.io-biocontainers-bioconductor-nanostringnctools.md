---
layout: container
name:  "quay.io/biocontainers/bioconductor-nanostringnctools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-nanostringnctools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-nanostringnctools/container.yaml"
updated_at: "2025-08-01 11:03:09.941849"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-nanostringnctools"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-nanostringnctools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-nanostringnctools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-nanostringnctools", "latest": {"1.14.0--r44hdfd78af_0": "sha256:ed4a93437e8d7e4daf97e5bfeada7c94b300657372bedcdeca859283047c572f"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:ac157040fe65aa6189bd4abed0e36cd8c612bd709ea1f22b83daf315323fac16", "1.6.0--r42hdfd78af_0": "sha256:9bc96c8d5b4c81a7d4968c6cdf77a32fbcd72d17900b8173e70b1b06ef690e21", "1.8.0--r43hdfd78af_0": "sha256:7125809867197418688e81ee22e4c141a1ca54399fda12d21a75f407fa23b982", "1.10.0--r43hdfd78af_0": "sha256:190f7085e5466782f24835fd0acce085ef937ae70f0054994afebd15645b7247", "1.14.0--r44hdfd78af_0": "sha256:ed4a93437e8d7e4daf97e5bfeada7c94b300657372bedcdeca859283047c572f"}, "docker": "quay.io/biocontainers/bioconductor-nanostringnctools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-nanostringnctools.
shpc-registry automated BioContainers addition for bioconductor-nanostringnctools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-nanostringnctools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-nanostringnctools:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-nanostringnctools/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-nanostringnctools/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-nanostringnctools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanostringnctools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-nanostringnctools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-nanostringnctools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-nanostringnctools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-nanostringnctools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-nanostringnctools

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