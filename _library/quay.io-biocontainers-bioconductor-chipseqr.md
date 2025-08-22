---
layout: container
name:  "quay.io/biocontainers/bioconductor-chipseqr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chipseqr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chipseqr/container.yaml"
updated_at: "2025-08-22 03:52:49.321490"
latest: "1.60.0--r44h3df3fcb_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chipseqr"

versions:
 - "1.48.0--r41hc0cfd56_2"
 - "1.52.0--r42hc0cfd56_0"
 - "1.52.0--r42ha9d7317_1"
 - "1.54.0--r43ha9d7317_0"
 - "1.56.0--r43ha9d7317_0"
 - "1.56.0--r43ha9d7317_1"
 - "1.60.0--r44h3df3fcb_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chipseqr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chipseqr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chipseqr", "latest": {"1.60.0--r44h3df3fcb_0": "sha256:8229b3627a5f9d9d5d6d413a5caa5384c7e3dadfa726b05cdba63fe1c70de7a2"}, "tags": {"1.48.0--r41hc0cfd56_2": "sha256:86cf9673db70cfc6758f9e99a1f3b85773b450360ea2da0e647971b73393e0b1", "1.52.0--r42hc0cfd56_0": "sha256:93c4896a67d868ffa21ca9b93b93d040dc0aec0590d33f6bd78e684984f61c9b", "1.52.0--r42ha9d7317_1": "sha256:4ad34be10f226cb2926685fb9b3aa810e01d5b3da64c0f9563a5ad9c68c1dc10", "1.54.0--r43ha9d7317_0": "sha256:5261145d1583873ccb2420a078d1f613de647f5ca65c5281e8378c7ad70d6abf", "1.56.0--r43ha9d7317_0": "sha256:3798e3fcb9880497a010ae2ba556f6c9c0af8e215d0325868aa8693a90c74c43", "1.56.0--r43ha9d7317_1": "sha256:a6e434050f57c63b2decf312378bff8e9235017c99d9d0e697e2f382774f433d", "1.60.0--r44h3df3fcb_0": "sha256:8229b3627a5f9d9d5d6d413a5caa5384c7e3dadfa726b05cdba63fe1c70de7a2"}, "docker": "quay.io/biocontainers/bioconductor-chipseqr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chipseqr.
shpc-registry automated BioContainers addition for bioconductor-chipseqr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chipseqr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chipseqr:1.60.0--r44h3df3fcb_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chipseqr/1.60.0--r44h3df3fcb_0
$ module help quay.io/biocontainers/bioconductor-chipseqr/1.60.0--r44h3df3fcb_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chipseqr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipseqr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chipseqr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chipseqr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chipseqr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chipseqr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chipseqr

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