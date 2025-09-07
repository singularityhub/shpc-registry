---
layout: container
name:  "quay.io/biocontainers/deacon"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/deacon/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/deacon/container.yaml"
updated_at: "2025-09-07 03:53:07.772753"
latest: "0.9.0--h4349ce8_0"
container_url: "https://biocontainers.pro/tools/deacon"
aliases:
 - "deacon"
versions:
 - "0.1.0--h4349ce8_0"
 - "0.3.0--h4349ce8_0"
 - "0.2.0--h4349ce8_0"
 - "0.5.0--h4349ce8_0"
 - "0.4.0--h4349ce8_0"
 - "0.7.0--h4349ce8_0"
 - "0.6.0--h4349ce8_0"
 - "0.9.0--h4349ce8_0"
 - "0.8.1--h4349ce8_0"
description: "singularity registry hpc automated addition for deacon"
config: {"url": "https://biocontainers.pro/tools/deacon", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for deacon", "latest": {"0.9.0--h4349ce8_0": "sha256:a426959600bc2146ac5b4b30f925ff4d3dc8982dbf6a7fe45544303dd5335064"}, "tags": {"0.1.0--h4349ce8_0": "sha256:22d6f9e7ada423cef2f4dbf54ce9f9dcf5916dbec64d7fd32944528d39f360d6", "0.3.0--h4349ce8_0": "sha256:14f3d7c7cf75f0fc81dc1194587236f76de34d872ab8168c39599e7ff6409872", "0.2.0--h4349ce8_0": "sha256:6143d3962e4109e76db9b944d81cc5b1aecf50dbc5c3d41780b207af2ed58dee", "0.5.0--h4349ce8_0": "sha256:300356398d8f0236022a867060d66e4904d581840b303a4d1f9bc89b12c2a3d8", "0.4.0--h4349ce8_0": "sha256:0a8da50af9f3e564f4aa012c4fed9238a409eba4487d743505644db14b8842d1", "0.7.0--h4349ce8_0": "sha256:a835f759b8c167127bd44f9b60a548fbe94c14dcc7ac10dd69584d5dba940a65", "0.6.0--h4349ce8_0": "sha256:dd6453573c6e285b343baa0b89351e36a40d8809745ab67f04bfb7452f5cc698", "0.9.0--h4349ce8_0": "sha256:a426959600bc2146ac5b4b30f925ff4d3dc8982dbf6a7fe45544303dd5335064", "0.8.1--h4349ce8_0": "sha256:80de276d9b20bc883aaf50d9917f95b3b4cd5620d2023fe4f7589cc3fba7fd07"}, "docker": "quay.io/biocontainers/deacon", "aliases": {"deacon": "/usr/local/bin/deacon"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/deacon.
singularity registry hpc automated addition for deacon
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/deacon
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/deacon:0.9.0--h4349ce8_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/deacon/0.9.0--h4349ce8_0
$ module help quay.io/biocontainers/deacon/0.9.0--h4349ce8_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### deacon-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### deacon-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### deacon-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### deacon-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### deacon-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### deacon-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### deacon

```bash
$ singularity exec <container> /usr/local/bin/deacon
$ podman run --it --rm --entrypoint /usr/local/bin/deacon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/deacon   -v ${PWD} -w ${PWD} <container> -c " $@"
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