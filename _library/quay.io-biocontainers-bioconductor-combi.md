---
layout: container
name:  "quay.io/biocontainers/bioconductor-combi"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-combi/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-combi/container.yaml"
updated_at: "2024-10-07 16:43:31.803197"
latest: "1.14.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-combi"

versions:
 - "1.6.0--r41hdfd78af_0"
 - "1.10.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-combi"
config: {"url": "https://biocontainers.pro/tools/bioconductor-combi", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-combi", "latest": {"1.14.0--r43hdfd78af_0": "sha256:5ed60eca148929e96f8b1072383cfaecf7640acbf85de3de985c00d11266a280"}, "tags": {"1.6.0--r41hdfd78af_0": "sha256:9058b7b4ce3181c533cd8d1bc266890fe7f2dd806496fd25a38de46e501964e6", "1.10.0--r42hdfd78af_0": "sha256:7ba38414a5b4bb1b2287ea50303b0e157281253fc8a8a40fe696e4b6fc8ce0ed", "1.12.0--r43hdfd78af_0": "sha256:5ecf1da97c036f6f82cc34df4f96b763feca29f9d7f4e13d9c4f2430772fb9d4", "1.14.0--r43hdfd78af_0": "sha256:5ed60eca148929e96f8b1072383cfaecf7640acbf85de3de985c00d11266a280"}, "docker": "quay.io/biocontainers/bioconductor-combi"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-combi.
shpc-registry automated BioContainers addition for bioconductor-combi
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-combi
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-combi:1.14.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-combi/1.14.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-combi/1.14.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-combi-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-combi-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-combi-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-combi-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-combi-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-combi-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-combi

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