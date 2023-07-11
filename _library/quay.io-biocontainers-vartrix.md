---
layout: container
name:  "quay.io/biocontainers/vartrix"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/vartrix/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/vartrix/container.yaml"
updated_at: "2023-07-11 03:06:58.448684"
latest: "1.1.22--h27d5293_3"
container_url: "https://biocontainers.pro/tools/vartrix"
aliases:
 - "vartrix"
versions:
 - "1.1.22--hd11b1f6_1"
 - "1.1.22--hd11b1f6_2"
 - "1.1.22--h27d5293_3"
description: "shpc-registry automated BioContainers addition for vartrix"
config: {"url": "https://biocontainers.pro/tools/vartrix", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for vartrix", "latest": {"1.1.22--h27d5293_3": "sha256:69baf827a57cb5ddac4c1d61837a944da6ff55f45839775c669ab620dc729052"}, "tags": {"1.1.22--hd11b1f6_1": "sha256:8a2b494c0eb0afe4f0d77417e2cb8c9459b925e91c084f96df3ce84ba7ed4261", "1.1.22--hd11b1f6_2": "sha256:eeb54bd52048d4934eb6603d9aac116ef536887f7445472f9c6ab67967f2a169", "1.1.22--h27d5293_3": "sha256:69baf827a57cb5ddac4c1d61837a944da6ff55f45839775c669ab620dc729052"}, "docker": "quay.io/biocontainers/vartrix", "aliases": {"vartrix": "/usr/local/bin/vartrix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/vartrix.
shpc-registry automated BioContainers addition for vartrix
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/vartrix
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/vartrix:1.1.22--h27d5293_3
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/vartrix/1.1.22--h27d5293_3
$ module help quay.io/biocontainers/vartrix/1.1.22--h27d5293_3
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### vartrix-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### vartrix-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### vartrix-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### vartrix-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### vartrix-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### vartrix-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### vartrix

```bash
$ singularity exec <container> /usr/local/bin/vartrix
$ podman run --it --rm --entrypoint /usr/local/bin/vartrix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vartrix   -v ${PWD} -w ${PWD} <container> -c " $@"
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