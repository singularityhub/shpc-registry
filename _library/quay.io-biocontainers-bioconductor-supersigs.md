---
layout: container
name:  "quay.io/biocontainers/bioconductor-supersigs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-supersigs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-supersigs/container.yaml"
updated_at: "2025-05-14 03:54:29.290147"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-supersigs"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-supersigs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-supersigs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-supersigs", "latest": {"1.14.0--r44hdfd78af_0": "sha256:0d132950cf42c0fa840c81d6c7da9add731b86159cf28b8a01a3b550d4a15075"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:3c453a37d59073085c8047a525f327c33aa15c8b62f7af9a7d3d284295846c99", "1.6.0--r42hdfd78af_0": "sha256:d43a455e03ecb1d2c9b98e56e3ea2fed46b2ab6255c52c8d1b505fb46f160159", "1.8.0--r43hdfd78af_0": "sha256:d57dcde83188dd94eb235358470726aa10b7365a038b83ce4e374306488685c4", "1.10.0--r43hdfd78af_0": "sha256:125a99e0762fd6d28baedd01fef751edbdf2ae67475033845a52f516f711343a", "1.14.0--r44hdfd78af_0": "sha256:0d132950cf42c0fa840c81d6c7da9add731b86159cf28b8a01a3b550d4a15075"}, "docker": "quay.io/biocontainers/bioconductor-supersigs"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-supersigs.
shpc-registry automated BioContainers addition for bioconductor-supersigs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-supersigs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-supersigs:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-supersigs/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-supersigs/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-supersigs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-supersigs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-supersigs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-supersigs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-supersigs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-supersigs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-supersigs

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