---
layout: container
name:  "quay.io/biocontainers/pbfusion"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pbfusion/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pbfusion/container.yaml"
updated_at: "2025-04-10 03:26:45.854039"
latest: "0.5.1--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/pbfusion"
aliases:
 - "gffcache"
 - "pbfusion"
versions:
 - "0.1.0--hdfd78af_0"
 - "0.2.2--hdfd78af_0"
 - "0.3.1--hdfd78af_0"
 - "0.4.0--hdfd78af_0"
 - "0.4.1--hdfd78af_0"
 - "0.5.1--hdfd78af_0"
description: "singularity registry hpc automated addition for pbfusion"
config: {"url": "https://biocontainers.pro/tools/pbfusion", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pbfusion", "latest": {"0.5.1--hdfd78af_0": "sha256:987658a11fe55fea1368778ca0024a37c47c5319ccdbaa706b220afdd572b4df"}, "tags": {"0.1.0--hdfd78af_0": "sha256:3c1c3d83a9949a0bfbce7721f03dc9a0182cdc78679ec58c488d74bd994e4824", "0.2.2--hdfd78af_0": "sha256:aa8d3b936c9c6f1ed75853fd83af7d5e2d0fce4a742e275b82169a52065d567a", "0.3.1--hdfd78af_0": "sha256:c5e94d025224cdb8d0df0953c2ebe7b60987fe905c73e7fc3530b474bce4a147", "0.4.0--hdfd78af_0": "sha256:0c41532dedbd0e17b2acfef806be530d57a7db227e58b6d1deac41b25fc058b7", "0.4.1--hdfd78af_0": "sha256:82709bf807b26cdcf9afa8ab40490f759264db1a90b8a145ed7928be4840dd17", "0.5.1--hdfd78af_0": "sha256:987658a11fe55fea1368778ca0024a37c47c5319ccdbaa706b220afdd572b4df"}, "docker": "quay.io/biocontainers/pbfusion", "aliases": {"gffcache": "/usr/local/bin/gffcache", "pbfusion": "/usr/local/bin/pbfusion"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pbfusion.
singularity registry hpc automated addition for pbfusion
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pbfusion
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pbfusion:0.5.1--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pbfusion/0.5.1--hdfd78af_0
$ module help quay.io/biocontainers/pbfusion/0.5.1--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pbfusion-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pbfusion-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pbfusion-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pbfusion-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pbfusion-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pbfusion-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gffcache

```bash
$ singularity exec <container> /usr/local/bin/gffcache
$ podman run --it --rm --entrypoint /usr/local/bin/gffcache   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gffcache   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pbfusion

```bash
$ singularity exec <container> /usr/local/bin/pbfusion
$ podman run --it --rm --entrypoint /usr/local/bin/pbfusion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pbfusion   -v ${PWD} -w ${PWD} <container> -c " $@"
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