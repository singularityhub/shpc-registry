---
layout: container
name:  "quay.io/biocontainers/bioconductor-epinem"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-epinem/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-epinem/container.yaml"
updated_at: "2023-03-20 03:35:01.341392"
latest: "1.22.0--r42hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-epinem"

versions:
 - "1.18.0--r41hdfd78af_0"
 - "1.22.0--r42hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-epinem"
config: {"url": "https://biocontainers.pro/tools/bioconductor-epinem", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-epinem", "latest": {"1.22.0--r42hdfd78af_0": "sha256:7ce333bfc28e508ebb06fed1e28dcef93da2219318788cda770d350678d331be"}, "tags": {"1.18.0--r41hdfd78af_0": "sha256:a532d06a387e715c3a83ab945f52d749d9c7385913c7c8880e7f8a6f9f393220", "1.22.0--r42hdfd78af_0": "sha256:7ce333bfc28e508ebb06fed1e28dcef93da2219318788cda770d350678d331be"}, "docker": "quay.io/biocontainers/bioconductor-epinem"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-epinem.
shpc-registry automated BioContainers addition for bioconductor-epinem
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-epinem
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-epinem:1.22.0--r42hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-epinem/1.22.0--r42hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-epinem/1.22.0--r42hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-epinem-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epinem-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-epinem-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-epinem-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-epinem-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-epinem-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-epinem

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