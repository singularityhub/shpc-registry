---
layout: container
name:  "quay.io/biocontainers/srnamapper"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/srnamapper/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/srnamapper/container.yaml"
updated_at: "2025-12-25 04:15:58.027599"
latest: "1.0.8--he4a0461_2"
container_url: "https://biocontainers.pro/tools/srnamapper"
aliases:
 - "srnaMapper"
versions:
 - "1.0.8--h7132678_1"
 - "1.0.8--he4a0461_2"
description: "shpc-registry automated BioContainers addition for srnamapper"
config: {"url": "https://biocontainers.pro/tools/srnamapper", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for srnamapper", "latest": {"1.0.8--he4a0461_2": "sha256:e107b89e1cdda16fa428f610ea124b04f53aeee973bcedc8f820c121dd05d4f7"}, "tags": {"1.0.8--h7132678_1": "sha256:836601646e94f18acb5dbac65d67252cdb3a50469ef4ad96d0126d0cf7ce7c88", "1.0.8--he4a0461_2": "sha256:e107b89e1cdda16fa428f610ea124b04f53aeee973bcedc8f820c121dd05d4f7"}, "docker": "quay.io/biocontainers/srnamapper", "aliases": {"srnaMapper": "/usr/local/bin/srnaMapper"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/srnamapper.
shpc-registry automated BioContainers addition for srnamapper
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/srnamapper
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/srnamapper:1.0.8--he4a0461_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/srnamapper/1.0.8--he4a0461_2
$ module help quay.io/biocontainers/srnamapper/1.0.8--he4a0461_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### srnamapper-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### srnamapper-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### srnamapper-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### srnamapper-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### srnamapper-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### srnamapper-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### srnaMapper

```bash
$ singularity exec <container> /usr/local/bin/srnaMapper
$ podman run --it --rm --entrypoint /usr/local/bin/srnaMapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/srnaMapper   -v ${PWD} -w ${PWD} <container> -c " $@"
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