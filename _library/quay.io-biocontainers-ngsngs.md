---
layout: container
name:  "quay.io/biocontainers/ngsngs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/ngsngs/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/ngsngs/container.yaml"
updated_at: "2023-11-10 02:33:42.422884"
latest: "0.9.2--hce60e53_0"
container_url: "https://biocontainers.pro/tools/ngsngs"
aliases:
 - "ngsngs"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.9.0--h6448e42_0"
 - "0.9.0--hce60e53_1"
 - "0.9.2--hce60e53_0"
description: "singularity registry hpc automated addition for ngsngs"
config: {"url": "https://biocontainers.pro/tools/ngsngs", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for ngsngs", "latest": {"0.9.2--hce60e53_0": "sha256:5cee8593a37e41bbb129e7302ebd2f9525cc1d95a1e3c27085a16e7d9941b0ce"}, "tags": {"0.9.0--h6448e42_0": "sha256:a98120e8edea1eed923008318d178946c7ff99756e512ccfb504fb873fcfef4b", "0.9.0--hce60e53_1": "sha256:0880fe15c7b5480e38abf882a0decd4449e5e8f6343a535d3b8d3d96ae1582f7", "0.9.2--hce60e53_0": "sha256:5cee8593a37e41bbb129e7302ebd2f9525cc1d95a1e3c27085a16e7d9941b0ce"}, "docker": "quay.io/biocontainers/ngsngs", "aliases": {"ngsngs": "/usr/local/bin/ngsngs", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/ngsngs.
singularity registry hpc automated addition for ngsngs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/ngsngs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/ngsngs:0.9.2--hce60e53_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/ngsngs/0.9.2--hce60e53_0
$ module help quay.io/biocontainers/ngsngs/0.9.2--hce60e53_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### ngsngs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### ngsngs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### ngsngs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### ngsngs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### ngsngs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### ngsngs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### ngsngs

```bash
$ singularity exec <container> /usr/local/bin/ngsngs
$ podman run --it --rm --entrypoint /usr/local/bin/ngsngs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngsngs   -v ${PWD} -w ${PWD} <container> -c " $@"
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