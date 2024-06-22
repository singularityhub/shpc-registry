---
layout: container
name:  "quay.io/biocontainers/bioconductor-aspli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-aspli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-aspli/container.yaml"
updated_at: "2024-06-22 02:47:37.495076"
latest: "2.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-aspli"
aliases:
 - "pandoc"
versions:
 - "2.4.0--r41hdfd78af_0"
 - "2.8.0--r42hdfd78af_0"
 - "2.10.0--r43hdfd78af_0"
 - "2.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-aspli"
config: {"url": "https://biocontainers.pro/tools/bioconductor-aspli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-aspli", "latest": {"2.12.0--r43hdfd78af_0": "sha256:21328890b331983695a9dd8c742fe915748668f595ff81ad776b28cc3594d829"}, "tags": {"2.4.0--r41hdfd78af_0": "sha256:8e4da938a3bb5be5365fdacbcc1ca101c30d45ec0d81992e3ac0de1097f76f08", "2.8.0--r42hdfd78af_0": "sha256:04a10e2b2fcb1fe4b0620a339554da31806dea6881dbba8aeab6ba6de00d4f46", "2.10.0--r43hdfd78af_0": "sha256:754f15f53a26d8987a02837793bdc9b9ecce3f3278b51ddb91b046a1f27a8b3f", "2.12.0--r43hdfd78af_0": "sha256:21328890b331983695a9dd8c742fe915748668f595ff81ad776b28cc3594d829"}, "docker": "quay.io/biocontainers/bioconductor-aspli", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-aspli.
shpc-registry automated BioContainers addition for bioconductor-aspli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-aspli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-aspli:2.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-aspli/2.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-aspli/2.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-aspli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aspli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-aspli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-aspli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-aspli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-aspli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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