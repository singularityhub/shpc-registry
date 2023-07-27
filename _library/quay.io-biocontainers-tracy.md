---
layout: container
name:  "quay.io/biocontainers/tracy"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/tracy/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/tracy/container.yaml"
updated_at: "2023-07-27 02:45:56.690085"
latest: "0.7.5--hd8a7f93_2"
container_url: "https://biocontainers.pro/tools/tracy"
aliases:
 - "tracy"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.7.2--ha41ced6_1"
 - "0.7.3--ha41ced6_0"
 - "0.7.3--h2af1cb8_1"
 - "0.7.5--h96c1cfd_0"
 - "0.7.5--hd8a7f93_2"
description: "shpc-registry automated BioContainers addition for tracy"
config: {"url": "https://biocontainers.pro/tools/tracy", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for tracy", "latest": {"0.7.5--hd8a7f93_2": "sha256:9c87038966bef37d84a3bc74218973d4e7ae7d056cab265731181bd479060a97"}, "tags": {"0.7.2--ha41ced6_1": "sha256:4f4dccdf37ed2df042da3430f7dbb498e297b729639677664b1edd35bf3f1397", "0.7.3--ha41ced6_0": "sha256:13a92e0cb86e47111184ff4972c0c36bee44f37107bfc2df6e49529662dd2bd7", "0.7.3--h2af1cb8_1": "sha256:da36fe6c2d69bd98ac56f90be9cefca6ed2f7c035ec865fa4cb19ea247800fc5", "0.7.5--h96c1cfd_0": "sha256:bed27c2858af936f270160da09c797f0102a7c300a11caa97fabe11abd6368d5", "0.7.5--hd8a7f93_2": "sha256:9c87038966bef37d84a3bc74218973d4e7ae7d056cab265731181bd479060a97"}, "docker": "quay.io/biocontainers/tracy", "aliases": {"tracy": "/usr/local/bin/tracy", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/tracy.
shpc-registry automated BioContainers addition for tracy
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/tracy
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/tracy:0.7.5--hd8a7f93_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/tracy/0.7.5--hd8a7f93_2
$ module help quay.io/biocontainers/tracy/0.7.5--hd8a7f93_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### tracy-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### tracy-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### tracy-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### tracy-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### tracy-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### tracy-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### tracy

```bash
$ singularity exec <container> /usr/local/bin/tracy
$ podman run --it --rm --entrypoint /usr/local/bin/tracy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tracy   -v ${PWD} -w ${PWD} <container> -c " $@"
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