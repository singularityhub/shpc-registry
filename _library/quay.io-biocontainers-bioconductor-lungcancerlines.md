---
layout: container
name:  "quay.io/biocontainers/bioconductor-lungcancerlines"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lungcancerlines/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lungcancerlines/container.yaml"
updated_at: "2024-11-17 03:43:30.828937"
latest: "0.40.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lungcancerlines"

versions:
 - "0.32.0--r41hdfd78af_1"
 - "0.36.0--r42hdfd78af_0"
 - "0.38.0--r43hdfd78af_0"
 - "0.40.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lungcancerlines"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lungcancerlines", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lungcancerlines", "latest": {"0.40.0--r43hdfd78af_0": "sha256:0ad304277c3dc1e3edf140bd931c70be32de7448c75041cb6e24d413847d5caa"}, "tags": {"0.32.0--r41hdfd78af_1": "sha256:d94d9e3e12aa706c1643410ff31609f8bf9d77cbf3cfde9decf63053765d27b8", "0.36.0--r42hdfd78af_0": "sha256:71df9ffcc75755ae141964f1635d3ee62c94a1e5d2c73c07afa3b26b2747cfa9", "0.38.0--r43hdfd78af_0": "sha256:5e664374bb47530c57499b72a0429d9afc4ede1472424172c495b85b277c4860", "0.40.0--r43hdfd78af_0": "sha256:0ad304277c3dc1e3edf140bd931c70be32de7448c75041cb6e24d413847d5caa"}, "docker": "quay.io/biocontainers/bioconductor-lungcancerlines"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lungcancerlines.
shpc-registry automated BioContainers addition for bioconductor-lungcancerlines
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lungcancerlines
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lungcancerlines:0.40.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lungcancerlines/0.40.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lungcancerlines/0.40.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lungcancerlines-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lungcancerlines-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lungcancerlines-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lungcancerlines-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lungcancerlines-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lungcancerlines-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lungcancerlines

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