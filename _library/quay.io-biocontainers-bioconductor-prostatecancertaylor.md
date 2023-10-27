---
layout: container
name:  "quay.io/biocontainers/bioconductor-prostatecancertaylor"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-prostatecancertaylor/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-prostatecancertaylor/container.yaml"
updated_at: "2023-10-27 02:46:34.127708"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-prostatecancertaylor"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-prostatecancertaylor"
config: {"url": "https://biocontainers.pro/tools/bioconductor-prostatecancertaylor", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-prostatecancertaylor", "latest": {"1.28.0--r43hdfd78af_0": "sha256:0ba39e7682301178f62276919ac37819bf5a88d4fcaed759746818cd8dcbd8a7"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:25e5f8b0c4cef292a613861e514fc045a3dfb964d6116366c6ed6e74d53810e4", "1.26.0--r42hdfd78af_0": "sha256:677946d485abf654db708aa6affd0edfd8d2d6524f1365aaa52133bfbc8b306b", "1.28.0--r43hdfd78af_0": "sha256:0ba39e7682301178f62276919ac37819bf5a88d4fcaed759746818cd8dcbd8a7"}, "docker": "quay.io/biocontainers/bioconductor-prostatecancertaylor"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-prostatecancertaylor.
shpc-registry automated BioContainers addition for bioconductor-prostatecancertaylor
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancertaylor
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-prostatecancertaylor:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-prostatecancertaylor/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-prostatecancertaylor/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-prostatecancertaylor-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancertaylor-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-prostatecancertaylor-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-prostatecancertaylor-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-prostatecancertaylor-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-prostatecancertaylor-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-prostatecancertaylor

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