---
layout: container
name:  "quay.io/biocontainers/gfa1"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfa1/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfa1/container.yaml"
updated_at: "2025-02-04 03:22:27.151939"
latest: "0.53.alpha--h577a1d6_3"
container_url: "https://biocontainers.pro/tools/gfa1"
aliases:
 - "falcon2gfa"
 - "fastg2gfa"
 - "gfaview"
 - "mag2gfa"
 - "supernova2gfa"
versions:
 - "0.53.alpha--h7132678_0"
 - "0.53.alpha--h7132678_1"
 - "0.53.alpha--he4a0461_2"
 - "0.53.alpha--h577a1d6_3"
description: "singularity registry hpc automated addition for gfa1"
config: {"url": "https://biocontainers.pro/tools/gfa1", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gfa1", "latest": {"0.53.alpha--h577a1d6_3": "sha256:7be99c3652a748f842a5c845c75b513511e78aa3fa67ec8c496930996edbffc4"}, "tags": {"0.53.alpha--h7132678_0": "sha256:f42d02eb1cc0ffab97d0fd992fa16374fd61fb22a7348c747db2755da1e96474", "0.53.alpha--h7132678_1": "sha256:be9b026fc2527e86ab561257ed978637b1c2cd707de0c48c4a242830ad2ececd", "0.53.alpha--he4a0461_2": "sha256:1665da30c47769d82aa2085b4582696af49c6f3a29688df22f6b4c0776a9f391", "0.53.alpha--h577a1d6_3": "sha256:7be99c3652a748f842a5c845c75b513511e78aa3fa67ec8c496930996edbffc4"}, "docker": "quay.io/biocontainers/gfa1", "aliases": {"falcon2gfa": "/usr/local/bin/falcon2gfa", "fastg2gfa": "/usr/local/bin/fastg2gfa", "gfaview": "/usr/local/bin/gfaview", "mag2gfa": "/usr/local/bin/mag2gfa", "supernova2gfa": "/usr/local/bin/supernova2gfa"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfa1.
singularity registry hpc automated addition for gfa1
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfa1
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfa1:0.53.alpha--h577a1d6_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfa1/0.53.alpha--h577a1d6_3
$ module help quay.io/biocontainers/gfa1/0.53.alpha--h577a1d6_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfa1-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfa1-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfa1-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfa1-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfa1-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfa1-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### falcon2gfa

```bash
$ singularity exec <container> /usr/local/bin/falcon2gfa
$ podman run --it --rm --entrypoint /usr/local/bin/falcon2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/falcon2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fastg2gfa

```bash
$ singularity exec <container> /usr/local/bin/fastg2gfa
$ podman run --it --rm --entrypoint /usr/local/bin/fastg2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fastg2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfaview

```bash
$ singularity exec <container> /usr/local/bin/gfaview
$ podman run --it --rm --entrypoint /usr/local/bin/gfaview   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfaview   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mag2gfa

```bash
$ singularity exec <container> /usr/local/bin/mag2gfa
$ podman run --it --rm --entrypoint /usr/local/bin/mag2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mag2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### supernova2gfa

```bash
$ singularity exec <container> /usr/local/bin/supernova2gfa
$ podman run --it --rm --entrypoint /usr/local/bin/supernova2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/supernova2gfa   -v ${PWD} -w ${PWD} <container> -c " $@"
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