---
layout: container
name:  "quay.io/biocontainers/r-mytai"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-mytai/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-mytai/container.yaml"
updated_at: "2025-03-17 03:29:25.958067"
latest: "0.9.3--r42hb0898b6_1"
container_url: "https://biocontainers.pro/tools/r-mytai"
aliases:
 - "tjbench"
 - "glpsol"
 - "pandoc"
versions:
 - "0.9.3--r42hb0898b6_0"
 - "0.9.3--r42hb0898b6_1"
description: "singularity registry hpc automated addition for r-mytai"
config: {"url": "https://biocontainers.pro/tools/r-mytai", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for r-mytai", "latest": {"0.9.3--r42hb0898b6_1": "sha256:f3bb711c9760387a41058a6f8bc414f6c9835ba4071c472c42b58e5b2f0645f9"}, "tags": {"0.9.3--r42hb0898b6_0": "sha256:f9107df9033afb0997c29b72786fa9ed7a329fbcffac992ee4dac7058ec32720", "0.9.3--r42hb0898b6_1": "sha256:f3bb711c9760387a41058a6f8bc414f6c9835ba4071c472c42b58e5b2f0645f9"}, "docker": "quay.io/biocontainers/r-mytai", "aliases": {"tjbench": "/usr/local/bin/tjbench", "glpsol": "/usr/local/bin/glpsol", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-mytai.
singularity registry hpc automated addition for r-mytai
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-mytai
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-mytai:0.9.3--r42hb0898b6_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-mytai/0.9.3--r42hb0898b6_1
$ module help quay.io/biocontainers/r-mytai/0.9.3--r42hb0898b6_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-mytai-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-mytai-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-mytai-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-mytai-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-mytai-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-mytai-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc

```bash
$ singularity exec <container> /usr/local/bin/pandoc
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc   -v ${PWD} -w ${PWD} <container> -c " $@"
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