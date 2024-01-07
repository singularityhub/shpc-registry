---
layout: container
name:  "quay.io/biocontainers/bioconductor-etec16s"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-etec16s/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-etec16s/container.yaml"
updated_at: "2024-01-07 02:49:29.533661"
latest: "1.30.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-etec16s"

versions:
 - "1.22.0--r41hdfd78af_1"
 - "1.26.0--r42hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
 - "1.30.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-etec16s"
config: {"url": "https://biocontainers.pro/tools/bioconductor-etec16s", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-etec16s", "latest": {"1.30.0--r43hdfd78af_0": "sha256:e43de2901b4e54182e979a402d89f9aa2dc36f1ed4d67cffcf88810a2522f761"}, "tags": {"1.22.0--r41hdfd78af_1": "sha256:3f4b9296b86e8eaabb75abe13ba51fbb923f85b6e9287572ed09d6bb9995c2ba", "1.26.0--r42hdfd78af_0": "sha256:b1404d02656af56f608d371936002f096fddcbedd5cbbad19bdd19c62d9ca16e", "1.28.0--r43hdfd78af_0": "sha256:a5e414ebfbc537cf48520a061071ee366df9e8f67f64642a816b1b0e02adfee5", "1.30.0--r43hdfd78af_0": "sha256:e43de2901b4e54182e979a402d89f9aa2dc36f1ed4d67cffcf88810a2522f761"}, "docker": "quay.io/biocontainers/bioconductor-etec16s"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-etec16s.
shpc-registry automated BioContainers addition for bioconductor-etec16s
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-etec16s
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-etec16s:1.30.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-etec16s/1.30.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-etec16s/1.30.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-etec16s-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-etec16s-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-etec16s-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-etec16s-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-etec16s-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-etec16s-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-etec16s

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