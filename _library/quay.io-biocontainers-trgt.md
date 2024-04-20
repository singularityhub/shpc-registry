---
layout: container
name:  "quay.io/biocontainers/trgt"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/trgt/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/trgt/container.yaml"
updated_at: "2024-04-20 02:46:03.429706"
latest: "0.9.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/trgt"
aliases:
 - "trgt"
 - "trvz"
versions:
 - "0.3.4--hdfd78af_0"
 - "0.4.0--hdfd78af_0"
 - "0.5.0--hdfd78af_0"
 - "0.7.0--hdfd78af_0"
 - "0.8.0--hdfd78af_0"
 - "0.9.0--hdfd78af_0"
description: "singularity registry hpc automated addition for trgt"
config: {"url": "https://biocontainers.pro/tools/trgt", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for trgt", "latest": {"0.9.0--hdfd78af_0": "sha256:d64172ab796bac16e22e8e4527b0fdd304df3b7cc71356f8ad0a0dcabf3aa499"}, "tags": {"0.3.4--hdfd78af_0": "sha256:fd43ea17e09f402bb0ee677021fc860a9308c081ec998cecf9030541b06a4aa7", "0.4.0--hdfd78af_0": "sha256:337aff680c8552224faefaa2f5bcedb7f7ec94ae585e085fc8ae4538c56b114d", "0.5.0--hdfd78af_0": "sha256:033eddc9aead1e2971c0a202f50eb642f708212a635f086cdb3cb9dc63752da1", "0.7.0--hdfd78af_0": "sha256:8630b3706c6fe0b25e8d8782cd4d02c1950b394a3b2eea6dbe3c7f0bfca670e9", "0.8.0--hdfd78af_0": "sha256:16d9c13b9be273013e76790df0e8421499fdc331ecab667726de2bb3f39d1918", "0.9.0--hdfd78af_0": "sha256:d64172ab796bac16e22e8e4527b0fdd304df3b7cc71356f8ad0a0dcabf3aa499"}, "docker": "quay.io/biocontainers/trgt", "aliases": {"trgt": "/usr/local/bin/trgt", "trvz": "/usr/local/bin/trvz"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/trgt.
singularity registry hpc automated addition for trgt
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/trgt
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/trgt:0.9.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/trgt/0.9.0--hdfd78af_0
$ module help quay.io/biocontainers/trgt/0.9.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### trgt-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### trgt-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### trgt-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### trgt-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### trgt-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### trgt-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### trgt

```bash
$ singularity exec <container> /usr/local/bin/trgt
$ podman run --it --rm --entrypoint /usr/local/bin/trgt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trgt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trvz

```bash
$ singularity exec <container> /usr/local/bin/trvz
$ podman run --it --rm --entrypoint /usr/local/bin/trvz   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trvz   -v ${PWD} -w ${PWD} <container> -c " $@"
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