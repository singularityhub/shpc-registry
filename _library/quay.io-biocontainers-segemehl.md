---
layout: container
name:  "quay.io/biocontainers/segemehl"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/segemehl/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/segemehl/container.yaml"
updated_at: "2025-04-19 03:19:24.948004"
latest: "0.3.4--h3e6c209_12"
container_url: "https://biocontainers.pro/tools/segemehl"
aliases:
 - "haarz.x"
 - "segemehl.x"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.3.4--h283732a_7"
 - "0.3.4--hf7d323f_8"
 - "0.3.4--hfe57441_9"
 - "0.3.4--h264e753_10"
 - "0.3.4--h3e6c209_11"
 - "0.3.4--h3e6c209_12"
description: "shpc-registry automated BioContainers addition for segemehl"
config: {"url": "https://biocontainers.pro/tools/segemehl", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for segemehl", "latest": {"0.3.4--h3e6c209_12": "sha256:09eb28707ca54958fc05b95253e2d98d8795645f64f7a224be1e71bc95315477"}, "tags": {"0.3.4--h283732a_7": "sha256:02ac65a0b7bcf1c25bf4189be655a4d694c54ca704dd700335e7440b52d832be", "0.3.4--hf7d323f_8": "sha256:987c37d4bb73c71bf68cc44d1d091b53f7bdca298489ff975530eebac49503d3", "0.3.4--hfe57441_9": "sha256:1a314cc58e0fb937ede97556fc44e9f415b00735a953262c9d686a76bc53d150", "0.3.4--h264e753_10": "sha256:f1c855dd1d182051c58ff41fb9ffb1bc19b3a3c9894374b69eb3ccddf1b9d74e", "0.3.4--h3e6c209_11": "sha256:2aa05e3f69611f62a2241c3d2d2d9b32317836533aba59637d636e044d473818", "0.3.4--h3e6c209_12": "sha256:09eb28707ca54958fc05b95253e2d98d8795645f64f7a224be1e71bc95315477"}, "docker": "quay.io/biocontainers/segemehl", "aliases": {"haarz.x": "/usr/local/bin/haarz.x", "segemehl.x": "/usr/local/bin/segemehl.x", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/segemehl.
shpc-registry automated BioContainers addition for segemehl
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/segemehl
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/segemehl:0.3.4--h3e6c209_12
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/segemehl/0.3.4--h3e6c209_12
$ module help quay.io/biocontainers/segemehl/0.3.4--h3e6c209_12
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### segemehl-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### segemehl-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### segemehl-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### segemehl-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### segemehl-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### segemehl-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### haarz.x

```bash
$ singularity exec <container> /usr/local/bin/haarz.x
$ podman run --it --rm --entrypoint /usr/local/bin/haarz.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haarz.x   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### segemehl.x

```bash
$ singularity exec <container> /usr/local/bin/segemehl.x
$ podman run --it --rm --entrypoint /usr/local/bin/segemehl.x   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/segemehl.x   -v ${PWD} -w ${PWD} <container> -c " $@"
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