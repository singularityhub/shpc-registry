---
layout: container
name:  "quay.io/biocontainers/ryuto"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ryuto/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ryuto/container.yaml"
updated_at: "2024-01-20 02:37:10.503314"
latest: "1.6.3--hb03c83d_2"
container_url: "https://biocontainers.pro/tools/ryuto"
aliases:
 - "ryuto"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.6.2--h986a166_0"
 - "1.6.3--hf71abe7_0"
 - "1.6.3--h3c77e6d_1"
 - "1.6.3--hb03c83d_2"
description: "shpc-registry automated BioContainers addition for ryuto"
config: {"url": "https://biocontainers.pro/tools/ryuto", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for ryuto", "latest": {"1.6.3--hb03c83d_2": "sha256:ccce8b73299f42b1c3f33d3054425f7752f1a58991a598f509f85f8c179e0a21"}, "tags": {"1.6.2--h986a166_0": "sha256:f01e8dd6820263da949de9bc873c8cdf0e6571e72649709fa261d4bea92aef42", "1.6.3--hf71abe7_0": "sha256:563fb920750814b0c38f5df438f9316988d6a222e2eee02b1f0273ab8078d86f", "1.6.3--h3c77e6d_1": "sha256:69f4b40458d18924914df6ffdd0169578d37cde5b92dc1844d400bf6da1f4663", "1.6.3--hb03c83d_2": "sha256:ccce8b73299f42b1c3f33d3054425f7752f1a58991a598f509f85f8c179e0a21"}, "docker": "quay.io/biocontainers/ryuto", "aliases": {"ryuto": "/usr/local/bin/ryuto", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ryuto.
shpc-registry automated BioContainers addition for ryuto
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ryuto
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ryuto:1.6.3--hb03c83d_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ryuto/1.6.3--hb03c83d_2
$ module help quay.io/biocontainers/ryuto/1.6.3--hb03c83d_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ryuto-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ryuto-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ryuto-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ryuto-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ryuto-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ryuto-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ryuto

```bash
$ singularity exec <container> /usr/local/bin/ryuto
$ podman run --it --rm --entrypoint /usr/local/bin/ryuto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ryuto   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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