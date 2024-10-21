---
layout: container
name:  "quay.io/biocontainers/r-acidsinglecell"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-acidsinglecell/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-acidsinglecell/container.yaml"
updated_at: "2024-10-21 03:31:07.899536"
latest: "0.4.2--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/r-acidsinglecell"

versions:
 - "0.2.0--r41hdfd78af_0"
 - "0.3.3--r42hdfd78af_1"
 - "0.3.4--r42hdfd78af_0"
 - "0.3.4--r42hdfd78af_1"
 - "0.3.5--r42hdfd78af_1"
 - "0.3.5--r43hdfd78af_2"
 - "0.3.6--r43hdfd78af_0"
 - "0.4.0--r43hdfd78af_0"
 - "0.4.1--r43hdfd78af_0"
 - "0.4.2--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for r-acidsinglecell"
config: {"url": "https://biocontainers.pro/tools/r-acidsinglecell", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-acidsinglecell", "latest": {"0.4.2--r43hdfd78af_0": "sha256:da3568d857b4ebe168643ad755af53d727de5d68c46801bff21e47304382816a"}, "tags": {"0.2.0--r41hdfd78af_0": "sha256:28547717f9ab2bbce71036b8347db6a2b766d568fd75f4cc4b865cdfa5f3b1f9", "0.3.3--r42hdfd78af_1": "sha256:2b15a88cf883b0e6df6f347feaf770c7ccab55af410e3d0144dbbd7d53c297ac", "0.3.4--r42hdfd78af_0": "sha256:3e4267d203b1f825a33bf40bb783962f0ed11c0a8419c71461ef98b8d74d9dfe", "0.3.4--r42hdfd78af_1": "sha256:ebfab07325552036d66415cede4055584a5916c371af9179829b8fdf9da02186", "0.3.5--r42hdfd78af_1": "sha256:5a6fbf955f7fae69f008a7391084c3e94b9b87ca535601ea27fae9d7ea6b2668", "0.3.5--r43hdfd78af_2": "sha256:ba14d7c32aa1307ef3407651e7b926315976dfe68747909069212adcc3fdfeef", "0.3.6--r43hdfd78af_0": "sha256:4e334cdb02b1b0e8fac749d23f56e8995488bdab51ad35add91b7d6a16dfc2f7", "0.4.0--r43hdfd78af_0": "sha256:ce00932d284e066719a89279db12324c08d91bd5fd3134c4b769d629ee35bb55", "0.4.1--r43hdfd78af_0": "sha256:35a8550268bb2cae4d0794a3102e2cf42c64edbc25b66c033bef5c8f2714ce10", "0.4.2--r43hdfd78af_0": "sha256:da3568d857b4ebe168643ad755af53d727de5d68c46801bff21e47304382816a"}, "docker": "quay.io/biocontainers/r-acidsinglecell"}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-acidsinglecell.
shpc-registry automated BioContainers addition for r-acidsinglecell
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-acidsinglecell
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-acidsinglecell:0.4.2--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-acidsinglecell/0.4.2--r43hdfd78af_0
$ module help quay.io/biocontainers/r-acidsinglecell/0.4.2--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-acidsinglecell-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-acidsinglecell-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-acidsinglecell-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-acidsinglecell-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-acidsinglecell-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-acidsinglecell-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### r-acidsinglecell

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