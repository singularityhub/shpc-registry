---
layout: container
name:  "quay.io/biocontainers/bioconductor-biocio"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-biocio/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-biocio/container.yaml"
updated_at: "2024-11-04 08:27:24.977855"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-biocio"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-biocio"
config: {"url": "https://biocontainers.pro/tools/bioconductor-biocio", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-biocio", "latest": {"1.12.0--r43hdfd78af_0": "sha256:f3541b347d644e751e380785cc88661b4035c9e0447b9dd7d85cdd0148d70175"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:036aeb173dcc1a87eb3504a46c75f2d07d04d04d47755a74cbf215b294766084", "1.8.0--r42hdfd78af_0": "sha256:110cb7a241fb70369f706ffa8eaee33064c039c85e42b7ae2d7e5f7af4afb466", "1.10.0--r43hdfd78af_0": "sha256:64f802c45105e60b7dba422802dd220ec0ee4f28ed92e70d35046cea04ea33b6", "1.12.0--r43hdfd78af_0": "sha256:f3541b347d644e751e380785cc88661b4035c9e0447b9dd7d85cdd0148d70175"}, "docker": "quay.io/biocontainers/bioconductor-biocio"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-biocio.
shpc-registry automated BioContainers addition for bioconductor-biocio
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-biocio
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-biocio:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-biocio/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-biocio/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-biocio-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocio-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-biocio-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-biocio-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-biocio-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-biocio-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-biocio

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