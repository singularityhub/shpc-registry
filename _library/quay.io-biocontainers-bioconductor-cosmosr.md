---
layout: container
name:  "quay.io/biocontainers/bioconductor-cosmosr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-cosmosr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-cosmosr/container.yaml"
updated_at: "2025-09-28 03:40:26.038518"
latest: "1.14.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-cosmosr"
aliases:
 - "pandoc"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.14.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-cosmosr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-cosmosr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-cosmosr", "latest": {"1.14.0--r44hdfd78af_0": "sha256:1a80b1789dbfced6fc83e8f9cee7a82aea0e47231fb3f28323b443528bdc898e"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:0818dde3e37d6f3041ec115d6951fe266c1d7dc0515bdea4ba8e40f65ecd71b0", "1.6.0--r42hdfd78af_0": "sha256:0a3e128e97d73aaae0650b03f891c459f6044998151c1342a5b93bf7f252d894", "1.8.0--r43hdfd78af_0": "sha256:d11883ed4433b28863e6848c12bbd24a1831878785ce5522169d1e9b60db20c9", "1.10.0--r43hdfd78af_0": "sha256:5908457f2cbd254b0079eca4b6de7d063af1faad60624c1d6a202089e0ade895", "1.14.0--r44hdfd78af_0": "sha256:1a80b1789dbfced6fc83e8f9cee7a82aea0e47231fb3f28323b443528bdc898e"}, "docker": "quay.io/biocontainers/bioconductor-cosmosr", "aliases": {"pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-cosmosr.
shpc-registry automated BioContainers addition for bioconductor-cosmosr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-cosmosr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-cosmosr:1.14.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-cosmosr/1.14.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-cosmosr/1.14.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-cosmosr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cosmosr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-cosmosr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-cosmosr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-cosmosr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-cosmosr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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