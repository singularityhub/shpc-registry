---
layout: container
name:  "quay.io/biocontainers/bioconductor-retrofit"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-retrofit/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-retrofit/container.yaml"
updated_at: "2025-04-16 05:34:45.304166"
latest: "1.6.0--r44he5774e6_0"
container_url: "https://biocontainers.pro/tools/bioconductor-retrofit"
aliases:
 - "hb-info"
 - "tjbench"
versions:
 - "1.0.0--r43hf17093f_0"
 - "1.2.0--r43hf17093f_1"
 - "1.6.0--r44he5774e6_0"
description: "singularity registry hpc automated addition for bioconductor-retrofit"
config: {"url": "https://biocontainers.pro/tools/bioconductor-retrofit", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-retrofit", "latest": {"1.6.0--r44he5774e6_0": "sha256:c46125869d376de191de6c44f08033acd30bbad2fdbb8a412d1e2f00918a28e5"}, "tags": {"1.0.0--r43hf17093f_0": "sha256:ecefbba1c0eede1ed254f70a133c2b49c74f2350dde81923ae950b0f0750e1cb", "1.2.0--r43hf17093f_1": "sha256:24f594f33a57727e25cffb3804c8dd80a4372853f8ac62f4520b0c11b0445e2d", "1.6.0--r44he5774e6_0": "sha256:c46125869d376de191de6c44f08033acd30bbad2fdbb8a412d1e2f00918a28e5"}, "docker": "quay.io/biocontainers/bioconductor-retrofit", "aliases": {"hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-retrofit.
singularity registry hpc automated addition for bioconductor-retrofit
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-retrofit
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-retrofit:1.6.0--r44he5774e6_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-retrofit/1.6.0--r44he5774e6_0
$ module help quay.io/biocontainers/bioconductor-retrofit/1.6.0--r44he5774e6_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-retrofit-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-retrofit-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-retrofit-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-retrofit-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-retrofit-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-retrofit-inspect-deffile:

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