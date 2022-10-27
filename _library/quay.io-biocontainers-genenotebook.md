---
layout: container
name:  "quay.io/biocontainers/genenotebook"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/genenotebook/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/genenotebook/container.yaml"
updated_at: "2022-10-27 00:51:41.661602"
latest: "0.3.1--h9f5acd7_1"
container_url: "https://biocontainers.pro/tools/genenotebook"
aliases:
 - "genenotebook"
 - "install_compass"
 - "mongo"
 - "mongod"
 - "mongos"
 - "node"
 - "npm"
 - "npx"
versions:
 - "0.3.1--h9f5acd7_1"
description: "shpc-registry automated BioContainers addition for genenotebook"
config: {"url": "https://biocontainers.pro/tools/genenotebook", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for genenotebook", "latest": {"0.3.1--h9f5acd7_1": "sha256:a30f10d56d1312fe0385ff04c55967b7073e782d8b38ef204e6b954701b15c41"}, "tags": {"0.3.1--h9f5acd7_1": "sha256:a30f10d56d1312fe0385ff04c55967b7073e782d8b38ef204e6b954701b15c41"}, "docker": "quay.io/biocontainers/genenotebook", "aliases": {"genenotebook": "/usr/local/bin/genenotebook", "install_compass": "/usr/local/bin/install_compass", "mongo": "/usr/local/bin/mongo", "mongod": "/usr/local/bin/mongod", "mongos": "/usr/local/bin/mongos", "node": "/usr/local/bin/node", "npm": "/usr/local/bin/npm", "npx": "/usr/local/bin/npx"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/genenotebook.
shpc-registry automated BioContainers addition for genenotebook
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/genenotebook
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/genenotebook:0.3.1--h9f5acd7_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/genenotebook/0.3.1--h9f5acd7_1
$ module help quay.io/biocontainers/genenotebook/0.3.1--h9f5acd7_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### genenotebook-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### genenotebook-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### genenotebook-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### genenotebook-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### genenotebook-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### genenotebook-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### genenotebook

```bash
$ singularity exec <container> /usr/local/bin/genenotebook
$ podman run --it --rm --entrypoint /usr/local/bin/genenotebook   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genenotebook   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### install_compass

```bash
$ singularity exec <container> /usr/local/bin/install_compass
$ podman run --it --rm --entrypoint /usr/local/bin/install_compass   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/install_compass   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongo

```bash
$ singularity exec <container> /usr/local/bin/mongo
$ podman run --it --rm --entrypoint /usr/local/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongod

```bash
$ singularity exec <container> /usr/local/bin/mongod
$ podman run --it --rm --entrypoint /usr/local/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongod   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mongos

```bash
$ singularity exec <container> /usr/local/bin/mongos
$ podman run --it --rm --entrypoint /usr/local/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mongos   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### npx

```bash
$ singularity exec <container> /usr/local/bin/npx
$ podman run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/npx   -v ${PWD} -w ${PWD} <container> -c " $@"
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