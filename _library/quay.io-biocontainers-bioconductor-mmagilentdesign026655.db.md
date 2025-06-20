---
layout: container
name:  "quay.io/biocontainers/bioconductor-mmagilentdesign026655.db"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mmagilentdesign026655.db/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mmagilentdesign026655.db/container.yaml"
updated_at: "2025-06-20 03:26:34.822110"
latest: "3.2.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-mmagilentdesign026655.db"

versions:
 - "3.2.3--r41hdfd78af_9"
 - "3.2.3--r42hdfd78af_10"
 - "3.2.3--r43hdfd78af_11"
 - "3.2.3--r43hdfd78af_12"
 - "3.2.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-mmagilentdesign026655.db"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mmagilentdesign026655.db", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mmagilentdesign026655.db", "latest": {"3.2.3--r44hdfd78af_13": "sha256:ade14d90e9eb1dc26e0ab8cbf3a1848c857029d8dd947276f01879eb5c272316"}, "tags": {"3.2.3--r41hdfd78af_9": "sha256:0fb8fcca754866dd13b12867589a0ef5c1a915083d97e9480e43b83d302cee25", "3.2.3--r42hdfd78af_10": "sha256:b15bde943cec7f9907b40ee5746efa522551fa6c5c073c1b63aedefb0b8104e3", "3.2.3--r43hdfd78af_11": "sha256:dd3a959aa92b63f20b052f3afa2c12a1b22c7b297f89eb2c84714ac0aaea4fc2", "3.2.3--r43hdfd78af_12": "sha256:fd6eefebe61540d796bbb25a7b2cbaf06d021f981a8d1e61c7ba96221eeb0a11", "3.2.3--r44hdfd78af_13": "sha256:ade14d90e9eb1dc26e0ab8cbf3a1848c857029d8dd947276f01879eb5c272316"}, "docker": "quay.io/biocontainers/bioconductor-mmagilentdesign026655.db"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mmagilentdesign026655.db.
shpc-registry automated BioContainers addition for bioconductor-mmagilentdesign026655.db
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mmagilentdesign026655.db
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mmagilentdesign026655.db:3.2.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mmagilentdesign026655.db/3.2.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-mmagilentdesign026655.db/3.2.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mmagilentdesign026655.db-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmagilentdesign026655.db-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mmagilentdesign026655.db-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mmagilentdesign026655.db-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mmagilentdesign026655.db-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mmagilentdesign026655.db-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mmagilentdesign026655.db

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