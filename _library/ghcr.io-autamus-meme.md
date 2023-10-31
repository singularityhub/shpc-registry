---
layout: container
name:  "ghcr.io/autamus/meme"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/meme/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/meme/container.yaml"
updated_at: "2023-10-31 02:23:58.735243"
latest: "5.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/meme"
aliases:
 - "meme"
 - "meme-chip"
 - "memhog"
versions:
 - "5.3.0"
 - "latest"
description: "The MEME suite provides online tools for discovering and using protein and DNA sequence motifs."
config: {"docker": "ghcr.io/autamus/meme", "url": "https://github.com/orgs/autamus/packages/container/package/meme", "maintainer": "@vsoch", "description": "The MEME suite provides online tools for discovering and using protein and DNA sequence motifs.", "latest": {"5.3.0": "sha256:65f28df418d7d71c1b10d27f9b8e339d3355edada976aaab2892777f4a69e1c7"}, "tags": {"5.3.0": "sha256:65f28df418d7d71c1b10d27f9b8e339d3355edada976aaab2892777f4a69e1c7", "latest": "sha256:65f28df418d7d71c1b10d27f9b8e339d3355edada976aaab2892777f4a69e1c7"}, "aliases": {"meme": "/opt/view/bin/meme", "meme-chip": "/opt/view/bin/meme-chip", "memhog": "/opt/view/bin/memhog"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/meme.
The MEME suite provides online tools for discovering and using protein and DNA sequence motifs.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/meme
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/meme:5.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/meme/5.3.0
$ module help ghcr.io/autamus/meme/5.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### meme-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### meme-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### meme-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### meme-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### meme-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### meme-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### meme

```bash
$ singularity exec <container> /opt/view/bin/meme
$ podman run --it --rm --entrypoint /opt/view/bin/meme   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/meme   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### meme-chip

```bash
$ singularity exec <container> /opt/view/bin/meme-chip
$ podman run --it --rm --entrypoint /opt/view/bin/meme-chip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/meme-chip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### memhog

```bash
$ singularity exec <container> /opt/view/bin/memhog
$ podman run --it --rm --entrypoint /opt/view/bin/memhog   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/memhog   -v ${PWD} -w ${PWD} <container> -c " $@"
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