---
layout: container
name:  "quay.io/biocontainers/snakemake-minimal"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/snakemake-minimal/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/snakemake-minimal/container.yaml"
updated_at: "2022-10-27 00:41:44.946662"
latest: "5.9.1--py_0"
container_url: "https://biocontainers.pro/tools/snakemake-minimal"

versions:
 - "5.9.1--py_0"
description: "shpc-registry automated BioContainers addition for snakemake-minimal"
config: {"url": "https://biocontainers.pro/tools/snakemake-minimal", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for snakemake-minimal", "latest": {"5.9.1--py_0": "sha256:46611f4b19c9f6e11d9a159af8ded402e59d78d24f2dac6fec24210fde8c602c"}, "tags": {"5.9.1--py_0": "sha256:46611f4b19c9f6e11d9a159af8ded402e59d78d24f2dac6fec24210fde8c602c"}, "docker": "quay.io/biocontainers/snakemake-minimal"}
---

This module is a singularity container wrapper for quay.io/biocontainers/snakemake-minimal.
shpc-registry automated BioContainers addition for snakemake-minimal
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/snakemake-minimal
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/snakemake-minimal:5.9.1--py_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/snakemake-minimal/5.9.1--py_0
$ module help quay.io/biocontainers/snakemake-minimal/5.9.1--py_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### snakemake-minimal-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-minimal-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### snakemake-minimal-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### snakemake-minimal-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### snakemake-minimal-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### snakemake-minimal-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### snakemake-minimal

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