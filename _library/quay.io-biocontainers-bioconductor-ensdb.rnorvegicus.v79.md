---
layout: container
name:  "quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v79"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v79/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v79/container.yaml"
updated_at: "2023-08-21 03:15:14.196450"
latest: "2.99.0--r43hdfd78af_11"
container_url: "https://biocontainers.pro/tools/bioconductor-ensdb.rnorvegicus.v79"

versions:
 - "2.99.0--r41hdfd78af_9"
 - "2.99.0--r42hdfd78af_10"
 - "2.99.0--r43hdfd78af_11"
description: "shpc-registry automated BioContainers addition for bioconductor-ensdb.rnorvegicus.v79"
config: {"url": "https://biocontainers.pro/tools/bioconductor-ensdb.rnorvegicus.v79", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-ensdb.rnorvegicus.v79", "latest": {"2.99.0--r43hdfd78af_11": "sha256:7e7b02fb9287d4376a75d43da52cf2bcb040d3f748c28317f060448bb5633b33"}, "tags": {"2.99.0--r41hdfd78af_9": "sha256:090de2ffe6715859c56cb106fc9389aab579be66c464d026cd3bf95e2ad1a3a6", "2.99.0--r42hdfd78af_10": "sha256:42012ef16c8c850c81bb2bfe697121670f5d222f6239e4af50c0aa22ff472d5b", "2.99.0--r43hdfd78af_11": "sha256:7e7b02fb9287d4376a75d43da52cf2bcb040d3f748c28317f060448bb5633b33"}, "docker": "quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v79"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v79.
shpc-registry automated BioContainers addition for bioconductor-ensdb.rnorvegicus.v79
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v79
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v79:2.99.0--r43hdfd78af_11
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v79/2.99.0--r43hdfd78af_11
$ module help quay.io/biocontainers/bioconductor-ensdb.rnorvegicus.v79/2.99.0--r43hdfd78af_11
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-ensdb.rnorvegicus.v79-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.rnorvegicus.v79-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-ensdb.rnorvegicus.v79-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-ensdb.rnorvegicus.v79-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-ensdb.rnorvegicus.v79-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-ensdb.rnorvegicus.v79-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-ensdb.rnorvegicus.v79

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