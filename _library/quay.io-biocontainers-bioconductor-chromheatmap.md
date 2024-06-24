---
layout: container
name:  "quay.io/biocontainers/bioconductor-chromheatmap"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-chromheatmap/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-chromheatmap/container.yaml"
updated_at: "2024-06-24 03:31:34.366942"
latest: "1.56.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-chromheatmap"

versions:
 - "1.48.0--r41hdfd78af_0"
 - "1.52.0--r42hdfd78af_0"
 - "1.54.0--r43hdfd78af_0"
 - "1.56.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-chromheatmap"
config: {"url": "https://biocontainers.pro/tools/bioconductor-chromheatmap", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-chromheatmap", "latest": {"1.56.0--r43hdfd78af_0": "sha256:4739dfa0e0ec2c8c9b19e0ff855a470942dd134e45d838abed18603ac1f31851"}, "tags": {"1.48.0--r41hdfd78af_0": "sha256:e032a99fd2181f44337b36d45d586fe88427de2276645fb87bcd560a027b7a05", "1.52.0--r42hdfd78af_0": "sha256:29dcb752b644622454c21b386089d403f33cd7d41fe8a753584f99146b5c5662", "1.54.0--r43hdfd78af_0": "sha256:40df4f66683251c5223eb48d2b8b35cea577fcfbfc77cd50e15733569af3b20e", "1.56.0--r43hdfd78af_0": "sha256:4739dfa0e0ec2c8c9b19e0ff855a470942dd134e45d838abed18603ac1f31851"}, "docker": "quay.io/biocontainers/bioconductor-chromheatmap"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-chromheatmap.
shpc-registry automated BioContainers addition for bioconductor-chromheatmap
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-chromheatmap
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-chromheatmap:1.56.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-chromheatmap/1.56.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-chromheatmap/1.56.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-chromheatmap-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromheatmap-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-chromheatmap-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-chromheatmap-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-chromheatmap-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-chromheatmap-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-chromheatmap

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