---
layout: container
name:  "quay.io/biocontainers/bioconductor-rgu34ccdf"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-rgu34ccdf/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-rgu34ccdf/container.yaml"
updated_at: "2024-04-10 02:56:53.283207"
latest: "2.18.0--r43hdfd78af_12"
container_url: "https://biocontainers.pro/tools/bioconductor-rgu34ccdf"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
description: "shpc-registry automated BioContainers addition for bioconductor-rgu34ccdf"
config: {"url": "https://biocontainers.pro/tools/bioconductor-rgu34ccdf", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-rgu34ccdf", "latest": {"2.18.0--r43hdfd78af_12": "sha256:7f0d228abbcda2f1daad87030ed5bcb4514ae9f62e07fb527572b1945755cd31"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:057000053ca6fab9a98c18b33d592022baf34bef1151275a47a3e2391b6c07a7", "2.18.0--r42hdfd78af_10": "sha256:5103b66c8d9260e1d9e607dc4d70e459b8faf6467aff9a5954ef6f5555e50d1c", "2.18.0--r43hdfd78af_11": "sha256:63f1776ab8ce53938485545e4183f8b684b6476eb065b756ce19a8d765bad071", "2.18.0--r43hdfd78af_12": "sha256:7f0d228abbcda2f1daad87030ed5bcb4514ae9f62e07fb527572b1945755cd31"}, "docker": "quay.io/biocontainers/bioconductor-rgu34ccdf"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-rgu34ccdf.
shpc-registry automated BioContainers addition for bioconductor-rgu34ccdf
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34ccdf
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-rgu34ccdf:2.18.0--r43hdfd78af_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-rgu34ccdf/2.18.0--r43hdfd78af_12
$ module help quay.io/biocontainers/bioconductor-rgu34ccdf/2.18.0--r43hdfd78af_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-rgu34ccdf-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34ccdf-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-rgu34ccdf-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-rgu34ccdf-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-rgu34ccdf-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-rgu34ccdf-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-rgu34ccdf

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