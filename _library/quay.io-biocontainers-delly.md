---
layout: container
name:  "quay.io/biocontainers/delly"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/delly/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/delly/container.yaml"
updated_at: "2023-12-30 02:51:30.632260"
latest: "1.1.8--hb7e2ac5_0"
container_url: "https://biocontainers.pro/tools/delly"
aliases:
 - "delly"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "1.1.5--ha41ced6_1"
 - "1.1.6--ha41ced6_0"
 - "1.1.6--h2af1cb8_1"
 - "1.1.6--h6b1aa3f_2"
 - "1.1.7--h6b1aa3f_0"
 - "1.1.8--hb7e2ac5_0"
description: "shpc-registry automated BioContainers addition for delly"
config: {"url": "https://biocontainers.pro/tools/delly", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for delly", "latest": {"1.1.8--hb7e2ac5_0": "sha256:441c0d09e6a4f2d8af849001573a0501ea54c8824ddd7f6b8cacf2b804876a97"}, "tags": {"1.1.5--ha41ced6_1": "sha256:d6bf4e579f3b588d59e744cfbac51752b9a901af8dae06a22be65f436539dcd7", "1.1.6--ha41ced6_0": "sha256:1483554d377d5b30d98d2aa040a3eb33d6710b0caffe5e1002a047f36c21f452", "1.1.6--h2af1cb8_1": "sha256:1374d649c50930088fb7a4fd867e349f18036266e4d7c6800081b57b9a6fbbfc", "1.1.6--h6b1aa3f_2": "sha256:dce012f682fcb19cf07ae2e933d52666329f74dc50ce5aaac9e59c15ed9eea66", "1.1.7--h6b1aa3f_0": "sha256:04904f5e666e3e8d5fa44e1829bd66f1d4adaa68bffa3295c3ba98a7e26ccd61", "1.1.8--hb7e2ac5_0": "sha256:441c0d09e6a4f2d8af849001573a0501ea54c8824ddd7f6b8cacf2b804876a97"}, "docker": "quay.io/biocontainers/delly", "aliases": {"delly": "/usr/local/bin/delly", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/delly.
shpc-registry automated BioContainers addition for delly
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/delly
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/delly:1.1.8--hb7e2ac5_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/delly/1.1.8--hb7e2ac5_0
$ module help quay.io/biocontainers/delly/1.1.8--hb7e2ac5_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### delly-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### delly-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### delly-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### delly-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### delly-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### delly-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### delly

```bash
$ singularity exec <container> /usr/local/bin/delly
$ podman run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/delly   -v ${PWD} -w ${PWD} <container> -c " $@"
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