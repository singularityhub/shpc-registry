---
layout: container
name:  "quay.io/biocontainers/bioconductor-goseq"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-goseq/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-goseq/container.yaml"
updated_at: "2024-04-12 02:29:33.137019"
latest: "1.54.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-goseq"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-goseq"
config: {"url": "https://biocontainers.pro/tools/bioconductor-goseq", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-goseq", "latest": {"1.54.0--r43hdfd78af_0": "sha256:67392e48905efac0229f7d7f74c71186afa7f4cbf8d405cc5f4d268a1017011e"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:f1f54c1bd5a761f13d46aae19d38a76388cc0b293ef1748501f9d23e4baaf039", "1.50.0--r42hdfd78af_0": "sha256:77255f5d043de5c6838978be2803fe86a350598172ee79b220337e3de2ea4b68", "1.52.0--r43hdfd78af_0": "sha256:fccadbe8aa6878d9f9ee45b872343e578f386ccccb8668886a9eec3404cddd2a", "1.54.0--r43hdfd78af_0": "sha256:67392e48905efac0229f7d7f74c71186afa7f4cbf8d405cc5f4d268a1017011e"}, "docker": "quay.io/biocontainers/bioconductor-goseq"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-goseq.
shpc-registry automated BioContainers addition for bioconductor-goseq
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-goseq
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-goseq:1.54.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-goseq/1.54.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-goseq/1.54.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-goseq-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-goseq-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-goseq-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-goseq-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-goseq-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-goseq-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-goseq

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