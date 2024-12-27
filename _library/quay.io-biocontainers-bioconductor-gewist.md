---
layout: container
name:  "quay.io/biocontainers/bioconductor-gewist"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-gewist/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-gewist/container.yaml"
updated_at: "2024-12-27 03:05:16.123266"
latest: "1.46.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-gewist"

versions:
 - "1.38.0--r41hdfd78af_0"
 - "1.42.0--r42hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.46.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-gewist"
config: {"url": "https://biocontainers.pro/tools/bioconductor-gewist", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-gewist", "latest": {"1.46.0--r43hdfd78af_0": "sha256:e621205ff7596efed6f8c5844548ccfa86f3f875ffd8acf2ee2ef7b1f0c34856"}, "tags": {"1.38.0--r41hdfd78af_0": "sha256:26376253ffa0569fd4b80d0780ef3b37412f90cd28be608527962917e81f4cfc", "1.42.0--r42hdfd78af_0": "sha256:1e6fb38531f65b1dbe3528bbebd9c9bbc9f4a71e238cc275778babc6d68c584b", "1.44.0--r43hdfd78af_0": "sha256:e26c893aafd357dea2b0dd08759fbbc29eaeb58fb656ee4685c8c00a49dd5a13", "1.46.0--r43hdfd78af_0": "sha256:e621205ff7596efed6f8c5844548ccfa86f3f875ffd8acf2ee2ef7b1f0c34856"}, "docker": "quay.io/biocontainers/bioconductor-gewist"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-gewist.
shpc-registry automated BioContainers addition for bioconductor-gewist
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-gewist
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-gewist:1.46.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-gewist/1.46.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-gewist/1.46.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-gewist-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gewist-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-gewist-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-gewist-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-gewist-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-gewist-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-gewist

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