---
layout: container
name:  "quay.io/biocontainers/bioconductor-keggdzpathwaysgeo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-keggdzpathwaysgeo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-keggdzpathwaysgeo/container.yaml"
updated_at: "2024-03-25 02:55:19.560900"
latest: "1.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-keggdzpathwaysgeo"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.36.0--r42hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-keggdzpathwaysgeo"
config: {"url": "https://biocontainers.pro/tools/bioconductor-keggdzpathwaysgeo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-keggdzpathwaysgeo", "latest": {"1.40.0--r43hdfd78af_0": "sha256:d4c8781353372c9d393df4d65f541a11e2029a8147659cdd8573a67957233c69"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:62935199fcab49a780ac514e8d628866104088c31014d64ba6fee66faadf6147", "1.36.0--r42hdfd78af_0": "sha256:3c25968acf1d2b90db39206a8649d9a0354f45d7ca465e5d942dd9800eb6ce09", "1.38.0--r43hdfd78af_0": "sha256:a22846e38c405943a932bdcea0ff81fdaa649266d39d6532e6554bc8accd707f", "1.40.0--r43hdfd78af_0": "sha256:d4c8781353372c9d393df4d65f541a11e2029a8147659cdd8573a67957233c69"}, "docker": "quay.io/biocontainers/bioconductor-keggdzpathwaysgeo"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-keggdzpathwaysgeo.
shpc-registry automated BioContainers addition for bioconductor-keggdzpathwaysgeo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-keggdzpathwaysgeo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-keggdzpathwaysgeo:1.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-keggdzpathwaysgeo/1.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-keggdzpathwaysgeo/1.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-keggdzpathwaysgeo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-keggdzpathwaysgeo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-keggdzpathwaysgeo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-keggdzpathwaysgeo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-keggdzpathwaysgeo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-keggdzpathwaysgeo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-keggdzpathwaysgeo

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