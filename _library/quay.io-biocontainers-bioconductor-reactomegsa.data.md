---
layout: container
name:  "quay.io/biocontainers/bioconductor-reactomegsa.data"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-reactomegsa.data/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-reactomegsa.data/container.yaml"
updated_at: "2025-09-11 05:40:17.894381"
latest: "1.20.0--r44hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-reactomegsa.data"
aliases:
 - "geosop"
 - "geos-config"
 - "glpsol"
versions:
 - "1.8.0--r41hdfd78af_1"
 - "1.11.0--r42hdfd78af_0"
 - "1.14.0--r43hdfd78af_0"
 - "1.16.1--r43hdfd78af_0"
 - "1.20.0--r44hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-reactomegsa.data"
config: {"url": "https://biocontainers.pro/tools/bioconductor-reactomegsa.data", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-reactomegsa.data", "latest": {"1.20.0--r44hdfd78af_0": "sha256:b722a164e14dbfbae74bd9a2fddec644d5b464bbb1de5ad5e52c5473658a0af7"}, "tags": {"1.8.0--r41hdfd78af_1": "sha256:3d47ef470ff9d95f59bcf03dfcb18b05dbd14b8909dbc61cb2036ff30a1dc28d", "1.11.0--r42hdfd78af_0": "sha256:dd9543bb1a2844c8c1793cb5bc5f0f6ac26a219f124749efced4a350a8d32e07", "1.14.0--r43hdfd78af_0": "sha256:d50a1d96656f8edf62734cb1f454c8881da9d746cb9a3cf1de09033ae3d2a6e8", "1.16.1--r43hdfd78af_0": "sha256:c859c95ceb28641221b1d3ef0a82afdcf27eae18755365a80497e7849a6c5f84", "1.20.0--r44hdfd78af_0": "sha256:b722a164e14dbfbae74bd9a2fddec644d5b464bbb1de5ad5e52c5473658a0af7"}, "docker": "quay.io/biocontainers/bioconductor-reactomegsa.data", "aliases": {"geosop": "/usr/local/bin/geosop", "geos-config": "/usr/local/bin/geos-config", "glpsol": "/usr/local/bin/glpsol"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-reactomegsa.data.
shpc-registry automated BioContainers addition for bioconductor-reactomegsa.data
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-reactomegsa.data
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-reactomegsa.data:1.20.0--r44hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-reactomegsa.data/1.20.0--r44hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-reactomegsa.data/1.20.0--r44hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-reactomegsa.data-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reactomegsa.data-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reactomegsa.data-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-reactomegsa.data-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-reactomegsa.data-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-reactomegsa.data-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geos-config

```bash
$ singularity exec <container> /usr/local/bin/geos-config
$ podman run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geos-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### glpsol

```bash
$ singularity exec <container> /usr/local/bin/glpsol
$ podman run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/glpsol   -v ${PWD} -w ${PWD} <container> -c " $@"
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