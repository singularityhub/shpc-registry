---
layout: container
name:  "quay.io/biocontainers/bioconductor-informeasure"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-informeasure/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-informeasure/container.yaml"
updated_at: "2023-09-08 03:21:59.238135"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-informeasure"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-informeasure"
config: {"url": "https://biocontainers.pro/tools/bioconductor-informeasure", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-informeasure", "latest": {"1.10.0--r43hdfd78af_0": "sha256:133137f247cad11790a8784c19f35054b723f0e75817a7c1e28fa7c6097e5937"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:9f2dcaf2c6bb83c2f03d92cf4b0c242f88baca0f4e0d7e13b3db9851a837ee75", "1.8.0--r42hdfd78af_0": "sha256:6a8984e219a6376b52b7afec033d5c86d7043b845290aa2de1800f14314b9fc2", "1.10.0--r43hdfd78af_0": "sha256:133137f247cad11790a8784c19f35054b723f0e75817a7c1e28fa7c6097e5937"}, "docker": "quay.io/biocontainers/bioconductor-informeasure"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-informeasure.
shpc-registry automated BioContainers addition for bioconductor-informeasure
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-informeasure
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-informeasure:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-informeasure/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-informeasure/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-informeasure-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-informeasure-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-informeasure-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-informeasure-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-informeasure-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-informeasure-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-informeasure

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