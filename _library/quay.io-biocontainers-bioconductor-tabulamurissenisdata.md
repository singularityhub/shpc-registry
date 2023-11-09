---
layout: container
name:  "quay.io/biocontainers/bioconductor-tabulamurissenisdata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-tabulamurissenisdata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-tabulamurissenisdata/container.yaml"
updated_at: "2023-11-09 02:41:37.954897"
latest: "1.6.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-tabulamurissenisdata"

versions:
 - "1.0.0--r41hdfd78af_1"
 - "1.4.0--r42hdfd78af_0"
 - "1.6.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-tabulamurissenisdata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-tabulamurissenisdata", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-tabulamurissenisdata", "latest": {"1.6.0--r43hdfd78af_0": "sha256:a4cac3ccaa87fd76404de825fd98d96ea5c385a0262f202a09fd90a2cda8844c"}, "tags": {"1.0.0--r41hdfd78af_1": "sha256:b310b585a4a1b0f2c0068823cfdb2e8e84dfe033b4dc5a38b5f219976c52192e", "1.4.0--r42hdfd78af_0": "sha256:4552a6b944e6726e221658494750b3d4bd9218aa3fef9ddd3bff1f0875ff8bee", "1.6.0--r43hdfd78af_0": "sha256:a4cac3ccaa87fd76404de825fd98d96ea5c385a0262f202a09fd90a2cda8844c"}, "docker": "quay.io/biocontainers/bioconductor-tabulamurissenisdata"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-tabulamurissenisdata.
shpc-registry automated BioContainers addition for bioconductor-tabulamurissenisdata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-tabulamurissenisdata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-tabulamurissenisdata:1.6.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-tabulamurissenisdata/1.6.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-tabulamurissenisdata/1.6.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-tabulamurissenisdata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tabulamurissenisdata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-tabulamurissenisdata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-tabulamurissenisdata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-tabulamurissenisdata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-tabulamurissenisdata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-tabulamurissenisdata

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