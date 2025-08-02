---
layout: container
name:  "quay.io/biocontainers/bioconductor-keggorthology"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-keggorthology/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-keggorthology/container.yaml"
updated_at: "2025-08-02 03:42:59.136395"
latest: "2.58.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-keggorthology"

versions:
 - "2.46.0--r41hdfd78af_0"
 - "2.50.0--r42hdfd78af_0"
 - "2.52.0--r43hdfd78af_0"
 - "2.54.0--r43hdfd78af_0"
 - "2.58.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-keggorthology"
config: {"url": "https://biocontainers.pro/tools/bioconductor-keggorthology", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-keggorthology", "latest": {"2.58.0--r44hdfd78af_0": "sha256:07f57cf022aa07dbeae3ad4a5a106dca136a0add63957630c526d7d74b5df2e7"}, "tags": {"2.46.0--r41hdfd78af_0": "sha256:b2e25a67727271337501c7e2317502ddedee477fea5d858a3ac800f4f5ff1cb3", "2.50.0--r42hdfd78af_0": "sha256:db5d891144d528b002b4d6d5434876f9a40cd124e8fc7c2cb0bb3716cadcc921", "2.52.0--r43hdfd78af_0": "sha256:11d2414d7817109ced9e8500f053ca7e7ab930ed90d2457bab9082d8df5506c8", "2.54.0--r43hdfd78af_0": "sha256:e11e52d9346ea713584d0eb329355120fade9eed9d384995d83a20cf2288add0", "2.58.0--r44hdfd78af_0": "sha256:07f57cf022aa07dbeae3ad4a5a106dca136a0add63957630c526d7d74b5df2e7"}, "docker": "quay.io/biocontainers/bioconductor-keggorthology"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-keggorthology.
shpc-registry automated BioContainers addition for bioconductor-keggorthology
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-keggorthology
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-keggorthology:2.58.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-keggorthology/2.58.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-keggorthology/2.58.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-keggorthology-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-keggorthology-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-keggorthology-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-keggorthology-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-keggorthology-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-keggorthology-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-keggorthology

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