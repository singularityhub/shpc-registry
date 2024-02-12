---
layout: container
name:  "quay.io/biocontainers/bioconductor-spia"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-spia/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-spia/container.yaml"
updated_at: "2024-02-12 03:23:21.587457"
latest: "2.54.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-spia"

versions:
 - "2.46.0--r41hdfd78af_0"
 - "2.50.0--r42hdfd78af_0"
 - "2.52.0--r43hdfd78af_0"
 - "2.54.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-spia"
config: {"url": "https://biocontainers.pro/tools/bioconductor-spia", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-spia", "latest": {"2.54.0--r43hdfd78af_0": "sha256:4fa6d67047f3cea5b38981145a5c704c627c17b12e1253aeea342d4b4e583e93"}, "tags": {"2.46.0--r41hdfd78af_0": "sha256:6d02a3b3c635d28d5e0efb1e14bec2a2dfea8453876fa0b893a4db2ba0125d23", "2.50.0--r42hdfd78af_0": "sha256:75c7d27810b56e15dd69cbc5575edb011fc062fe56cd335d2745f8d828ec4553", "2.52.0--r43hdfd78af_0": "sha256:7f72e40a39080c6aa743e5218452627aabb1540959c9db683c6e4da82a61b03d", "2.54.0--r43hdfd78af_0": "sha256:4fa6d67047f3cea5b38981145a5c704c627c17b12e1253aeea342d4b4e583e93"}, "docker": "quay.io/biocontainers/bioconductor-spia"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-spia.
shpc-registry automated BioContainers addition for bioconductor-spia
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-spia
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-spia:2.54.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-spia/2.54.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-spia/2.54.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-spia-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spia-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-spia-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-spia-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-spia-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-spia-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-spia

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