---
layout: container
name:  "quay.io/biocontainers/samhaplotag"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samhaplotag/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/samhaplotag/container.yaml"
updated_at: "2024-11-28 04:27:45.691317"
latest: "0.0.4--h4ac6f70_3"
container_url: "https://biocontainers.pro/tools/samhaplotag"
aliases:
 - "10xSpoof"
 - "16BaseBCGen"
 - "SamHaplotag"
versions:
 - "0.0.4--h9f5acd7_1"
 - "0.0.4--h4ac6f70_3"
description: "shpc-registry automated BioContainers addition for samhaplotag"
config: {"url": "https://biocontainers.pro/tools/samhaplotag", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samhaplotag", "latest": {"0.0.4--h4ac6f70_3": "sha256:64ca167e1a3f282f8b99391b655775a1c2ef3909f29185a77f73ae06bbde6e53"}, "tags": {"0.0.4--h9f5acd7_1": "sha256:10c80be02ecc495c76de9d97d0060548a86591eb99de99fe08c86438c5c0e630", "0.0.4--h4ac6f70_3": "sha256:64ca167e1a3f282f8b99391b655775a1c2ef3909f29185a77f73ae06bbde6e53"}, "docker": "quay.io/biocontainers/samhaplotag", "aliases": {"10xSpoof": "/usr/local/bin/10xSpoof", "16BaseBCGen": "/usr/local/bin/16BaseBCGen", "SamHaplotag": "/usr/local/bin/SamHaplotag"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samhaplotag.
shpc-registry automated BioContainers addition for samhaplotag
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samhaplotag
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samhaplotag:0.0.4--h4ac6f70_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samhaplotag/0.0.4--h4ac6f70_3
$ module help quay.io/biocontainers/samhaplotag/0.0.4--h4ac6f70_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samhaplotag-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samhaplotag-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samhaplotag-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samhaplotag-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samhaplotag-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samhaplotag-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### 10xSpoof

```bash
$ singularity exec <container> /usr/local/bin/10xSpoof
$ podman run --it --rm --entrypoint /usr/local/bin/10xSpoof   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/10xSpoof   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 16BaseBCGen

```bash
$ singularity exec <container> /usr/local/bin/16BaseBCGen
$ podman run --it --rm --entrypoint /usr/local/bin/16BaseBCGen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/16BaseBCGen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SamHaplotag

```bash
$ singularity exec <container> /usr/local/bin/SamHaplotag
$ podman run --it --rm --entrypoint /usr/local/bin/SamHaplotag   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SamHaplotag   -v ${PWD} -w ${PWD} <container> -c " $@"
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