---
layout: container
name:  "quay.io/biocontainers/bioconductor-zebrafishprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-zebrafishprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-zebrafishprobe/container.yaml"
updated_at: "2025-04-17 03:46:42.880347"
latest: "2.18.0--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-zebrafishprobe"

versions:
 - "2.18.0--r41hdfd78af_9"
 - "2.18.0--r42hdfd78af_10"
 - "2.18.0--r43hdfd78af_11"
 - "2.18.0--r43hdfd78af_12"
 - "2.18.0--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-zebrafishprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-zebrafishprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-zebrafishprobe", "latest": {"2.18.0--r44hdfd78af_13": "sha256:58809adc05fd5ca45759743d0a6e71f9fc4e8f67f2d13b4546ef389193cdbc40"}, "tags": {"2.18.0--r41hdfd78af_9": "sha256:43edb27a668d10ab3c064d2de7dc35710154390d96e4b94462a83fab2e9baa9f", "2.18.0--r42hdfd78af_10": "sha256:c18117f09a910d4015b519dacd3ac7ba0ab8e07a7081b4174427f4a621583a32", "2.18.0--r43hdfd78af_11": "sha256:6726b236e56c6ab09b1accf1ecae9688fee4d096f47b85c6084816dfa0241ca3", "2.18.0--r43hdfd78af_12": "sha256:180beefdf6ddccbd4d42c3a024628f85702223683246ee3e9525b957e3199c11", "2.18.0--r44hdfd78af_13": "sha256:58809adc05fd5ca45759743d0a6e71f9fc4e8f67f2d13b4546ef389193cdbc40"}, "docker": "quay.io/biocontainers/bioconductor-zebrafishprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-zebrafishprobe.
shpc-registry automated BioContainers addition for bioconductor-zebrafishprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-zebrafishprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-zebrafishprobe:2.18.0--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-zebrafishprobe/2.18.0--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-zebrafishprobe/2.18.0--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-zebrafishprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zebrafishprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-zebrafishprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-zebrafishprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-zebrafishprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-zebrafishprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-zebrafishprobe

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
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