---
layout: container
name:  "quay.io/biocontainers/bioconductor-basicstarrseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-basicstarrseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-basicstarrseq/container.yaml"
updated_at: "2024-12-02 03:43:46.961900"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-basicstarrseq"

versions:
 - "1.22.0--r41hdfd78af_0"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-basicstarrseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-basicstarrseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-basicstarrseq", "latest": {"1.30.0--r43hdfd78af_0": "sha256:cdbbcb8f1eb0ef7c1ed3057436d7deba00565cb2c275a06b9fa75d630dc31f2d"}, "tags": {"1.22.0--r41hdfd78af_0": "sha256:bbffd28ef7b5f697c8f11c91c65b5e14d96af56263c95f7d8054fd573e3edb74", "1.26.0--r42hdfd78af_0": "sha256:ef4cefcf6aeac4661974edaa40801ffb87defbdc7711ef4c11f985f66f881ff2", "1.28.0--r43hdfd78af_0": "sha256:ffc76d0a3142c2bd1c2d344ba26e5ebbd122c3fff74b0534cae400954388ccdd", "1.30.0--r43hdfd78af_0": "sha256:cdbbcb8f1eb0ef7c1ed3057436d7deba00565cb2c275a06b9fa75d630dc31f2d"}, "docker": "quay.io/biocontainers/bioconductor-basicstarrseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-basicstarrseq.
shpc-registry automated BioContainers addition for bioconductor-basicstarrseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-basicstarrseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-basicstarrseq:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-basicstarrseq/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-basicstarrseq/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-basicstarrseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basicstarrseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-basicstarrseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-basicstarrseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-basicstarrseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-basicstarrseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-basicstarrseq

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