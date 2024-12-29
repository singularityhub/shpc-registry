---
layout: container
name:  "quay.io/biocontainers/bioconductor-unifiedwmwqpcr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-unifiedwmwqpcr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-unifiedwmwqpcr/container.yaml"
updated_at: "2024-12-29 03:16:25.708989"
latest: "1.38.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-unifiedwmwqpcr"

versions:
 - "1.30.0--r41hdfd78af_0"
 - "1.34.0--r42hdfd78af_0"
 - "1.36.0--r43hdfd78af_0"
 - "1.38.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-unifiedwmwqpcr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-unifiedwmwqpcr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-unifiedwmwqpcr", "latest": {"1.38.0--r43hdfd78af_0": "sha256:860098d2455624fbea9eaf2fb8371c7124eec6f2f8386f72a8d651be23a9e8f7"}, "tags": {"1.30.0--r41hdfd78af_0": "sha256:9983f323c8d12182fa5851f700034dc6831e8484b8c8008c078099e0113cf007", "1.34.0--r42hdfd78af_0": "sha256:4acde4ae0c75135478f807242abcf6efecfdfb8a90439eb3d5deb4cccecde723", "1.36.0--r43hdfd78af_0": "sha256:f98b51d3069f3c81ff0ccc6ff0b3a66a6bf4d03724df9a8098d9d881f5507d43", "1.38.0--r43hdfd78af_0": "sha256:860098d2455624fbea9eaf2fb8371c7124eec6f2f8386f72a8d651be23a9e8f7"}, "docker": "quay.io/biocontainers/bioconductor-unifiedwmwqpcr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-unifiedwmwqpcr.
shpc-registry automated BioContainers addition for bioconductor-unifiedwmwqpcr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-unifiedwmwqpcr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-unifiedwmwqpcr:1.38.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-unifiedwmwqpcr/1.38.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-unifiedwmwqpcr/1.38.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-unifiedwmwqpcr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-unifiedwmwqpcr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-unifiedwmwqpcr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-unifiedwmwqpcr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-unifiedwmwqpcr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-unifiedwmwqpcr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-unifiedwmwqpcr

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