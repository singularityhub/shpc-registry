---
layout: container
name:  "quay.io/biocontainers/bioconductor-podcall"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-podcall/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-podcall/container.yaml"
updated_at: "2023-12-06 02:39:55.163699"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-podcall"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-podcall"
config: {"url": "https://biocontainers.pro/tools/bioconductor-podcall", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-podcall", "latest": {"1.8.0--r43hdfd78af_0": "sha256:d849c3a4ab2b3edb955020047ca41f40ccf4e594a90cc54c70e50926f9dfc830"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:a2bf33133c0bb4b0e859bd9f569810faea70f5eece1a9fc62ac16aa53ad8370a", "1.6.0--r42hdfd78af_0": "sha256:04c03cf7b56deec125cd8f37f80227753b91224e51a0be31e2f3c61f52f70396", "1.8.0--r43hdfd78af_0": "sha256:d849c3a4ab2b3edb955020047ca41f40ccf4e594a90cc54c70e50926f9dfc830"}, "docker": "quay.io/biocontainers/bioconductor-podcall"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-podcall.
shpc-registry automated BioContainers addition for bioconductor-podcall
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-podcall
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-podcall:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-podcall/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-podcall/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-podcall-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-podcall-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-podcall-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-podcall-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-podcall-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-podcall-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-podcall

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