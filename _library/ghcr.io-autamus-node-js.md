---
layout: container
name:  "ghcr.io/autamus/node-js"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/ghcr.io/autamus/node-js/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/ghcr.io/autamus/node-js/container.yaml"
updated_at: "2024-09-12 02:44:09.410058"
latest: "15.3.0"
container_url: "https://github.com/orgs/autamus/packages/container/package/node-js"
aliases:
 - "node"
versions:
 - "15.3.0"
 - "latest"
description: "A JavaScript runtime built on Chrome's V8 JavaScript engine."
config: {"docker": "ghcr.io/autamus/node-js", "url": "https://github.com/orgs/autamus/packages/container/package/node-js", "maintainer": "@vsoch", "description": "A JavaScript runtime built on Chrome's V8 JavaScript engine.", "latest": {"15.3.0": "sha256:7f5c1e62b065e5c4c2bffb3f785acc090038590d694ee75c7a86ebc74497e46c"}, "tags": {"15.3.0": "sha256:7f5c1e62b065e5c4c2bffb3f785acc090038590d694ee75c7a86ebc74497e46c", "latest": "sha256:7f5c1e62b065e5c4c2bffb3f785acc090038590d694ee75c7a86ebc74497e46c"}, "aliases": {"node": "/opt/view/bin/node"}}
---

This module is a singularity container wrapper for ghcr.io/autamus/node-js.
A JavaScript runtime built on Chrome's V8 JavaScript engine.
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install ghcr.io/autamus/node-js
```

Or a specific version:

```bash
$ shpc install ghcr.io/autamus/node-js:15.3.0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load ghcr.io/autamus/node-js/15.3.0
$ module help ghcr.io/autamus/node-js/15.3.0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### node-js-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### node-js-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### node-js-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### node-js-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### node-js-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### node-js-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### node

```bash
$ singularity exec <container> /opt/view/bin/node
$ podman run --it --rm --entrypoint /opt/view/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /opt/view/bin/node   -v ${PWD} -w ${PWD} <container> -c " $@"
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