---
layout: container
name:  "quay.io/biocontainers/bioconductor-hu35ksubcprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-hu35ksubcprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-hu35ksubcprobe/container.yaml"
updated_at: "2024-12-02 03:26:14.092457"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-hu35ksubcprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-hu35ksubcprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-hu35ksubcprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-hu35ksubcprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:5921ac4ffe0a29b6f57b4f344ee15c7e544a5916fb1e7edfa2fc31ca9e2d876d"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:522520e85b725f8f480647319e0ef97825048e7e7da7a00728d3f2d0d96c6c0b", "2.18.0--r42hdfd78af_10": "sha256:6595e077c0c30c60d630e07a6f69ea3b54d78613fc55e67bd09670f0efd46e19", "2.18.0--r43hdfd78af_11": "sha256:1664e9ddb494086cb05a362669bc7881659f53505da644c5493105db746cd0c5", "2.18.0--r43hdfd78af_12": "sha256:5921ac4ffe0a29b6f57b4f344ee15c7e544a5916fb1e7edfa2fc31ca9e2d876d"}, "docker": "quay.io/biocontainers/bioconductor-hu35ksubcprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-hu35ksubcprobe.
shpc-registry automated BioContainers addition for bioconductor-hu35ksubcprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-hu35ksubcprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-hu35ksubcprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-hu35ksubcprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-hu35ksubcprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-hu35ksubcprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu35ksubcprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-hu35ksubcprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-hu35ksubcprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-hu35ksubcprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-hu35ksubcprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-hu35ksubcprobe

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