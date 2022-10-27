---
layout: container
name:  "quay.io/biocontainers/spine"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/spine/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/spine/container.yaml"
updated_at: "2022-10-27 00:53:11.240886"
latest: "0.3.2--pl5321hdfd78af_2"
container_url: "https://biocontainers.pro/tools/spine"
aliases:
 - "nucmer_backbone.pl"
 - "nucmer_multi.pl"
 - "spine.pl"
versions:
 - "0.3.2--pl5321hdfd78af_2"
description: "shpc-registry automated BioContainers addition for spine"
config: {"url": "https://biocontainers.pro/tools/spine", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for spine", "latest": {"0.3.2--pl5321hdfd78af_2": "sha256:29aef6f767385b946063d1da67f11042c20f8c5f6cce88d307ac4d934cd09478"}, "tags": {"0.3.2--pl5321hdfd78af_2": "sha256:29aef6f767385b946063d1da67f11042c20f8c5f6cce88d307ac4d934cd09478"}, "docker": "quay.io/biocontainers/spine", "aliases": {"nucmer_backbone.pl": "/usr/local/bin/nucmer_backbone.pl", "nucmer_multi.pl": "/usr/local/bin/nucmer_multi.pl", "spine.pl": "/usr/local/bin/spine.pl"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/spine.
shpc-registry automated BioContainers addition for spine
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/spine
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/spine:0.3.2--pl5321hdfd78af_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/spine/0.3.2--pl5321hdfd78af_2
$ module help quay.io/biocontainers/spine/0.3.2--pl5321hdfd78af_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### spine-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### spine-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### spine-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### spine-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### spine-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### spine-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nucmer_backbone.pl

```bash
$ singularity exec <container> /usr/local/bin/nucmer_backbone.pl
$ podman run --it --rm --entrypoint /usr/local/bin/nucmer_backbone.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucmer_backbone.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nucmer_multi.pl

```bash
$ singularity exec <container> /usr/local/bin/nucmer_multi.pl
$ podman run --it --rm --entrypoint /usr/local/bin/nucmer_multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nucmer_multi.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### spine.pl

```bash
$ singularity exec <container> /usr/local/bin/spine.pl
$ podman run --it --rm --entrypoint /usr/local/bin/spine.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/spine.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
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