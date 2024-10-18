---
layout: container
name:  "quay.io/biocontainers/bioconductor-affyilm"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-affyilm/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-affyilm/container.yaml"
updated_at: "2024-10-18 03:15:37.228628"
latest: "1.54.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-affyilm"

versions:
 - "1.46.0--r41hdfd78af_0"
 - "1.50.0--r42hdfd78af_0"
 - "1.52.0--r43hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-affyilm"
config: {"url": "https://biocontainers.pro/tools/bioconductor-affyilm", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-affyilm", "latest": {"1.54.0--r43hdfd78af_0": "sha256:40de7d740000eb7656ccdad4f994c6d6abbce7ac202026e8f8b9649f56c88b9a"}, "tags": {"1.46.0--r41hdfd78af_0": "sha256:2a93502d5faebb970937f070a516b9960787eb36d166c9a1830dd7fa5da68a93", "1.50.0--r42hdfd78af_0": "sha256:b39affbdf2ae528d7968ff2f69fc3d8aaa4c7076c59df7d4e5dc396f1c23d363", "1.52.0--r43hdfd78af_0": "sha256:a3d6de67b27f23079011dac3bb36753a12ee0fd51afdf1bc56ad162f1edc84af", "1.54.0--r43hdfd78af_0": "sha256:40de7d740000eb7656ccdad4f994c6d6abbce7ac202026e8f8b9649f56c88b9a"}, "docker": "quay.io/biocontainers/bioconductor-affyilm"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-affyilm.
shpc-registry automated BioContainers addition for bioconductor-affyilm
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-affyilm
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-affyilm:1.54.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-affyilm/1.54.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-affyilm/1.54.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-affyilm-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyilm-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-affyilm-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-affyilm-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-affyilm-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-affyilm-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-affyilm

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