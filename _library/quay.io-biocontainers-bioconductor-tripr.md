---
layout: container
name:  "quay.io/biocontainers/bioconductor-tripr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tripr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tripr/container.yaml"
updated_at: "2025-05-26 04:00:20.428470"
latest: "1.12.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tripr"

versions:
 - "1.0.0--r41hdfd78af_0"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
 - "1.8.0--r43hdfd78af_1"
 - "1.12.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tripr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tripr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tripr", "latest": {"1.12.0--r44hdfd78af_0": "sha256:02dd4e3a9ab3737538d530ca9d25ffe9c92fcd580057e341ef098405035dc2a2"}, "tags": {"1.0.0--r41hdfd78af_0": "sha256:dccbe088e00ac4e0ca4473320f058c48bfed007b7c5938dd28b3f4a3c30a3765", "1.4.0--r42hdfd78af_0": "sha256:3df41ccd69277bd28fcc24abb47cce85e81d1de315db82e85b9e3bddd685185a", "1.6.0--r43hdfd78af_0": "sha256:d512c8580141290123c12e0be164d3dea5504c25ff7fdcf99079ab2f31193ae4", "1.8.0--r43hdfd78af_1": "sha256:36a4900da7ecfad81ad5afccbe77d5ed9724f362fa710ce9c882de493d0fe576", "1.12.0--r44hdfd78af_0": "sha256:02dd4e3a9ab3737538d530ca9d25ffe9c92fcd580057e341ef098405035dc2a2"}, "docker": "quay.io/biocontainers/bioconductor-tripr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tripr.
shpc-registry automated BioContainers addition for bioconductor-tripr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tripr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tripr:1.12.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tripr/1.12.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tripr/1.12.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tripr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tripr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tripr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tripr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tripr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tripr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tripr

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