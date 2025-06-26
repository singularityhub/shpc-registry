---
layout: container
name:  "quay.io/biocontainers/bioconductor-dart"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-dart/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-dart/container.yaml"
updated_at: "2025-06-26 04:33:37.492204"
latest: "1.54.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-dart"

versions:
 - "1.42.0--r41hdfd78af_0"
 - "1.46.0--r42hdfd78af_0"
 - "1.48.0--r43hdfd78af_0"
 - "1.50.0--r43hdfd78af_0"
 - "1.54.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-dart"
config: {"url": "https://biocontainers.pro/tools/bioconductor-dart", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-dart", "latest": {"1.54.0--r44hdfd78af_0": "sha256:c11a3b5054bb74d6936beb0a9b6ccdba3078a4d4fd01d5c380ca83f630c7e858"}, "tags": {"1.42.0--r41hdfd78af_0": "sha256:ba1c94d776946dc27fb1fca85ff57779c380f8bdd762883ca6b4060874e395a3", "1.46.0--r42hdfd78af_0": "sha256:ee3c56eb7415c4455d64fc9805cd36d13e6f235aa1b233ac829162ff3ab2e474", "1.48.0--r43hdfd78af_0": "sha256:4a71efd8c443e158e72a210207290c27a569c8cba41a628679263a200ee0be1a", "1.50.0--r43hdfd78af_0": "sha256:5f282e6cf8045c1fa7a1d10b49bd22a794c57f5f1927c17a0b426d80a85a2c2c", "1.54.0--r44hdfd78af_0": "sha256:c11a3b5054bb74d6936beb0a9b6ccdba3078a4d4fd01d5c380ca83f630c7e858"}, "docker": "quay.io/biocontainers/bioconductor-dart"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-dart.
shpc-registry automated BioContainers addition for bioconductor-dart
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-dart
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-dart:1.54.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-dart/1.54.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-dart/1.54.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-dart-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dart-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-dart-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-dart-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-dart-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-dart-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-dart

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