---
layout: container
name:  "quay.io/biocontainers/bioconductor-anvilworkflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-anvilworkflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-anvilworkflow/container.yaml"
updated_at: "2025-12-08 03:41:59.923662"
latest: "1.6.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-anvilworkflow"
aliases:
 - "hb-info"
 - "tjbench"
 - "pandoc"
versions:
 - "1.0.1--r43hdfd78af_0"
 - "1.2.0--r43hdfd78af_0"
 - "1.6.0--r44hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-anvilworkflow"
config: {"url": "https://biocontainers.pro/tools/bioconductor-anvilworkflow", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-anvilworkflow", "latest": {"1.6.0--r44hdfd78af_0": "sha256:8de578cc2fdf7c2072e702e572d9feb080b0625391307e1d1057d1a1a0709fe4"}, "tags": {"1.0.1--r43hdfd78af_0": "sha256:545c7c9d6f650abc1ee9ca023bb9e08ee6f7c446271c4e802fbe57c20928f49c", "1.2.0--r43hdfd78af_0": "sha256:b9b2777980a1406afaa2acce297b904a8b8f74de6e26f97106f8adf5f6c24d3e", "1.6.0--r44hdfd78af_0": "sha256:8de578cc2fdf7c2072e702e572d9feb080b0625391307e1d1057d1a1a0709fe4"}, "docker": "quay.io/biocontainers/bioconductor-anvilworkflow", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-anvilworkflow.
singularity registry hpc automated addition for bioconductor-anvilworkflow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-anvilworkflow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-anvilworkflow:1.6.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-anvilworkflow/1.6.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-anvilworkflow/1.6.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-anvilworkflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anvilworkflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-anvilworkflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-anvilworkflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-anvilworkflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-anvilworkflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hb-info

```bash
$ singularity exec <container> /usr/local/bin/hb-info
$ podman run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hb-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tjbench

```bash
$ singularity exec <container> /usr/local/bin/tjbench
$ podman run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tjbench   -v ${PWD} -w ${PWD} <container> -c " $@"
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