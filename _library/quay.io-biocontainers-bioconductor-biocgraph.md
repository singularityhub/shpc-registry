---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocgraph"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocgraph/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocgraph/container.yaml"
updated_at: "2022-11-17 03:44:59.625192"
latest: "1.56.0--r41hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocgraph"

versions:
 - "1.56.0--r41hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocgraph"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocgraph", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocgraph", "latest": {"1.56.0--r41hdfd78af_0": "sha256:da95f36f23344e1375074ee48da7c2d795873a4caf1f3bfbc6352e1a50cfd1db"}, "tags": {"1.56.0--r41hdfd78af_0": "sha256:da95f36f23344e1375074ee48da7c2d795873a4caf1f3bfbc6352e1a50cfd1db"}, "docker": "quay.io/biocontainers/bioconductor-biocgraph"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocgraph.
shpc-registry automated BioContainers addition for bioconductor-biocgraph
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocgraph
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocgraph:1.56.0--r41hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocgraph/1.56.0--r41hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocgraph/1.56.0--r41hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocgraph-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocgraph-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocgraph-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocgraph-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocgraph-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocgraph-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biocgraph

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