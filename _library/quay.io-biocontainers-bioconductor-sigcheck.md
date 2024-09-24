---
layout: container
name:  "quay.io/biocontainers/bioconductor-sigcheck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-sigcheck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-sigcheck/container.yaml"
updated_at: "2024-09-24 03:35:50.023588"
latest: "2.34.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-sigcheck"

versions:
 - "2.26.0--r41hdfd78af_0"
 - "2.30.0--r42hdfd78af_0"
 - "2.32.0--r43hdfd78af_0"
 - "2.34.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-sigcheck"
config: {"url": "https://biocontainers.pro/tools/bioconductor-sigcheck", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-sigcheck", "latest": {"2.34.0--r43hdfd78af_0": "sha256:869632e3431163d3ff7110c7fb3404567f2949bab0e6c51a32ad29b40ca73f47"}, "tags": {"2.26.0--r41hdfd78af_0": "sha256:3f87c9c98e5151a4d057496590f447788f269789dacabbc5be866c4d1bde1fba", "2.30.0--r42hdfd78af_0": "sha256:0fd29cffa5a00420495831c7200fdde0ea6392011dd6606c9d7f45913110794a", "2.32.0--r43hdfd78af_0": "sha256:53eb1ebe221d3ed2ded36209f6bb1ae96544f8949dd90e829be2e8d5a321b9d3", "2.34.0--r43hdfd78af_0": "sha256:869632e3431163d3ff7110c7fb3404567f2949bab0e6c51a32ad29b40ca73f47"}, "docker": "quay.io/biocontainers/bioconductor-sigcheck"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-sigcheck.
shpc-registry automated BioContainers addition for bioconductor-sigcheck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-sigcheck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-sigcheck:2.34.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-sigcheck/2.34.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-sigcheck/2.34.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-sigcheck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigcheck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-sigcheck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-sigcheck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-sigcheck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-sigcheck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-sigcheck

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