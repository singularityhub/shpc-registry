---
layout: container
name:  "quay.io/biocontainers/bioconductor-demuxmix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-demuxmix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-demuxmix/container.yaml"
updated_at: "2024-02-15 02:47:05.876590"
latest: "1.4.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-demuxmix"

versions:
 - "1.0.0--r42hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.4.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-demuxmix"
config: {"url": "https://biocontainers.pro/tools/bioconductor-demuxmix", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-demuxmix", "latest": {"1.4.0--r43hdfd78af_0": "sha256:cd54ad260541c570da83642feb78825669a3efcb37d07b9ec1bbad9e5a16bc74"}, "tags": {"1.0.0--r42hdfd78af_0": "sha256:0bc32cda529db7826e0d00ad8ff605e2b4a005550c42c8acc554d82ed4703232", "1.2.0--r43hdfd78af_0": "sha256:976274ed70531bfb8b2606a3c02d971c59a6f10013b3c9c5374dd10e6f8351ed", "1.4.0--r43hdfd78af_0": "sha256:cd54ad260541c570da83642feb78825669a3efcb37d07b9ec1bbad9e5a16bc74"}, "docker": "quay.io/biocontainers/bioconductor-demuxmix"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-demuxmix.
singularity registry hpc automated addition for bioconductor-demuxmix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-demuxmix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-demuxmix:1.4.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-demuxmix/1.4.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-demuxmix/1.4.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-demuxmix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-demuxmix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-demuxmix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-demuxmix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-demuxmix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-demuxmix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-demuxmix

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