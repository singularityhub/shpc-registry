---
layout: container
name:  "quay.io/biocontainers/r-autospill"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-autospill/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-autospill/container.yaml"
updated_at: "2025-03-27 03:11:42.371010"
latest: "0.2.0--r44hdfd78af_3"
container_url: "https://biocontainers.pro/tools/r-autospill"
aliases:
 - "x86_64-conda-linux-gnu-gfortran.bin"
versions:
 - "0.2.0--r41hdfd78af_0"
 - "0.2.0--r42hdfd78af_1"
 - "0.2.0--r43hdfd78af_2"
 - "0.2.0--r44hdfd78af_3"
description: "shpc-registry automated BioContainers addition for r-autospill"
config: {"url": "https://biocontainers.pro/tools/r-autospill", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-autospill", "latest": {"0.2.0--r44hdfd78af_3": "sha256:28c76cd3f36024b2f1f72773f218ba58c37de5d9a78e54de2ab76ad0acd739b0"}, "tags": {"0.2.0--r41hdfd78af_0": "sha256:c2736578197852807861673c5de59896b2144e8b10f6ef12e0e576e9ea371a3c", "0.2.0--r42hdfd78af_1": "sha256:58ceb51d9990c43a9e7bda7ce2002df11a233f34f85f892535942c07d0ebaffd", "0.2.0--r43hdfd78af_2": "sha256:ac3d90f7b89a844b072056596a0d8cee331a96eebd6d56fb579da4132aefd0d4", "0.2.0--r44hdfd78af_3": "sha256:28c76cd3f36024b2f1f72773f218ba58c37de5d9a78e54de2ab76ad0acd739b0"}, "docker": "quay.io/biocontainers/r-autospill", "aliases": {"x86_64-conda-linux-gnu-gfortran.bin": "/usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-autospill.
shpc-registry automated BioContainers addition for r-autospill
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-autospill
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-autospill:0.2.0--r44hdfd78af_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-autospill/0.2.0--r44hdfd78af_3
$ module help quay.io/biocontainers/r-autospill/0.2.0--r44hdfd78af_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-autospill-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-autospill-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-autospill-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-autospill-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-autospill-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-autospill-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### x86_64-conda-linux-gnu-gfortran.bin

```bash
$ singularity exec <container> /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin
$ podman run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x86_64-conda-linux-gnu-gfortran.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
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