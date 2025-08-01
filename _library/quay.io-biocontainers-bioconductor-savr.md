---
layout: container
name:  "quay.io/biocontainers/bioconductor-savr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-savr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-savr/container.yaml"
updated_at: "2025-08-01 04:15:41.368295"
latest: "1.37.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-savr"

versions:
 - "1.32.0--r41hdfd78af_0"
 - "1.36.0--r42hdfd78af_0"
 - "1.37.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-savr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-savr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-savr", "latest": {"1.37.0--r43hdfd78af_0": "sha256:6da7eac592e1c6a3b49e64364bd17c9f633b83bf8ffe16d49705467f6005d4df"}, "tags": {"1.32.0--r41hdfd78af_0": "sha256:029d83b6c85a499b28eaff0cfa4e998592f1c20913ee8f13ccda8215b76108aa", "1.36.0--r42hdfd78af_0": "sha256:2238287667ef8127c8091a0a097b302fca18ff4436cf426a5083f8f72d0c3bb2", "1.37.0--r43hdfd78af_0": "sha256:6da7eac592e1c6a3b49e64364bd17c9f633b83bf8ffe16d49705467f6005d4df"}, "docker": "quay.io/biocontainers/bioconductor-savr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-savr.
shpc-registry automated BioContainers addition for bioconductor-savr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-savr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-savr:1.37.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-savr/1.37.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-savr/1.37.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-savr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-savr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-savr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-savr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-savr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-savr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-savr

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