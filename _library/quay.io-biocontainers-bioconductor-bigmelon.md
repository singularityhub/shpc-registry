---
layout: container
name:  "quay.io/biocontainers/bioconductor-bigmelon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bigmelon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bigmelon/container.yaml"
updated_at: "2023-07-15 04:00:35.275559"
latest: "1.24.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-bigmelon"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-bigmelon"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bigmelon", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bigmelon", "latest": {"1.24.0--r42hdfd78af_0": "sha256:1b8c1bd73ac18ecef79108030996952ee04547def45d89fceecd2259b9a9e112"}, "tags": {"1.8.0--r351_0": "sha256:6e3d8bc360f13859f9c2fd75ef304cf74823fb5a2cf89c03a9a8b2971db8796f", "1.24.0--r42hdfd78af_0": "sha256:1b8c1bd73ac18ecef79108030996952ee04547def45d89fceecd2259b9a9e112", "1.20.0--r41hdfd78af_0": "sha256:ac27ddd5c07fa81e24d606f8e3c9085ec2472133c156be8d957b44fa8eb52409", "1.18.0--r41hdfd78af_0": "sha256:d47d5222a2b82032a157881347627e1be1919713102e03865b61530233586f1d", "1.16.0--r40hdfd78af_1": "sha256:c248c97262f1b4ca7f1a7d2450c58d5eb07341ca641c95745e2aba5177465890", "1.14.0--r40_0": "sha256:aeab6a67014763ee1f093e4dbc5ab95960bf2d2d96aca96cadcc6579e9fc245c"}, "docker": "quay.io/biocontainers/bioconductor-bigmelon", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bigmelon.
shpc-registry automated BioContainers addition for bioconductor-bigmelon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bigmelon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bigmelon:1.24.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bigmelon/1.24.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-bigmelon/1.24.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bigmelon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bigmelon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bigmelon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bigmelon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bigmelon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bigmelon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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