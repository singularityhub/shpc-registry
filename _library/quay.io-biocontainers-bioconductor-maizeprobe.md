---
layout: container
name:  "quay.io/biocontainers/bioconductor-maizeprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-maizeprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-maizeprobe/container.yaml"
updated_at: "2024-06-11 05:14:22.800583"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-maizeprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-maizeprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-maizeprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-maizeprobe", "latest": {"2.18.0--r43hdfd78af_12": "sha256:da01d2e4b5d20b6872b7b2d18619181b97eeabda236f9a2f92f47b4e71a71543"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:d57678c7a557bedb6540b998f5c4b059f36d98eb24c91cf409114f1c4ad77bd3", "2.18.0--r42hdfd78af_10": "sha256:8473e46f5dbf2429e2b49ef9ec9d4052bbca0dbe64afad423b3d5c3a3c6a54d8", "2.18.0--r43hdfd78af_11": "sha256:9e2075cd2a14e3148bf8f25f6a9d62e1ece07631c235565619aec8895615eb02", "2.18.0--r43hdfd78af_12": "sha256:da01d2e4b5d20b6872b7b2d18619181b97eeabda236f9a2f92f47b4e71a71543"}, "docker": "quay.io/biocontainers/bioconductor-maizeprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-maizeprobe.
shpc-registry automated BioContainers addition for bioconductor-maizeprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-maizeprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-maizeprobe:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-maizeprobe/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-maizeprobe/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-maizeprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maizeprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-maizeprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-maizeprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-maizeprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-maizeprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-maizeprobe

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