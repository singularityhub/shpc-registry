---
layout: container
name:  "quay.io/biocontainers/bioconductor-phenotest"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-phenotest/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-phenotest/container.yaml"
updated_at: "2025-02-20 03:17:38.386534"
latest: "1.54.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-phenotest"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.54.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-phenotest"
config: {"url": "https://biocontainers.pro/tools/bioconductor-phenotest", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-phenotest", "latest": {"1.54.0--r44hdfd78af_0": "sha256:73128127e86e807a9811d1b9c8aadcf6a3f27b5c70e5e69d1db2becd095c1343"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:7292e4a4c9f8f0ef3709b2520c6093888fb1b978dfeba1c17721ba1644a7858a", "1.46.0--r42hdfd78af_0": "sha256:a1ffdbce67e384d75311b66d0a85ba3806989b4d2d22652025e860ab964833de", "1.48.0--r43hdfd78af_0": "sha256:cc133427cb750f5fce4c8c9ccbb4c09f4e4927d0d1deb6c36b5deb331af0323c", "1.50.0--r43hdfd78af_0": "sha256:43ef70ea42643c4a48f482ab68965f014ea2d8b04695c59c6a1ac2a017e883ef", "1.54.0--r44hdfd78af_0": "sha256:73128127e86e807a9811d1b9c8aadcf6a3f27b5c70e5e69d1db2becd095c1343"}, "docker": "quay.io/biocontainers/bioconductor-phenotest"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-phenotest.
shpc-registry automated BioContainers addition for bioconductor-phenotest
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-phenotest
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-phenotest:1.54.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-phenotest/1.54.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-phenotest/1.54.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-phenotest-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phenotest-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-phenotest-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-phenotest-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-phenotest-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-phenotest-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-phenotest

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