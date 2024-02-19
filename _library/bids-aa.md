---
layout: container
name:  "bids/aa"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/bids/aa/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/bids/aa/container.yaml"
updated_at: "2024-02-19 03:16:32.511263"
latest: "enh_various"
container_url: "https://hub.docker.com/r/bids/aa"

versions:
 - "enh_various"
description: "BIDS App containing an instance of the Automatic Analysis. (https://github.com/BIDS-Apps/aa)"
config: {"docker": "bids/aa", "latest": {"enh_various": "sha256:c5b2c733ee6475449066f7dfe7865cc4bf2c74fe3c1150fd4f61a6fed2a6f78b"}, "tags": {"enh_various": "sha256:c5b2c733ee6475449066f7dfe7865cc4bf2c74fe3c1150fd4f61a6fed2a6f78b"}, "filter": ["enh_various"], "maintainer": "@vsoch", "description": "BIDS App containing an instance of the Automatic Analysis. (https://github.com/BIDS-Apps/aa)", "url": "https://hub.docker.com/r/bids/aa"}
---

This module is a singularity container wrapper for bids/aa.
BIDS App containing an instance of the Automatic Analysis. (https://github.com/BIDS-Apps/aa)
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install bids/aa
```

Or a specific version:

```bash
$ shpc install bids/aa:enh_various
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load bids/aa/enh_various
$ module help bids/aa/enh_various
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### aa-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### aa-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### aa-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### aa-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### aa-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### aa-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### aa

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