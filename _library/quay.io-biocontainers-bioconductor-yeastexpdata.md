---
layout: container
name:  "quay.io/biocontainers/bioconductor-yeastexpdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-yeastexpdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-yeastexpdata/container.yaml"
updated_at: "2026-01-06 03:54:22.508275"
latest: "0.52.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-yeastexpdata"

versions:
 - "0.40.0--r41hdfd78af_1"
 - "0.44.0--r42hdfd78af_0"
 - "0.46.0--r43hdfd78af_0"
 - "0.48.0--r43hdfd78af_0"
 - "0.52.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-yeastexpdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-yeastexpdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-yeastexpdata", "latest": {"0.52.0--r44hdfd78af_0": "sha256:bd1bab6203d657c58fac2028b635c87d9f77f197d494c4e774785b04d180fcbb"}, "tags": {"0.40.0--r41hdfd78af_1": "sha256:b91cbc19e73158a8903f5b9edd5d86117f8e88e86e277af80ae5dac2e78f1af8", "0.44.0--r42hdfd78af_0": "sha256:a76ec3581f65a33fa907a3755f8c6393d34ac36ecb3199f12e39e806f30b36eb", "0.46.0--r43hdfd78af_0": "sha256:2d8bc88e647568e7403fb48af591212329e24adf2a9dd2ce932769660eb2ab30", "0.48.0--r43hdfd78af_0": "sha256:b4b696a48a7d931d64fe0366e46b472af92f297dab8c69505e10763d2f5ad9da", "0.52.0--r44hdfd78af_0": "sha256:bd1bab6203d657c58fac2028b635c87d9f77f197d494c4e774785b04d180fcbb"}, "docker": "quay.io/biocontainers/bioconductor-yeastexpdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-yeastexpdata.
shpc-registry automated BioContainers addition for bioconductor-yeastexpdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-yeastexpdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-yeastexpdata:0.52.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-yeastexpdata/0.52.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-yeastexpdata/0.52.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-yeastexpdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeastexpdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-yeastexpdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-yeastexpdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-yeastexpdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-yeastexpdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-yeastexpdata

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