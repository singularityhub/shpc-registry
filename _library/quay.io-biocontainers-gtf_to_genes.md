---
layout: container
name:  "quay.io/biocontainers/gtf_to_genes"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gtf_to_genes/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/gtf_to_genes/container.yaml"
updated_at: "2022-10-27 01:13:07.038469"
latest: "1.40--py_2"
container_url: "https://biocontainers.pro/tools/gtf_to_genes"

versions:
 - "1.40--py_2"
description: "shpc-registry automated BioContainers addition for gtf_to_genes"
config: {"url": "https://biocontainers.pro/tools/gtf_to_genes", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for gtf_to_genes", "latest": {"1.40--py_2": "sha256:09c2e8d0f4bfee710a087edbfc9ae4ff35247b5a0ced8bf24bf13c2053b9613a"}, "tags": {"1.40--py_2": "sha256:09c2e8d0f4bfee710a087edbfc9ae4ff35247b5a0ced8bf24bf13c2053b9613a"}, "docker": "quay.io/biocontainers/gtf_to_genes"}
---

This module is a singularity container wrapper for quay.io/biocontainers/gtf_to_genes.
shpc-registry automated BioContainers addition for gtf_to_genes
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gtf_to_genes
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gtf_to_genes:1.40--py_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gtf_to_genes/1.40--py_2
$ module help quay.io/biocontainers/gtf_to_genes/1.40--py_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gtf_to_genes-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gtf_to_genes-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gtf_to_genes-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gtf_to_genes-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gtf_to_genes-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gtf_to_genes-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### gtf_to_genes

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