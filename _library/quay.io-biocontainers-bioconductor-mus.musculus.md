---
layout: container
name:  "quay.io/biocontainers/bioconductor-mus.musculus"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mus.musculus/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mus.musculus/container.yaml"
updated_at: "2024-05-23 02:49:37.842343"
latest: "1.3.1--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-mus.musculus"

versions:
 - "1.3.1--r41hdfd78af_9"
 - "1.3.1--r42hdfd78af_10"
 - "1.3.1--r43hdfd78af_11"
 - "1.3.1--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-mus.musculus"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mus.musculus", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mus.musculus", "latest": {"1.3.1--r43hdfd78af_12": "sha256:b182707f1ac16e3af02bf67159b5ce54576b9fe835f8d90774753388700eb763"}, "tags": {"1.3.1--r41hdfd78af_9": "sha256:e0249d69a5a33b443c420ed22722a1552079a369b437e682a5ccbcad4ef962c9", "1.3.1--r42hdfd78af_10": "sha256:b3048f1a2733131295ad91ddca9453b3bec541c2769dbae5c5e264f93bd35f3f", "1.3.1--r43hdfd78af_11": "sha256:9f794295adb66435a639ab04814d27b133a6c7e5c1c50f0911e8f74006ccce60", "1.3.1--r43hdfd78af_12": "sha256:b182707f1ac16e3af02bf67159b5ce54576b9fe835f8d90774753388700eb763"}, "docker": "quay.io/biocontainers/bioconductor-mus.musculus"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mus.musculus.
shpc-registry automated BioContainers addition for bioconductor-mus.musculus
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mus.musculus
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mus.musculus:1.3.1--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mus.musculus/1.3.1--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-mus.musculus/1.3.1--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mus.musculus-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mus.musculus-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mus.musculus-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mus.musculus-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mus.musculus-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mus.musculus-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mus.musculus

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