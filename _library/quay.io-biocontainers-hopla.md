---
layout: container
name:  "quay.io/biocontainers/hopla"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/hopla/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/hopla/container.yaml"
updated_at: "2023-12-03 03:01:57.329692"
latest: "1.2.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/hopla"
aliases:
 - "hapmapConverter"
 - "hopla"
 - "merlin"
 - "merlin-offline"
 - "merlin-regress"
 - "minx"
 - "minx-offline"
 - "pedmerge"
 - "pedstats"
 - "pedwipe"
 - "pandoc-server"
 - "pandoc"
versions:
 - "1.2.0--hdfd78af_0"
 - "1.2.1--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for hopla"
config: {"url": "https://biocontainers.pro/tools/hopla", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for hopla", "latest": {"1.2.1--hdfd78af_0": "sha256:69d1512a3eaca96e5bfa0c00c3792e33cb4b9a3ae4f7c084393bf0d42ff9d8d1"}, "tags": {"1.2.0--hdfd78af_0": "sha256:b51562cc5c7e42534544ce20eee9a5dc862e8882d498fe9e957de258344fe60c", "1.2.1--hdfd78af_0": "sha256:69d1512a3eaca96e5bfa0c00c3792e33cb4b9a3ae4f7c084393bf0d42ff9d8d1"}, "docker": "quay.io/biocontainers/hopla", "aliases": {"hapmapConverter": "/usr/local/bin/hapmapConverter", "hopla": "/usr/local/bin/hopla", "merlin": "/usr/local/bin/merlin", "merlin-offline": "/usr/local/bin/merlin-offline", "merlin-regress": "/usr/local/bin/merlin-regress", "minx": "/usr/local/bin/minx", "minx-offline": "/usr/local/bin/minx-offline", "pedmerge": "/usr/local/bin/pedmerge", "pedstats": "/usr/local/bin/pedstats", "pedwipe": "/usr/local/bin/pedwipe", "pandoc-server": "/usr/local/bin/pandoc-server", "pandoc": "/usr/local/bin/pandoc"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/hopla.
shpc-registry automated BioContainers addition for hopla
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/hopla
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/hopla:1.2.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/hopla/1.2.1--hdfd78af_0
$ module help quay.io/biocontainers/hopla/1.2.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### hopla-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### hopla-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### hopla-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### hopla-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### hopla-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### hopla-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### hapmapConverter

```bash
$ singularity exec <container> /usr/local/bin/hapmapConverter
$ podman run --it --rm --entrypoint /usr/local/bin/hapmapConverter   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hapmapConverter   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hopla

```bash
$ singularity exec <container> /usr/local/bin/hopla
$ podman run --it --rm --entrypoint /usr/local/bin/hopla   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hopla   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merlin

```bash
$ singularity exec <container> /usr/local/bin/merlin
$ podman run --it --rm --entrypoint /usr/local/bin/merlin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merlin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merlin-offline

```bash
$ singularity exec <container> /usr/local/bin/merlin-offline
$ podman run --it --rm --entrypoint /usr/local/bin/merlin-offline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merlin-offline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### merlin-regress

```bash
$ singularity exec <container> /usr/local/bin/merlin-regress
$ podman run --it --rm --entrypoint /usr/local/bin/merlin-regress   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/merlin-regress   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minx

```bash
$ singularity exec <container> /usr/local/bin/minx
$ podman run --it --rm --entrypoint /usr/local/bin/minx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### minx-offline

```bash
$ singularity exec <container> /usr/local/bin/minx-offline
$ podman run --it --rm --entrypoint /usr/local/bin/minx-offline   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/minx-offline   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pedmerge

```bash
$ singularity exec <container> /usr/local/bin/pedmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pedmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pedmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pedstats

```bash
$ singularity exec <container> /usr/local/bin/pedstats
$ podman run --it --rm --entrypoint /usr/local/bin/pedstats   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pedstats   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pedwipe

```bash
$ singularity exec <container> /usr/local/bin/pedwipe
$ podman run --it --rm --entrypoint /usr/local/bin/pedwipe   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pedwipe   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pandoc-server

```bash
$ singularity exec <container> /usr/local/bin/pandoc-server
$ podman run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pandoc-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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