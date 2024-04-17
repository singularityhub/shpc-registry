---
layout: container
name:  "quay.io/biocontainers/bioconductor-fgga"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-fgga/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-fgga/container.yaml"
updated_at: "2024-04-17 02:39:24.490368"
latest: "1.9.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-fgga"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.9.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-fgga"
config: {"url": "https://biocontainers.pro/tools/bioconductor-fgga", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-fgga", "latest": {"1.9.0--r43hdfd78af_0": "sha256:1a673505b0ca7a6f728f4e0c793d992be8762aa6d2a53c4af7f3882f293d37e3"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:b4ff85fc969f01cee3f1cd94098afbc234798aa9eaea9cfa87371c588ac4bd0d", "1.6.0--r42hdfd78af_0": "sha256:27fb08c0f0924b0cfc9328ce67cda13e426c0c861c5aa709b89efe31df6d5099", "1.8.0--r43hdfd78af_0": "sha256:744be844d341df8a1268ecbebed0baf113c63108a3ea054133d342d532f5a544", "1.9.0--r43hdfd78af_0": "sha256:1a673505b0ca7a6f728f4e0c793d992be8762aa6d2a53c4af7f3882f293d37e3"}, "docker": "quay.io/biocontainers/bioconductor-fgga"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-fgga.
shpc-registry automated BioContainers addition for bioconductor-fgga
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-fgga
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-fgga:1.9.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-fgga/1.9.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-fgga/1.9.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-fgga-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fgga-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-fgga-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-fgga-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-fgga-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-fgga-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-fgga

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