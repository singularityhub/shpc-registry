---
layout: container
name:  "quay.io/biocontainers/phcue-ck"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/phcue-ck/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/phcue-ck/container.yaml"
updated_at: "2025-10-24 03:22:50.031947"
latest: "0.2.0--h3dc2dae_4"
container_url: "https://biocontainers.pro/tools/phcue-ck"
aliases:
 - "phcue-ck"
versions:
 - "0.2.0--h1f4ba0c_0"
 - "0.2.0--h5076881_2"
 - "0.2.0--hc234bb7_3"
 - "0.2.0--h3dc2dae_4"
description: "singularity registry hpc automated addition for phcue-ck"
config: {"url": "https://biocontainers.pro/tools/phcue-ck", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for phcue-ck", "latest": {"0.2.0--h3dc2dae_4": "sha256:d1a4afeda2e5eee2c156d5b38f913cb3a71d389ea66ff9d144570c2ada4283b4"}, "tags": {"0.2.0--h1f4ba0c_0": "sha256:c9525c902a42e9ba54e35917a79c9e3098e6c9cc80f9c74f8c5c615e66d5e550", "0.2.0--h5076881_2": "sha256:ddd4e8463e210aaff076345b37cf87c508295a2c8d791aca617ddfcd317bb936", "0.2.0--hc234bb7_3": "sha256:2f325db39efe48fd124d43af26f980e98e4d6241b1d81ae7bab853cba3147f7d", "0.2.0--h3dc2dae_4": "sha256:d1a4afeda2e5eee2c156d5b38f913cb3a71d389ea66ff9d144570c2ada4283b4"}, "docker": "quay.io/biocontainers/phcue-ck", "aliases": {"phcue-ck": "/usr/local/bin/phcue-ck"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/phcue-ck.
singularity registry hpc automated addition for phcue-ck
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/phcue-ck
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/phcue-ck:0.2.0--h3dc2dae_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/phcue-ck/0.2.0--h3dc2dae_4
$ module help quay.io/biocontainers/phcue-ck/0.2.0--h3dc2dae_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### phcue-ck-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### phcue-ck-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### phcue-ck-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### phcue-ck-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### phcue-ck-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### phcue-ck-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### phcue-ck

```bash
$ singularity exec <container> /usr/local/bin/phcue-ck
$ podman run --it --rm --entrypoint /usr/local/bin/phcue-ck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/phcue-ck   -v ${PWD} -w ${PWD} <container> -c " $@"
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