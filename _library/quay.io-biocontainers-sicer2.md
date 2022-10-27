---
layout: container
name:  "quay.io/biocontainers/sicer2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/sicer2/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/sicer2/container.yaml"
updated_at: "2022-10-27 00:54:05.164013"
latest: "1.0.3--py37h37892f8_2"
container_url: "https://biocontainers.pro/tools/sicer2"
aliases:
 - "recognicer"
 - "recognicer_df"
 - "sicer"
 - "sicer_df"
versions:
 - "1.0.3--py37h37892f8_2"
description: "shpc-registry automated BioContainers addition for sicer2"
config: {"url": "https://biocontainers.pro/tools/sicer2", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for sicer2", "latest": {"1.0.3--py37h37892f8_2": "sha256:d5e957a3d4b01a6cbe55117151fbbd664d261524c1f367585b31c1123980cf9f"}, "tags": {"1.0.3--py37h37892f8_2": "sha256:d5e957a3d4b01a6cbe55117151fbbd664d261524c1f367585b31c1123980cf9f"}, "docker": "quay.io/biocontainers/sicer2", "aliases": {"recognicer": "/usr/local/bin/recognicer", "recognicer_df": "/usr/local/bin/recognicer_df", "sicer": "/usr/local/bin/sicer", "sicer_df": "/usr/local/bin/sicer_df"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/sicer2.
shpc-registry automated BioContainers addition for sicer2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/sicer2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/sicer2:1.0.3--py37h37892f8_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/sicer2/1.0.3--py37h37892f8_2
$ module help quay.io/biocontainers/sicer2/1.0.3--py37h37892f8_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### sicer2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### sicer2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### sicer2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### sicer2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### sicer2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### sicer2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### recognicer

```bash
$ singularity exec <container> /usr/local/bin/recognicer
$ podman run --it --rm --entrypoint /usr/local/bin/recognicer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recognicer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### recognicer_df

```bash
$ singularity exec <container> /usr/local/bin/recognicer_df
$ podman run --it --rm --entrypoint /usr/local/bin/recognicer_df   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recognicer_df   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sicer

```bash
$ singularity exec <container> /usr/local/bin/sicer
$ podman run --it --rm --entrypoint /usr/local/bin/sicer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sicer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sicer_df

```bash
$ singularity exec <container> /usr/local/bin/sicer_df
$ podman run --it --rm --entrypoint /usr/local/bin/sicer_df   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sicer_df   -v ${PWD} -w ${PWD} <container> -c " $@"
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