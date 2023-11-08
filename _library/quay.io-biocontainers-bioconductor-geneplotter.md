---
layout: container
name:  "quay.io/biocontainers/bioconductor-geneplotter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-geneplotter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-geneplotter/container.yaml"
updated_at: "2023-11-08 03:21:18.074333"
latest: "1.78.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-geneplotter"

versions:
 - "1.72.0--r41hdfd78af_0"
 - "1.76.0--r42hdfd78af_0"
 - "1.78.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-geneplotter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-geneplotter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-geneplotter", "latest": {"1.78.0--r43hdfd78af_0": "sha256:a70d83ca7e76d96a9c0631edab7fb16b3bccaed3add2ca3d93071316ba78a30b"}, "tags": {"1.72.0--r41hdfd78af_0": "sha256:c8e2f7c835d703fd2acc94d3301eeb3054481bf2499ca27e7cf9ac03bb1fb4c1", "1.76.0--r42hdfd78af_0": "sha256:046ff86ff260f35aca16ef4a8bfbd9df936459cb6863e0784df5821550682a80", "1.78.0--r43hdfd78af_0": "sha256:a70d83ca7e76d96a9c0631edab7fb16b3bccaed3add2ca3d93071316ba78a30b"}, "docker": "quay.io/biocontainers/bioconductor-geneplotter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-geneplotter.
shpc-registry automated BioContainers addition for bioconductor-geneplotter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-geneplotter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-geneplotter:1.78.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-geneplotter/1.78.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-geneplotter/1.78.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-geneplotter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneplotter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-geneplotter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-geneplotter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-geneplotter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-geneplotter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-geneplotter

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