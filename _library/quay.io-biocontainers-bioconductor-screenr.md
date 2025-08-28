---
layout: container
name:  "quay.io/biocontainers/bioconductor-screenr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-screenr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-screenr/container.yaml"
updated_at: "2025-08-28 03:25:29.168317"
latest: "1.8.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-screenr"

versions:
 - "1.0.0--r42hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
 - "1.8.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-screenr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-screenr", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-screenr", "latest": {"1.8.0--r44hdfd78af_0": "sha256:e1a7f9137a0401173df9c50a21430f59c1788f2d4e7b86dbcb44897ceadc8080"}, "tags": {"1.0.0--r42hdfd78af_0": "sha256:fe094028144f66655e1573b6e3620b8de3e0f208aa43773984f5c997444846ed", "1.2.0--r43hdfd78af_0": "sha256:6ec7ffbbafae75dccad12513cdbed916026d1ab4d0788ae253f2b320510a860c", "1.4.0--r43hdfd78af_0": "sha256:fe5412d96da84d3ae75d7273d61f2a485b0a56aa6ec78eb39b7aaae76de14faa", "1.8.0--r44hdfd78af_0": "sha256:e1a7f9137a0401173df9c50a21430f59c1788f2d4e7b86dbcb44897ceadc8080"}, "docker": "quay.io/biocontainers/bioconductor-screenr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-screenr.
singularity registry hpc automated addition for bioconductor-screenr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-screenr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-screenr:1.8.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-screenr/1.8.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-screenr/1.8.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-screenr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-screenr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-screenr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-screenr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-screenr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-screenr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-screenr

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