---
layout: container
name:  "quay.io/biocontainers/miniprot"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/miniprot/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/miniprot/container.yaml"
updated_at: "2023-02-15 03:21:01.600806"
latest: "0.7--h7132678_0"
container_url: "https://biocontainers.pro/tools/miniprot"
aliases:
 - "miniprot"
versions:
 - "0.4--h7132678_0"
 - "0.5--h7132678_0"
 - "0.7--h7132678_0"
 - "0.6--h7132678_0"
description: "shpc-registry automated BioContainers addition for miniprot"
config: {"url": "https://biocontainers.pro/tools/miniprot", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for miniprot", "latest": {"0.7--h7132678_0": "sha256:f6b9122f4bc36cabea25c5c81f17711d37b60b235a6c3e8e04e5979e51079c5e"}, "tags": {"0.4--h7132678_0": "sha256:f47e9f65bc7e6abcd7e1d73dc505a737bcac805514ab44f2d7aa1a97c7d95ebd", "0.5--h7132678_0": "sha256:f2470b9f18f7c6765547e4e1429f04166238454aa0625204ea73d217743e48d9", "0.7--h7132678_0": "sha256:f6b9122f4bc36cabea25c5c81f17711d37b60b235a6c3e8e04e5979e51079c5e", "0.6--h7132678_0": "sha256:81a3a45c40ccc3d8875d0f512654dc20b91aa9a6f2e8ec1962efdbc24a80226e"}, "docker": "quay.io/biocontainers/miniprot", "aliases": {"miniprot": "/usr/local/bin/miniprot"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/miniprot.
shpc-registry automated BioContainers addition for miniprot
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/miniprot
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/miniprot:0.7--h7132678_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/miniprot/0.7--h7132678_0
$ module help quay.io/biocontainers/miniprot/0.7--h7132678_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### miniprot-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### miniprot-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### miniprot-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### miniprot-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### miniprot-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### miniprot-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### miniprot

```bash
$ singularity exec <container> /usr/local/bin/miniprot
$ podman run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/miniprot   -v ${PWD} -w ${PWD} <container> -c " $@"
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