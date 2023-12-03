---
layout: container
name:  "quay.io/biocontainers/bioconductor-scthi.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-scthi.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-scthi.data/container.yaml"
updated_at: "2023-12-03 02:57:16.426309"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-scthi.data"

versions:
 - "1.6.0--r41hdfd78af_1"
 - "1.9.0--r42hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-scthi.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-scthi.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-scthi.data", "latest": {"1.12.0--r43hdfd78af_0": "sha256:7eaefd34601daeddee63edbe7fd55593487abd0e9d73e22b994c8dd901882ee6"}, "tags": {"1.6.0--r41hdfd78af_1": "sha256:28fe2920b3764df74caa1555ddd4ac2f7e30ce7107225aace3ffc96990d457b6", "1.9.0--r42hdfd78af_0": "sha256:b12e69292590b3f16329e5f57b34d8f1ce01eab56c297e1393411a365907910c", "1.12.0--r43hdfd78af_0": "sha256:7eaefd34601daeddee63edbe7fd55593487abd0e9d73e22b994c8dd901882ee6"}, "docker": "quay.io/biocontainers/bioconductor-scthi.data"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-scthi.data.
shpc-registry automated BioContainers addition for bioconductor-scthi.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-scthi.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-scthi.data:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-scthi.data/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-scthi.data/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-scthi.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scthi.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-scthi.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-scthi.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-scthi.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-scthi.data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-scthi.data

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