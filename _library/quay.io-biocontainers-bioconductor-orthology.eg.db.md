---
layout: container
name:  "quay.io/biocontainers/bioconductor-orthology.eg.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-orthology.eg.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-orthology.eg.db/container.yaml"
updated_at: "2024-08-26 03:25:28.875634"
latest: "3.18.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-orthology.eg.db"

versions:
 - "3.14.0--r41hdfd78af_1"
 - "3.16.0--r42hdfd78af_0"
 - "3.17.0--r43hdfd78af_0"
 - "3.18.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-orthology.eg.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-orthology.eg.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-orthology.eg.db", "latest": {"3.18.0--r43hdfd78af_0": "sha256:93de763ce697c838f6178b8ace80ce2a7a93eb4ff2693861ed152eac8985f0c2"}, "tags": {"3.14.0--r41hdfd78af_1": "sha256:048028a17bb8811ffecd28f4837ee634524d9c0cfcc2a02fedd043146176e8ed", "3.16.0--r42hdfd78af_0": "sha256:b339c9b12f932e0e1223f1cee6f852cc66e43e241dc3fa28a87120bc584724b6", "3.17.0--r43hdfd78af_0": "sha256:50de88b727cfd17603d50a450aeab0ca583e30bc0a70298212ff7570b0fd05f9", "3.18.0--r43hdfd78af_0": "sha256:93de763ce697c838f6178b8ace80ce2a7a93eb4ff2693861ed152eac8985f0c2"}, "docker": "quay.io/biocontainers/bioconductor-orthology.eg.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-orthology.eg.db.
shpc-registry automated BioContainers addition for bioconductor-orthology.eg.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-orthology.eg.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-orthology.eg.db:3.18.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-orthology.eg.db/3.18.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-orthology.eg.db/3.18.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-orthology.eg.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orthology.eg.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-orthology.eg.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-orthology.eg.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-orthology.eg.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-orthology.eg.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-orthology.eg.db

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