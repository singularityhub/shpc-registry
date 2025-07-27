---
layout: container
name:  "quay.io/biocontainers/bioconductor-moda"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-moda/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-moda/container.yaml"
updated_at: "2025-07-27 04:05:04.331720"
latest: "1.28.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-moda"
aliases:
 - "wget"
 - "c89"
 - "c99"
versions:
 - "1.8.0--r351_0"
 - "1.24.0--r42hdfd78af_0"
 - "1.20.0--r41hdfd78af_0"
 - "1.18.0--r41hdfd78af_0"
 - "1.16.0--r40hdfd78af_1"
 - "1.14.0--r40_0"
 - "1.26.0--r43hdfd78af_0"
 - "1.28.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-moda"
config: {"url": "https://biocontainers.pro/tools/bioconductor-moda", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-moda", "latest": {"1.28.0--r43hdfd78af_0": "sha256:1bed725643f2c2901cd865ea684a2b49d0830c6048cc5db728cbd580aa641c9a"}, "tags": {"1.8.0--r351_0": "sha256:ab88094819f8a969838fb31de047a263ab16a571df9dd38b57180c2d2949bdf8", "1.24.0--r42hdfd78af_0": "sha256:9698e745df5dbcba744780bee300932c0d72233dd97e898b454a15befcc114c8", "1.20.0--r41hdfd78af_0": "sha256:d1e53ecd401f79f95434eee6768aaa83c5e47b678ed427010d4bb9fa5469c5e7", "1.18.0--r41hdfd78af_0": "sha256:d10e45620f2f2c4e2ebd537ea40da2f845ed54caa4cac9ad32a2dab04149ba2f", "1.16.0--r40hdfd78af_1": "sha256:86eedbb9e580b9b25c89284818b2bf91db8b035c42860049e865f1bfa9ef92e1", "1.14.0--r40_0": "sha256:f5e7ddc5d15c60dca82aaec751266ececfa215e1f3ac68d4c7ae341558cc7a7b", "1.26.0--r43hdfd78af_0": "sha256:81636843caf486c4dd7c46c87d074d378f2493738825f46845e15e51108c8277", "1.28.0--r43hdfd78af_0": "sha256:1bed725643f2c2901cd865ea684a2b49d0830c6048cc5db728cbd580aa641c9a"}, "docker": "quay.io/biocontainers/bioconductor-moda", "aliases": {"wget": "/usr/local/bin/wget", "c89": "/usr/local/bin/c89", "c99": "/usr/local/bin/c99"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-moda.
shpc-registry automated BioContainers addition for bioconductor-moda
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-moda
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-moda:1.28.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-moda/1.28.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-moda/1.28.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-moda-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moda-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-moda-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-moda-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-moda-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-moda-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### wget

```bash
$ singularity exec <container> /usr/local/bin/wget
$ podman run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wget   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c89

```bash
$ singularity exec <container> /usr/local/bin/c89
$ podman run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c89   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### c99

```bash
$ singularity exec <container> /usr/local/bin/c99
$ podman run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/c99   -v ${PWD} -w ${PWD} <container> -c " $@"
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