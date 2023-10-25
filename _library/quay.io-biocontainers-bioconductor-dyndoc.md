---
layout: container
name:  "quay.io/biocontainers/bioconductor-dyndoc"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dyndoc/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dyndoc/container.yaml"
updated_at: "2023-10-25 02:26:46.657435"
latest: "1.78.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dyndoc"

versions:
 - "1.72.0--r41hdfd78af_0"
 - "1.76.0--r42hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dyndoc"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dyndoc", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dyndoc", "latest": {"1.78.0--r43hdfd78af_0": "sha256:527078229e26db735ab33a31d722328f25fb215a215022f1bdc765bd16e84cda"}, "tags": {"1.72.0--r41hdfd78af_0": "sha256:f625001edb7fc3f659a6edf8ebc35f5468f45cc9bf14e6a80c9c4df7e0cb9455", "1.76.0--r42hdfd78af_0": "sha256:d1fe05c456d8fb464796897648cee69cb2982897a00fb5c9eb87aa6444d4b47d", "1.78.0--r43hdfd78af_0": "sha256:527078229e26db735ab33a31d722328f25fb215a215022f1bdc765bd16e84cda"}, "docker": "quay.io/biocontainers/bioconductor-dyndoc"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dyndoc.
shpc-registry automated BioContainers addition for bioconductor-dyndoc
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dyndoc
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dyndoc:1.78.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dyndoc/1.78.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dyndoc/1.78.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dyndoc-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dyndoc-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dyndoc-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dyndoc-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dyndoc-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dyndoc-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dyndoc

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