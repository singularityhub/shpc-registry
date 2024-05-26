---
layout: container
name:  "quay.io/biocontainers/bioconda2biocontainer"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconda2biocontainer/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconda2biocontainer/container.yaml"
updated_at: "2024-05-26 03:03:32.081407"
latest: "0.0.7--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconda2biocontainer"
aliases:
 - "bioconda2biocontainer"
 - "bioconda2cwldocker"
 - "biocontainers-search"
 - "normalizer"
 - "2to3-3.10"
 - "idle3.10"
 - "pydoc3.10"
 - "python3.1"
 - "python3.10"
 - "python3.10-config"
versions:
 - "0.0.7--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconda2biocontainer"
config: {"url": "https://biocontainers.pro/tools/bioconda2biocontainer", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconda2biocontainer", "latest": {"0.0.7--pyhdfd78af_0": "sha256:79d233da5e6b4b84755914f1a5c603c286acf2091c40b931cf8f13129ec06761"}, "tags": {"0.0.7--pyhdfd78af_0": "sha256:79d233da5e6b4b84755914f1a5c603c286acf2091c40b931cf8f13129ec06761"}, "docker": "quay.io/biocontainers/bioconda2biocontainer", "aliases": {"bioconda2biocontainer": "/usr/local/bin/bioconda2biocontainer", "bioconda2cwldocker": "/usr/local/bin/bioconda2cwldocker", "biocontainers-search": "/usr/local/bin/biocontainers-search", "normalizer": "/usr/local/bin/normalizer", "2to3-3.10": "/usr/local/bin/2to3-3.10", "idle3.10": "/usr/local/bin/idle3.10", "pydoc3.10": "/usr/local/bin/pydoc3.10", "python3.1": "/usr/local/bin/python3.1", "python3.10": "/usr/local/bin/python3.10", "python3.10-config": "/usr/local/bin/python3.10-config"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconda2biocontainer.
shpc-registry automated BioContainers addition for bioconda2biocontainer
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconda2biocontainer
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconda2biocontainer:0.0.7--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconda2biocontainer/0.0.7--pyhdfd78af_0
$ module help quay.io/biocontainers/bioconda2biocontainer/0.0.7--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconda2biocontainer-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconda2biocontainer-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconda2biocontainer-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconda2biocontainer-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconda2biocontainer-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconda2biocontainer-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bioconda2biocontainer

```bash
$ singularity exec <container> /usr/local/bin/bioconda2biocontainer
$ podman run --it --rm --entrypoint /usr/local/bin/bioconda2biocontainer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconda2biocontainer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bioconda2cwldocker

```bash
$ singularity exec <container> /usr/local/bin/bioconda2cwldocker
$ podman run --it --rm --entrypoint /usr/local/bin/bioconda2cwldocker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bioconda2cwldocker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### biocontainers-search

```bash
$ singularity exec <container> /usr/local/bin/biocontainers-search
$ podman run --it --rm --entrypoint /usr/local/bin/biocontainers-search   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/biocontainers-search   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.10

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.10
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.10

```bash
$ singularity exec <container> /usr/local/bin/idle3.10
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.10

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.10
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.1

```bash
$ singularity exec <container> /usr/local/bin/python3.1
$ podman run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10

```bash
$ singularity exec <container> /usr/local/bin/python3.10
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### python3.10-config

```bash
$ singularity exec <container> /usr/local/bin/python3.10-config
$ podman run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/python3.10-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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