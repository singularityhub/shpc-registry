---
layout: container
name:  "quay.io/biocontainers/bioconductor-easyreporting"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-easyreporting/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-easyreporting/container.yaml"
updated_at: "2023-08-12 02:22:24.703493"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-easyreporting"
aliases:
 - "pandoc"
versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-easyreporting"
config: {"url": "https://biocontainers.pro/tools/bioconductor-easyreporting", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-easyreporting", "latest": {"1.12.0--r43hdfd78af_0": "sha256:5e4f4ce3433e692d6fc6d6e41581e662bddbd13d31792f95c7d555c0f4b76e8e"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:8b9bfa934772943797b94c086f0ea13d39d5a4085d934677c666a2c314641c55", "1.10.0--r42hdfd78af_0": "sha256:a15f3199de73fda123774a8db620dc65db46e77a3d44bf52664a3b535cc105fb", "1.12.0--r43hdfd78af_0": "sha256:5e4f4ce3433e692d6fc6d6e41581e662bddbd13d31792f95c7d555c0f4b76e8e"}, "docker": "quay.io/biocontainers/bioconductor-easyreporting", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-easyreporting.
shpc-registry automated BioContainers addition for bioconductor-easyreporting
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-easyreporting
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-easyreporting:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-easyreporting/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-easyreporting/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-easyreporting-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-easyreporting-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-easyreporting-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-easyreporting-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-easyreporting-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-easyreporting-inspect-deffile:

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