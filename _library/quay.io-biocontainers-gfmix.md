---
layout: container
name:  "quay.io/biocontainers/gfmix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/gfmix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/gfmix/container.yaml"
updated_at: "2024-06-18 03:04:28.106297"
latest: "1.0.2--hdbdd923_2"
container_url: "https://biocontainers.pro/tools/gfmix"
aliases:
 - "alpha_est_mix_rt"
 - "gfmix"
 - "rert"
 - "treecns"
versions:
 - "1.0.2--h87f3376_0"
 - "1.0.2--hdbdd923_2"
description: "singularity registry hpc automated addition for gfmix"
config: {"url": "https://biocontainers.pro/tools/gfmix", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for gfmix", "latest": {"1.0.2--hdbdd923_2": "sha256:1cfb194290cc6b26a4337c93ef64e02385740ec5ae1f8cd9db93d9fcc1720454"}, "tags": {"1.0.2--h87f3376_0": "sha256:adb9d61278a1f2f5522f63335b1e8fba7b346a96ccae62e76aa5485015f5f7c3", "1.0.2--hdbdd923_2": "sha256:1cfb194290cc6b26a4337c93ef64e02385740ec5ae1f8cd9db93d9fcc1720454"}, "docker": "quay.io/biocontainers/gfmix", "aliases": {"alpha_est_mix_rt": "/usr/local/bin/alpha_est_mix_rt", "gfmix": "/usr/local/bin/gfmix", "rert": "/usr/local/bin/rert", "treecns": "/usr/local/bin/treecns"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/gfmix.
singularity registry hpc automated addition for gfmix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/gfmix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/gfmix:1.0.2--hdbdd923_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/gfmix/1.0.2--hdbdd923_2
$ module help quay.io/biocontainers/gfmix/1.0.2--hdbdd923_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### gfmix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### gfmix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### gfmix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### gfmix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### gfmix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### gfmix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### alpha_est_mix_rt

```bash
$ singularity exec <container> /usr/local/bin/alpha_est_mix_rt
$ podman run --it --rm --entrypoint /usr/local/bin/alpha_est_mix_rt   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/alpha_est_mix_rt   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gfmix

```bash
$ singularity exec <container> /usr/local/bin/gfmix
$ podman run --it --rm --entrypoint /usr/local/bin/gfmix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gfmix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### rert

```bash
$ singularity exec <container> /usr/local/bin/rert
$ podman run --it --rm --entrypoint /usr/local/bin/rert   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/rert   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### treecns

```bash
$ singularity exec <container> /usr/local/bin/treecns
$ podman run --it --rm --entrypoint /usr/local/bin/treecns   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/treecns   -v ${PWD} -w ${PWD} <container> -c " $@"
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