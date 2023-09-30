---
layout: container
name:  "quay.io/biocontainers/bioconductor-annotationtools"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-annotationtools/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-annotationtools/container.yaml"
updated_at: "2023-09-30 02:41:22.416431"
latest: "1.74.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-annotationtools"

versions:
 - "1.68.0--r41hdfd78af_0"
 - "1.72.0--r42hdfd78af_0"
 - "1.74.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-annotationtools"
config: {"url": "https://biocontainers.pro/tools/bioconductor-annotationtools", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-annotationtools", "latest": {"1.74.0--r43hdfd78af_0": "sha256:d38af474ce98b392b6baf0944476d4baff9758a6a4246c970f57008b8e291cf7"}, "tags": {"1.68.0--r41hdfd78af_0": "sha256:2fcb54be94ffd3f08b8f5eca127f6522b39c145fb581b6f355676fd34b47d20c", "1.72.0--r42hdfd78af_0": "sha256:e2f67d06ee7fe47db2063276a9c1674911acd2c316ea7c5c898d387354931e14", "1.74.0--r43hdfd78af_0": "sha256:d38af474ce98b392b6baf0944476d4baff9758a6a4246c970f57008b8e291cf7"}, "docker": "quay.io/biocontainers/bioconductor-annotationtools"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-annotationtools.
shpc-registry automated BioContainers addition for bioconductor-annotationtools
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationtools
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-annotationtools:1.74.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-annotationtools/1.74.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-annotationtools/1.74.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-annotationtools-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationtools-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-annotationtools-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-annotationtools-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-annotationtools-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-annotationtools-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-annotationtools

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