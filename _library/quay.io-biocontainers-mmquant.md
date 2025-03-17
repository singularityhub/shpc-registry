---
layout: container
name:  "quay.io/biocontainers/mmquant"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/mmquant/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/mmquant/container.yaml"
updated_at: "2025-03-17 03:24:21.046436"
latest: "1.0.9--h077b44d_1"
container_url: "https://biocontainers.pro/tools/mmquant"
aliases:
 - "mmquant"
versions:
 - "1.0.4--hd03093a_1"
 - "1.0.5--hd03093a_0"
 - "1.0.5--hdcf5f25_2"
 - "1.0.7--hdcf5f25_0"
 - "1.0.9--hdcf5f25_0"
 - "1.0.9--h077b44d_1"
description: "shpc-registry automated BioContainers addition for mmquant"
config: {"url": "https://biocontainers.pro/tools/mmquant", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for mmquant", "latest": {"1.0.9--h077b44d_1": "sha256:74c58e283e03238ead36aea13e97567d41f5a3593b725c3d909a7afa62427202"}, "tags": {"1.0.4--hd03093a_1": "sha256:cc14611f926d053a17e8972998398bc3ed6a7db754dc40f3a7cc61e39db178e9", "1.0.5--hd03093a_0": "sha256:7f919367b43e508f76d787d53b9293c952fa4da516abde062e574d3b7feb1bfc", "1.0.5--hdcf5f25_2": "sha256:c9ed826c9aba11e00981cba166a7fafbe75ab136b2b3d0d09a715946dea125e4", "1.0.7--hdcf5f25_0": "sha256:f49b1a0dc372be461e1aff9598b598e5b61a6dc271682ef39c9dd5e2e603ed5c", "1.0.9--hdcf5f25_0": "sha256:27d79e260714791678f745a9445263bd38f02ab8f7f3b9b67d4627e8166e9f63", "1.0.9--h077b44d_1": "sha256:74c58e283e03238ead36aea13e97567d41f5a3593b725c3d909a7afa62427202"}, "docker": "quay.io/biocontainers/mmquant", "aliases": {"mmquant": "/usr/local/bin/mmquant"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/mmquant.
shpc-registry automated BioContainers addition for mmquant
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/mmquant
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/mmquant:1.0.9--h077b44d_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/mmquant/1.0.9--h077b44d_1
$ module help quay.io/biocontainers/mmquant/1.0.9--h077b44d_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### mmquant-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### mmquant-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### mmquant-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### mmquant-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### mmquant-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### mmquant-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mmquant

```bash
$ singularity exec <container> /usr/local/bin/mmquant
$ podman run --it --rm --entrypoint /usr/local/bin/mmquant   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mmquant   -v ${PWD} -w ${PWD} <container> -c " $@"
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