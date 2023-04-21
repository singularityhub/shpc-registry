---
layout: container
name:  "quay.io/biocontainers/bioconductor-pchicdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pchicdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pchicdata/container.yaml"
updated_at: "2023-04-21 02:57:47.679408"
latest: "1.25.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pchicdata"
aliases:
 - "wget"
versions:
 - "1.8.0--r351_0"
 - "1.25.0--r42hdfd78af_0"
 - "1.22.1--r41hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r40hdfd78af_1"
 - "1.16.0--r40_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pchicdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pchicdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pchicdata", "latest": {"1.25.0--r42hdfd78af_0": "sha256:72a25ceae4e7d0009f1224e957e5c7bbcd646c94a7f74d51fc8c469a4efb4269"}, "tags": {"1.8.0--r351_0": "sha256:31db2d778c86b1ec714ead88f92adc0d87a551573f483912e8a87081d08249e6", "1.25.0--r42hdfd78af_0": "sha256:72a25ceae4e7d0009f1224e957e5c7bbcd646c94a7f74d51fc8c469a4efb4269", "1.22.1--r41hdfd78af_0": "sha256:54bdc42d3e9f62c940de0051d2c5079b206f6f21f698f003ae7ab1ef5bd45d1a", "1.20.0--r41hdfd78af_0": "sha256:9d3843ab34f3a40b7712e7635da9ec7b62d8371be02c78b57de7c57d2fec298e", "1.18.0--r40hdfd78af_1": "sha256:1bddf40408f5380abb61e6d0ea552e928e7818ba2429b7ffdd2eaee72afd8085", "1.16.0--r40_0": "sha256:e740e4a8dec773eac03238a09faa3b55c3e7dce39aa22febdd03bcac9a5a6d00"}, "docker": "quay.io/biocontainers/bioconductor-pchicdata", "aliases": {"wget": "/usr/local/bin/wget"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pchicdata.
shpc-registry automated BioContainers addition for bioconductor-pchicdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pchicdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pchicdata:1.25.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pchicdata/1.25.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pchicdata/1.25.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pchicdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pchicdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pchicdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pchicdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pchicdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pchicdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
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