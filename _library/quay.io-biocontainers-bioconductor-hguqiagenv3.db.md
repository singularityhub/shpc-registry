---
layout: container
name:  "quay.io/biocontainers/bioconductor-hguqiagenv3.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hguqiagenv3.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hguqiagenv3.db/container.yaml"
updated_at: "2023-09-25 02:24:54.168082"
latest: "3.2.3--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-hguqiagenv3.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-hguqiagenv3.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hguqiagenv3.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hguqiagenv3.db", "latest": {"3.2.3--r43hdfd78af_11": "sha256:e17417cc7f5f3c9b21c75e9dc251de82de70d2f65144730dc9a966f0cd873a29"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:422c5a35078412598846c1a18fd46394ee2f86bc9b476d4ee9cc6145fb8c3236", "3.2.3--r42hdfd78af_10": "sha256:fb99f6ae7c2b77f8041f8347b2de2866916af0931f6a11186174edee60965575", "3.2.3--r43hdfd78af_11": "sha256:e17417cc7f5f3c9b21c75e9dc251de82de70d2f65144730dc9a966f0cd873a29"}, "docker": "quay.io/biocontainers/bioconductor-hguqiagenv3.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hguqiagenv3.db.
shpc-registry automated BioContainers addition for bioconductor-hguqiagenv3.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hguqiagenv3.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hguqiagenv3.db:3.2.3--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hguqiagenv3.db/3.2.3--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-hguqiagenv3.db/3.2.3--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hguqiagenv3.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hguqiagenv3.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hguqiagenv3.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hguqiagenv3.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hguqiagenv3.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hguqiagenv3.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hguqiagenv3.db

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