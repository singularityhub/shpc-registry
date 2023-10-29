---
layout: container
name:  "quay.io/biocontainers/bioconductor-filterffpe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-filterffpe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-filterffpe/container.yaml"
updated_at: "2023-10-29 03:19:56.766898"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-filterffpe"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-filterffpe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-filterffpe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-filterffpe", "latest": {"1.10.0--r43hdfd78af_0": "sha256:f00f79fec2cf25eee8e337784287086c9b38edd36c4a320e9b64af7d0114b52b"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:43e253a3e683428a422f93acddeeea027d2fe10a25b5e581bab4823ccf6ca82d", "1.8.0--r42hdfd78af_0": "sha256:799e67670094cea5107573a3864011850082c291a3277a07dc0e25c8159d150d", "1.10.0--r43hdfd78af_0": "sha256:f00f79fec2cf25eee8e337784287086c9b38edd36c4a320e9b64af7d0114b52b"}, "docker": "quay.io/biocontainers/bioconductor-filterffpe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-filterffpe.
shpc-registry automated BioContainers addition for bioconductor-filterffpe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-filterffpe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-filterffpe:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-filterffpe/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-filterffpe/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-filterffpe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-filterffpe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-filterffpe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-filterffpe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-filterffpe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-filterffpe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-filterffpe

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