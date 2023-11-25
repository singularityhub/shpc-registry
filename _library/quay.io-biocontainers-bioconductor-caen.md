---
layout: container
name:  "quay.io/biocontainers/bioconductor-caen"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-caen/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-caen/container.yaml"
updated_at: "2023-11-25 02:42:39.124194"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-caen"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-caen"
config: {"url": "https://biocontainers.pro/tools/bioconductor-caen", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-caen", "latest": {"1.8.0--r43hdfd78af_0": "sha256:a34dcd4fc10ed76c31834fc1b123a06433ca506b2caf2893a6de250edca32960"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:7ebb971bf58ad294c9ae1226713ce66facc1820440374a0be7e5880954a8b93d", "1.6.0--r42hdfd78af_0": "sha256:2876ad4407391dedad562f6e092685c5b3c6732989a2ac4ce6874e6f1bcc87bb", "1.8.0--r43hdfd78af_0": "sha256:a34dcd4fc10ed76c31834fc1b123a06433ca506b2caf2893a6de250edca32960"}, "docker": "quay.io/biocontainers/bioconductor-caen"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-caen.
shpc-registry automated BioContainers addition for bioconductor-caen
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-caen
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-caen:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-caen/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-caen/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-caen-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-caen-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-caen-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-caen-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-caen-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-caen-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-caen

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