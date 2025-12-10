---
layout: container
name:  "quay.io/biocontainers/bioconductor-omnipathr"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-omnipathr/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-omnipathr/container.yaml"
updated_at: "2025-12-10 03:31:57.300269"
latest: "3.10.1--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-omnipathr"

versions:
 - "3.2.0--r41hdfd78af_0"
 - "3.5.25--r42hdfd78af_0"
 - "3.8.0--r43hdfd78af_0"
 - "3.10.1--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-omnipathr"
config: {"url": "https://biocontainers.pro/tools/bioconductor-omnipathr", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-omnipathr", "latest": {"3.10.1--r43hdfd78af_0": "sha256:b6d9a518f30c69ff9b8020905209faec50babbc5f7931f211ec5233fd5927178"}, "tags": {"3.2.0--r41hdfd78af_0": "sha256:d86bb0da85b36c95bd578d8e83a9247cdfa4b6929054a6be7d6cbb2653abb153", "3.5.25--r42hdfd78af_0": "sha256:acf94b92149e80267d21c5614aaee47cbb976ab73db083b99af85303ad28609a", "3.8.0--r43hdfd78af_0": "sha256:35f1cad9e2a7df0f0f7975adce14a158e77d47d8731877d659fb62a5c609560c", "3.10.1--r43hdfd78af_0": "sha256:b6d9a518f30c69ff9b8020905209faec50babbc5f7931f211ec5233fd5927178"}, "docker": "quay.io/biocontainers/bioconductor-omnipathr"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-omnipathr.
shpc-registry automated BioContainers addition for bioconductor-omnipathr
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-omnipathr
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-omnipathr:3.10.1--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-omnipathr/3.10.1--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-omnipathr/3.10.1--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-omnipathr-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omnipathr-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-omnipathr-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-omnipathr-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-omnipathr-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-omnipathr-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-omnipathr

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