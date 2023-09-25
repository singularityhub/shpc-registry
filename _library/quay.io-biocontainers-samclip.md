---
layout: container
name:  "quay.io/biocontainers/samclip"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/samclip/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/samclip/container.yaml"
updated_at: "2023-09-25 02:43:08.853736"
latest: "0.4.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/samclip"
aliases:
 - "samclip"
 - "perl5.32.0"
 - "streamzip"
versions:
 - "0.4.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for samclip"
config: {"url": "https://biocontainers.pro/tools/samclip", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for samclip", "latest": {"0.4.0--hdfd78af_1": "sha256:5cda1c9937eee7d269ee40bd3a7a04472f22f5cb1c78f5b856dfecb7339246ea"}, "tags": {"0.4.0--hdfd78af_1": "sha256:5cda1c9937eee7d269ee40bd3a7a04472f22f5cb1c78f5b856dfecb7339246ea"}, "docker": "quay.io/biocontainers/samclip", "aliases": {"samclip": "/usr/local/bin/samclip", "perl5.32.0": "/usr/local/bin/perl5.32.0", "streamzip": "/usr/local/bin/streamzip"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/samclip.
shpc-registry automated BioContainers addition for samclip
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/samclip
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/samclip:0.4.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/samclip/0.4.0--hdfd78af_1
$ module help quay.io/biocontainers/samclip/0.4.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### samclip-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### samclip-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### samclip-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### samclip-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### samclip-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### samclip-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### samclip

```bash
$ singularity exec <container> /usr/local/bin/samclip
$ podman run --it --rm --entrypoint /usr/local/bin/samclip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/samclip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### perl5.32.0

```bash
$ singularity exec <container> /usr/local/bin/perl5.32.0
$ podman run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/perl5.32.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### streamzip

```bash
$ singularity exec <container> /usr/local/bin/streamzip
$ podman run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/streamzip   -v ${PWD} -w ${PWD} <container> -c " $@"
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