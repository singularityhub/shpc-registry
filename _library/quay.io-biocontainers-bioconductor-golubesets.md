---
layout: container
name:  "quay.io/biocontainers/bioconductor-golubesets"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-golubesets/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-golubesets/container.yaml"
updated_at: "2025-01-22 03:03:48.237410"
latest: "1.48.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-golubesets"

versions:
 - "1.36.0--r41hdfd78af_1"
 - "1.40.0--r42hdfd78af_0"
 - "1.42.0--r43hdfd78af_0"
 - "1.44.0--r43hdfd78af_0"
 - "1.48.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-golubesets"
config: {"url": "https://biocontainers.pro/tools/bioconductor-golubesets", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-golubesets", "latest": {"1.48.0--r44hdfd78af_0": "sha256:8d6d09e54cabeaa9e67b99fc2f7d5ef632ef4cf2391e2b8e7532f6277de0bc41"}, "tags": {"1.36.0--r41hdfd78af_1": "sha256:52f1d40300d436c9a97a41f0b0ab804f262d75053bdd663ee52c4613c81ab12e", "1.40.0--r42hdfd78af_0": "sha256:b2212201e9de85c861644709894fbf26ad8ed385e7a8330aee8d9c3c10e97d7d", "1.42.0--r43hdfd78af_0": "sha256:5416ceb6b8b14ad2fdc8e4678574a12b97f820bd79412059966d090bae548343", "1.44.0--r43hdfd78af_0": "sha256:1d056ac1c6fa500a8ea5c398bc85da9946b2abaf062a013aef9b2b23f673fbb7", "1.48.0--r44hdfd78af_0": "sha256:8d6d09e54cabeaa9e67b99fc2f7d5ef632ef4cf2391e2b8e7532f6277de0bc41"}, "docker": "quay.io/biocontainers/bioconductor-golubesets"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-golubesets.
shpc-registry automated BioContainers addition for bioconductor-golubesets
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-golubesets
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-golubesets:1.48.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-golubesets/1.48.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-golubesets/1.48.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-golubesets-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-golubesets-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-golubesets-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-golubesets-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-golubesets-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-golubesets-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-golubesets

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