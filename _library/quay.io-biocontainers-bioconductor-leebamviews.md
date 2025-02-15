---
layout: container
name:  "quay.io/biocontainers/bioconductor-leebamviews"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-leebamviews/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-leebamviews/container.yaml"
updated_at: "2025-02-15 02:52:53.272700"
latest: "1.42.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-leebamviews"

versions:
 - "1.30.1--r41hdfd78af_1"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
 - "1.42.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-leebamviews"
config: {"url": "https://biocontainers.pro/tools/bioconductor-leebamviews", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-leebamviews", "latest": {"1.42.0--r44hdfd78af_0": "sha256:41a32bd5dcccab272573c28c3befc5c059a908d1d260a0db418d953e44e33cb5"}, "tags": {"1.30.1--r41hdfd78af_1": "sha256:3e6014da428d5add2b26f488e84c917f70892660a0c456fbe5b37537c181e37f", "1.34.0--r42hdfd78af_0": "sha256:ef5060536321e6674e9dbca933654f124387883412c0db4bc60f0a4b243090b8", "1.36.0--r43hdfd78af_0": "sha256:f6367dc2d9e80bcad841fc33ff2713c5f5f8e390a1dd216e2287535cc0789aba", "1.38.0--r43hdfd78af_0": "sha256:ccdea0e0ddffa8a9f76f9aa78b3d145d092d2dd231a3e9d7d47a399e69d49407", "1.42.0--r44hdfd78af_0": "sha256:41a32bd5dcccab272573c28c3befc5c059a908d1d260a0db418d953e44e33cb5"}, "docker": "quay.io/biocontainers/bioconductor-leebamviews"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-leebamviews.
shpc-registry automated BioContainers addition for bioconductor-leebamviews
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-leebamviews
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-leebamviews:1.42.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-leebamviews/1.42.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-leebamviews/1.42.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-leebamviews-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-leebamviews-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-leebamviews-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-leebamviews-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-leebamviews-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-leebamviews-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-leebamviews

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