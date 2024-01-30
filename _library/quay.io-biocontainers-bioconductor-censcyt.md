---
layout: container
name:  "quay.io/biocontainers/bioconductor-censcyt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-censcyt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-censcyt/container.yaml"
updated_at: "2024-01-30 02:31:39.118148"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-censcyt"

versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-censcyt"
config: {"url": "https://biocontainers.pro/tools/bioconductor-censcyt", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-censcyt", "latest": {"1.10.0--r43hdfd78af_0": "sha256:4921d3cb271a8b31b770c38a35e06425fcd47c7aa0b3962ee98725ae745451eb"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:f9e75f93c6afd03e805879ecb3442fc452f4febff62678e4cb60e8cf14ceb8f8", "1.6.0--r42hdfd78af_0": "sha256:e52ff4987e35fadab5029bf412763738afb157ee3ba34bb2f0277610f7a5def8", "1.8.0--r43hdfd78af_0": "sha256:622a3f88a06af8a9a55e6b388d5bb199f6ea0b9cc28fee4cec74aa92afeff791", "1.10.0--r43hdfd78af_0": "sha256:4921d3cb271a8b31b770c38a35e06425fcd47c7aa0b3962ee98725ae745451eb"}, "docker": "quay.io/biocontainers/bioconductor-censcyt"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-censcyt.
shpc-registry automated BioContainers addition for bioconductor-censcyt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-censcyt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-censcyt:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-censcyt/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-censcyt/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-censcyt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-censcyt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-censcyt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-censcyt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-censcyt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-censcyt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-censcyt

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