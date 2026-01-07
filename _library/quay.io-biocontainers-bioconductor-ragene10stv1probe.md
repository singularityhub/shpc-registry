---
layout: container
name:  "quay.io/biocontainers/bioconductor-ragene10stv1probe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ragene10stv1probe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ragene10stv1probe/container.yaml"
updated_at: "2026-01-07 04:04:01.496342"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-ragene10stv1probe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-ragene10stv1probe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ragene10stv1probe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ragene10stv1probe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:9710bc545f7020e6fe20c7a43c75892d32ae979709170594a50d354ebb8e8f63"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:c763f928350c4dc7dbf2a5cc99828fc151ae79dc71e020ea2e159174680fd1c9", "2.18.0--r42hdfd78af_10": "sha256:cd98fa80081d37e2ec9f353bbb1cd06c0126c593ff6ab621ae8147a722fb3e4e", "2.18.0--r43hdfd78af_11": "sha256:55784d7d16969b951f76e73aa5fb08e738a9f78ba731de280905ae4ead808fdd", "2.18.0--r43hdfd78af_12": "sha256:74f96f251ea9e260d4e166d4b7148a065c72a69def0b0121a28f6e2388d8c962", "2.18.0--r44hdfd78af_13": "sha256:9710bc545f7020e6fe20c7a43c75892d32ae979709170594a50d354ebb8e8f63"}, "docker": "quay.io/biocontainers/bioconductor-ragene10stv1probe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ragene10stv1probe.
shpc-registry automated BioContainers addition for bioconductor-ragene10stv1probe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ragene10stv1probe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ragene10stv1probe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ragene10stv1probe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-ragene10stv1probe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ragene10stv1probe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ragene10stv1probe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ragene10stv1probe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ragene10stv1probe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ragene10stv1probe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ragene10stv1probe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ragene10stv1probe

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