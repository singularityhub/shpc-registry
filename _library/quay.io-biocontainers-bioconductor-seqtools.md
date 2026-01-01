---
layout: container
name:  "quay.io/biocontainers/bioconductor-seqtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-seqtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-seqtools/container.yaml"
updated_at: "2026-01-01 04:13:47.069639"
latest: "1.40.0--r44h15a9599_1"
container_url: "https://biocontainers.pro/tools/bioconductor-seqtools"

versions:
 - "1.28.0--r41hc0cfd56_2"
 - "1.32.0--r42hc0cfd56_0"
 - "1.32.0--r42ha9d7317_1"
 - "1.34.0--r43ha9d7317_0"
 - "1.36.0--r43ha9d7317_0"
 - "1.40.0--r44h15a9599_0"
 - "1.40.0--r44h15a9599_1"
description: "shpc-registry automated BioContainers addition for bioconductor-seqtools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-seqtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-seqtools", "latest": {"1.40.0--r44h15a9599_1": "sha256:bff24f64154fd26e8055cd9e1bcffe7460a62dc9a98a470e8546153ed54951de"}, "tags": {"1.28.0--r41hc0cfd56_2": "sha256:4a07326237af9204015d4474871ce658142e895fbb1ac3b9c3007322523446e6", "1.32.0--r42hc0cfd56_0": "sha256:b2d49a5a10185c100207b123fcdd35267fd0512e003588da35bad36a9bd5b9de", "1.32.0--r42ha9d7317_1": "sha256:3c31c2ec36da254c6de4dc2ae9b3af4949382ba1cbb45f89947ab76c6c0c29a9", "1.34.0--r43ha9d7317_0": "sha256:fbc62bf8192de9a6f0d8744777b71900c4aae8680c5543d24be6aa7c7388b18b", "1.36.0--r43ha9d7317_0": "sha256:aa94cf7048b03bea540111d12f5b7de3695a78f1d972d758e11718f51ea35c77", "1.40.0--r44h15a9599_0": "sha256:928493feba19132f3aedc2ecc754518b5e44202f7fe147f3661f42674e800f68", "1.40.0--r44h15a9599_1": "sha256:bff24f64154fd26e8055cd9e1bcffe7460a62dc9a98a470e8546153ed54951de"}, "docker": "quay.io/biocontainers/bioconductor-seqtools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-seqtools.
shpc-registry automated BioContainers addition for bioconductor-seqtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-seqtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-seqtools:1.40.0--r44h15a9599_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-seqtools/1.40.0--r44h15a9599_1
$ module help quay.io/biocontainers/bioconductor-seqtools/1.40.0--r44h15a9599_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-seqtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-seqtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-seqtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-seqtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-seqtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-seqtools

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