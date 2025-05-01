---
layout: container
name:  "quay.io/biocontainers/bioconductor-adme16cod.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-adme16cod.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-adme16cod.db/container.yaml"
updated_at: "2025-05-01 03:29:01.191945"
latest: "3.4.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-adme16cod.db"

versions:
 - "3.4.0--r41hdfd78af_9"
 - "3.4.0--r42hdfd78af_10"
 - "3.4.0--r43hdfd78af_11"
 - "3.4.0--r43hdfd78af_12"
 - "3.4.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-adme16cod.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-adme16cod.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-adme16cod.db", "latest": {"3.4.0--r44hdfd78af_13": "sha256:b25e4d2dc11b7a441d77988d5d860038098abe6037bf1d0ad73f5485a3d017a2"}, "tags": {"3.4.0--r41hdfd78af_9": "sha256:1b904438d6fcc54cdd1a90415a7ef38caf0971d4d48f9c8287874f700d944d45", "3.4.0--r42hdfd78af_10": "sha256:3053c7d666c48e337218f8fd458d2f72c5b2f25103131ba04ac526b6e88adea9", "3.4.0--r43hdfd78af_11": "sha256:0443a19a3871311391f1cd6f443a9d6bd23c9c3dc41c5f0da46d878055260fea", "3.4.0--r43hdfd78af_12": "sha256:c65d04049d62b35c4fe83620dd4c53e24511ef2ebcbd71573b32b48345a5c943", "3.4.0--r44hdfd78af_13": "sha256:b25e4d2dc11b7a441d77988d5d860038098abe6037bf1d0ad73f5485a3d017a2"}, "docker": "quay.io/biocontainers/bioconductor-adme16cod.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-adme16cod.db.
shpc-registry automated BioContainers addition for bioconductor-adme16cod.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-adme16cod.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-adme16cod.db:3.4.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-adme16cod.db/3.4.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-adme16cod.db/3.4.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-adme16cod.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adme16cod.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-adme16cod.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-adme16cod.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-adme16cod.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-adme16cod.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-adme16cod.db

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