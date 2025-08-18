---
layout: container
name:  "quay.io/biocontainers/bioconductor-lowmacaannotation"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lowmacaannotation/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lowmacaannotation/container.yaml"
updated_at: "2025-08-18 04:17:14.227015"
latest: "0.99.3--r44hdfd78af_13"
container_url: "https://biocontainers.pro/tools/bioconductor-lowmacaannotation"

versions:
 - "0.99.3--r41hdfd78af_9"
 - "0.99.3--r42hdfd78af_10"
 - "0.99.3--r43hdfd78af_11"
 - "0.99.3--r43hdfd78af_12"
 - "0.99.3--r44hdfd78af_13"
description: "shpc-registry automated BioContainers addition for bioconductor-lowmacaannotation"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lowmacaannotation", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lowmacaannotation", "latest": {"0.99.3--r44hdfd78af_13": "sha256:5dbe55750673db4d5e936983de9a8974ef769e4df05f056e419aa4b7d517e3ff"}, "tags": {"0.99.3--r41hdfd78af_9": "sha256:dbc4ab06b35d462c65a2be4019c2f51985707801243c33dd3ada3d9714fcf6eb", "0.99.3--r42hdfd78af_10": "sha256:017870cb6f905dfa5c455dac48d201d22ecd12d2ef231b8d5f4ce38a3edbe6cf", "0.99.3--r43hdfd78af_11": "sha256:e33e698260a1bbdcba90014c95277fd4edd546a646b49582345b7082692aa579", "0.99.3--r43hdfd78af_12": "sha256:ee4eede6c7d19f2002833a434aab1bd9767f20ffb23cc758f691c6c065499bb2", "0.99.3--r44hdfd78af_13": "sha256:5dbe55750673db4d5e936983de9a8974ef769e4df05f056e419aa4b7d517e3ff"}, "docker": "quay.io/biocontainers/bioconductor-lowmacaannotation"}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lowmacaannotation.
shpc-registry automated BioContainers addition for bioconductor-lowmacaannotation
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lowmacaannotation
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lowmacaannotation:0.99.3--r44hdfd78af_13
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lowmacaannotation/0.99.3--r44hdfd78af_13
$ module help quay.io/biocontainers/bioconductor-lowmacaannotation/0.99.3--r44hdfd78af_13
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lowmacaannotation-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lowmacaannotation-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lowmacaannotation-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lowmacaannotation-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lowmacaannotation-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lowmacaannotation-inspect-deffile:

```bash
$ singularity inspect -d <container>
```



#### bioconductor-lowmacaannotation

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