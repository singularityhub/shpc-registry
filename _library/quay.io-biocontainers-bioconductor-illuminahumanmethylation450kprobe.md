---
layout: container
name:  "quay.io/biocontainers/bioconductor-illuminahumanmethylation450kprobe"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-illuminahumanmethylation450kprobe/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-illuminahumanmethylation450kprobe/container.yaml"
updated_at: "2025-04-06 03:31:03.418230"
latest: "2.0.6--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-illuminahumanmethylation450kprobe"

versions:
 - "2.0.6--r41hdfd78af_9"
 - "2.0.6--r42hdfd78af_10"
 - "2.0.6--r43hdfd78af_11"
 - "2.0.6--r43hdfd78af_12"
 - "2.0.6--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-illuminahumanmethylation450kprobe"
config: {"url": "https://biocontainers.pro/tools/bioconductor-illuminahumanmethylation450kprobe", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-illuminahumanmethylation450kprobe", "latest": {"2.0.6--r44hdfd78af_13": "sha256:bced27f178533721eda74bd9652d1bb85843fc8ef8f4554d29214b3636a6a9d7"}, "tags": {"2.0.6--r41hdfd78af_9": "sha256:22190d99b7342b4a087133d6c4e7ebaa2393401e81192a054eb112152ddca814", "2.0.6--r42hdfd78af_10": "sha256:dd231295165690eed7d8f4243fef238c2c9b87148b6ded7922c3911d61c4e8f0", "2.0.6--r43hdfd78af_11": "sha256:6ba55cd54237680246cb6434ca0c4b22f2b91573b9870df678b425f5a567a59e", "2.0.6--r43hdfd78af_12": "sha256:570eb722f4465674499cf273b21f99e9e7f31101fb555a4755efcae44ab91c5e", "2.0.6--r44hdfd78af_13": "sha256:bced27f178533721eda74bd9652d1bb85843fc8ef8f4554d29214b3636a6a9d7"}, "docker": "quay.io/biocontainers/bioconductor-illuminahumanmethylation450kprobe"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-illuminahumanmethylation450kprobe.
shpc-registry automated BioContainers addition for bioconductor-illuminahumanmethylation450kprobe
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanmethylation450kprobe
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-illuminahumanmethylation450kprobe:2.0.6--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-illuminahumanmethylation450kprobe/2.0.6--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-illuminahumanmethylation450kprobe/2.0.6--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-illuminahumanmethylation450kprobe-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanmethylation450kprobe-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-illuminahumanmethylation450kprobe-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-illuminahumanmethylation450kprobe-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-illuminahumanmethylation450kprobe-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-illuminahumanmethylation450kprobe-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-illuminahumanmethylation450kprobe

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