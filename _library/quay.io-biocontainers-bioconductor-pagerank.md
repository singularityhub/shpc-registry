---
layout: container
name:  "quay.io/biocontainers/bioconductor-pagerank"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-pagerank/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-pagerank/container.yaml"
updated_at: "2024-07-10 03:15:54.766366"
latest: "1.12.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-pagerank"

versions:
 - "1.4.0--r41hdfd78af_0"
 - "1.8.0--r42hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
 - "1.12.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-pagerank"
config: {"url": "https://biocontainers.pro/tools/bioconductor-pagerank", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-pagerank", "latest": {"1.12.0--r43hdfd78af_0": "sha256:edd13a68232e297d5455df4b50b6383e4754f2861457be559b96efef1d23f00e"}, "tags": {"1.4.0--r41hdfd78af_0": "sha256:b5a771f5053bcded5d32309e94588f16b50c9a7696a090d89c2919bfa9178e05", "1.8.0--r42hdfd78af_0": "sha256:e179d0dbd1d65043f5768136a7c6c10680b07b5429af773091d9c134b3fc261a", "1.10.0--r43hdfd78af_0": "sha256:93146d35e5719d5c47a18aeb26be5ae33e445960a3cf0501d10c803531b0f588", "1.12.0--r43hdfd78af_0": "sha256:edd13a68232e297d5455df4b50b6383e4754f2861457be559b96efef1d23f00e"}, "docker": "quay.io/biocontainers/bioconductor-pagerank"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-pagerank.
shpc-registry automated BioContainers addition for bioconductor-pagerank
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-pagerank
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-pagerank:1.12.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-pagerank/1.12.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-pagerank/1.12.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-pagerank-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pagerank-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-pagerank-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-pagerank-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-pagerank-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-pagerank-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-pagerank

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