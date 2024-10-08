---
layout: container
name:  "quay.io/biocontainers/dicey"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/dicey/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/dicey/container.yaml"
updated_at: "2024-10-08 03:25:56.437866"
latest: "0.3.3--hf9970c3_0"
container_url: "https://biocontainers.pro/tools/dicey"
aliases:
 - "dicey"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.1.8--ha41ced6_3"
 - "0.2.1--ha41ced6_0"
 - "0.2.3--ha41ced6_0"
 - "0.2.3--h2af1cb8_1"
 - "0.2.3--h6b1aa3f_2"
 - "0.2.6--h6b1aa3f_0"
 - "0.2.8--h0d5efe1_0"
 - "0.3.1--h0d5efe1_0"
 - "0.3.3--hf9970c3_0"
description: "shpc-registry automated BioContainers addition for dicey"
config: {"url": "https://biocontainers.pro/tools/dicey", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for dicey", "latest": {"0.3.3--hf9970c3_0": "sha256:9423ee5e7b1a0ebbf59f2b349cf62b1adfd18052347a26d4cbd283b2a856bffd"}, "tags": {"0.1.8--ha41ced6_3": "sha256:93bbc25eca8732e7290c48c91e427d19df351dd25897d7bafc3ca9e6d5af4048", "0.2.1--ha41ced6_0": "sha256:40b09f5b1f7022d537796283d773629d23f51f677a244308238cbddff8ce8f25", "0.2.3--ha41ced6_0": "sha256:bf28a5d3c822adb77e930defdc3615fa54068700403296cf2b14ab7bae648689", "0.2.3--h2af1cb8_1": "sha256:293990b8d16643449c664f1e00622c99d005aef3f5fb682ccd144e90e0ce972a", "0.2.3--h6b1aa3f_2": "sha256:d0f202304755e2aa3fd38c5477baacabd3eba089b1f653847d8113c2faf6d0a8", "0.2.6--h6b1aa3f_0": "sha256:910a405314ecb81744d069c6446524e99a53754a26ba5d50a70a16003f2ccbbe", "0.2.8--h0d5efe1_0": "sha256:5c1693ebef023aac5f9894daa2312cce9edc8d57698fd7f2ce702ccf22b5f082", "0.3.1--h0d5efe1_0": "sha256:85c14d759b54cd1cb1736d10092d962686e68625f6fb48678049d348cca79dfc", "0.3.3--hf9970c3_0": "sha256:9423ee5e7b1a0ebbf59f2b349cf62b1adfd18052347a26d4cbd283b2a856bffd"}, "docker": "quay.io/biocontainers/dicey", "aliases": {"dicey": "/usr/local/bin/dicey", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/dicey.
shpc-registry automated BioContainers addition for dicey
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/dicey
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/dicey:0.3.3--hf9970c3_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/dicey/0.3.3--hf9970c3_0
$ module help quay.io/biocontainers/dicey/0.3.3--hf9970c3_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### dicey-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### dicey-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### dicey-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### dicey-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### dicey-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### dicey-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### dicey

```bash
$ singularity exec <container> /usr/local/bin/dicey
$ podman run --it --rm --entrypoint /usr/local/bin/dicey   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dicey   -v ${PWD} -w ${PWD} <container> -c " $@"
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