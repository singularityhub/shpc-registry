---
layout: container
name:  "quay.io/biocontainers/bioconductor-getdee2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-getdee2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-getdee2/container.yaml"
updated_at: "2024-01-05 02:42:41.200278"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-getdee2"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.7.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-getdee2"
config: {"url": "https://biocontainers.pro/tools/bioconductor-getdee2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-getdee2", "latest": {"1.12.0--r43hdfd78af_0": "sha256:6e15dd41e9414921db6419eb257d48e6660f8248252928e7979010fbf9139906"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:0841799d0e9366d5b18a1f29ddabffa855507af52b7781df31fc07fc30b4ef94", "1.7.0--r42hdfd78af_0": "sha256:b1b1a5758cbf36cb2be5cbcf99f70afa4a37816a766cfa0832d78064c10f5308", "1.10.0--r43hdfd78af_0": "sha256:c8a1b680251d094b334a2af01d2a21a6fa8ae1e3f008d986f3c493e9b56b7bff", "1.12.0--r43hdfd78af_0": "sha256:6e15dd41e9414921db6419eb257d48e6660f8248252928e7979010fbf9139906"}, "docker": "quay.io/biocontainers/bioconductor-getdee2"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-getdee2.
shpc-registry automated BioContainers addition for bioconductor-getdee2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-getdee2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-getdee2:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-getdee2/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-getdee2/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-getdee2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-getdee2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-getdee2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-getdee2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-getdee2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-getdee2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-getdee2

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