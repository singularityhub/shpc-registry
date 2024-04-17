---
layout: container
name:  "quay.io/biocontainers/bioconductor-reusedata"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-reusedata/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-reusedata/container.yaml"
updated_at: "2024-04-17 02:28:13.587550"
latest: "1.0.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-reusedata"
aliases:
 - "corepack"
 - "git2"
 - "npx"
 - "node"
 - "npm"
 - "hb-info"
 - "tjbench"
 - "glpsol"
 - "pandoc"
versions:
 - "1.0.0--r43hdfd78af_0"
description: "singularity registry hpc automated addition for bioconductor-reusedata"
config: {"url": "https://biocontainers.pro/tools/bioconductor-reusedata", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for bioconductor-reusedata", "latest": {"1.0.0--r43hdfd78af_0": "sha256:ba191ccbf12afd07007517b2d364aac967ff7765625fe3e03daefad18f396c3f"}, "tags": {"1.0.0--r43hdfd78af_0": "sha256:ba191ccbf12afd07007517b2d364aac967ff7765625fe3e03daefad18f396c3f"}, "docker": "quay.io/biocontainers/bioconductor-reusedata", "aliases": {"corepack": "/usr/local/bin/corepack", "git2": "/usr/local/bin/git2", "npx": "/usr/local/bin/npx", "node": "/usr/local/bin/node", "npm": "/usr/local/bin/npm", "hb-info": "/usr/local/bin/hb-info", "tjbench": "/usr/local/bin/tjbench", "glpsol": "/usr/local/bin/glpsol", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-reusedata.
singularity registry hpc automated addition for bioconductor-reusedata
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-reusedata
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-reusedata:1.0.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-reusedata/1.0.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-reusedata/1.0.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-reusedata-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reusedata-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-reusedata-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-reusedata-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-reusedata-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-reusedata-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### corepack

```bash
$ singularity exec <container> /usr/local/bin/corepack
$ podman run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/corepack   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git2

```bash
$ singularity exec <container> /usr/local/bin/git2
$ podman run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npx

```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### node

```bash
$ singularity exec <container> /usr/local/bin/node
$ podman run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### npm

```bash
$ singularity exec <container> /usr/local/bin/npm
$ podman run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npm   -v ${PWD} -w ${PWD} <container> -c " $@"
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