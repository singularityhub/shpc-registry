---
layout: container
name:  "quay.io/biocontainers/bioconductor-snifter"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-snifter/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-snifter/container.yaml"
updated_at: "2025-11-15 03:10:59.278385"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-snifter"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-snifter"
config: {"url": "https://biocontainers.pro/tools/bioconductor-snifter", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-snifter", "latest": {"1.12.0--r43hdfd78af_0": "sha256:8f50ae895b76072a1a00579d5a5dadb538d6f3f29c27d3d8cf004393fa80e261"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:4caf94880f22e81b46a99d7db22a3473bdd778568ddc0b38fb64029dce1689e8", "1.8.0--r42hdfd78af_0": "sha256:35e77a6631b77a53d68f967b944d4d4e685407effac583a248c0a35d26b20609", "1.10.0--r43hdfd78af_0": "sha256:9d1112793957a58bf30325238dbfc172c7e9c4accf25d6b9eae0c214001c3408", "1.12.0--r43hdfd78af_0": "sha256:8f50ae895b76072a1a00579d5a5dadb538d6f3f29c27d3d8cf004393fa80e261"}, "docker": "quay.io/biocontainers/bioconductor-snifter"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-snifter.
shpc-registry automated BioContainers addition for bioconductor-snifter
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-snifter
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-snifter:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-snifter/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-snifter/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-snifter-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snifter-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-snifter-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-snifter-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-snifter-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-snifter-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-snifter

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