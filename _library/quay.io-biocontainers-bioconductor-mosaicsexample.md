---
layout: container
name:  "quay.io/biocontainers/bioconductor-mosaicsexample"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mosaicsexample/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mosaicsexample/container.yaml"
updated_at: "2023-10-12 03:38:33.895789"
latest: "1.35.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mosaicsexample"

versions:
 - "1.32.0--r41hdfd78af_1"
 - "1.35.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mosaicsexample"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mosaicsexample", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mosaicsexample", "latest": {"1.35.0--r42hdfd78af_0": "sha256:1bfdb74522ac80dca43bcd0cfe9804b3fb44591997b2edc905d10202c4ee8644"}, "tags": {"1.32.0--r41hdfd78af_1": "sha256:eb78e6f170399adab1ee79e414e75cdb8aedf60b5a4553d18c8ee8630ac4526a", "1.35.0--r42hdfd78af_0": "sha256:1bfdb74522ac80dca43bcd0cfe9804b3fb44591997b2edc905d10202c4ee8644"}, "docker": "quay.io/biocontainers/bioconductor-mosaicsexample"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mosaicsexample.
shpc-registry automated BioContainers addition for bioconductor-mosaicsexample
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mosaicsexample
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mosaicsexample:1.35.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mosaicsexample/1.35.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mosaicsexample/1.35.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mosaicsexample-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mosaicsexample-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mosaicsexample-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mosaicsexample-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mosaicsexample-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mosaicsexample-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mosaicsexample

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