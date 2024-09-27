---
layout: container
name:  "quay.io/biocontainers/bioconductor-mousethymusageing"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-mousethymusageing/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-mousethymusageing/container.yaml"
updated_at: "2024-09-27 03:27:05.180727"
latest: "1.10.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-mousethymusageing"

versions:
 - "1.2.0--r41hdfd78af_1"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
 - "1.10.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-mousethymusageing"
config: {"url": "https://biocontainers.pro/tools/bioconductor-mousethymusageing", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-mousethymusageing", "latest": {"1.10.0--r43hdfd78af_0": "sha256:4250a05b3f873c8f99b2a3637a41a5dfc946d69dcae9d85c6f2bce6aed64ee71"}, "tags": {"1.2.0--r41hdfd78af_1": "sha256:c5362003a8c69143afbbe5bb6f55f805c218c4b4f2b056662754e480b492fa94", "1.6.0--r42hdfd78af_0": "sha256:5fa593ee7c810d38b579119f80f4866d1eb7d889e206d028ebfefa888f2eef31", "1.8.0--r43hdfd78af_0": "sha256:6f4c3b7fdc27aa3546fb8b4f2b28caa4597261205cc307fbf0769a2442c52825", "1.10.0--r43hdfd78af_0": "sha256:4250a05b3f873c8f99b2a3637a41a5dfc946d69dcae9d85c6f2bce6aed64ee71"}, "docker": "quay.io/biocontainers/bioconductor-mousethymusageing"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-mousethymusageing.
shpc-registry automated BioContainers addition for bioconductor-mousethymusageing
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-mousethymusageing
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-mousethymusageing:1.10.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-mousethymusageing/1.10.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-mousethymusageing/1.10.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-mousethymusageing-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mousethymusageing-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-mousethymusageing-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-mousethymusageing-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-mousethymusageing-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-mousethymusageing-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-mousethymusageing

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