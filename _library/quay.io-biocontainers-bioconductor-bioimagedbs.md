---
layout: container
name:  "quay.io/biocontainers/bioconductor-bioimagedbs"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-bioimagedbs/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-bioimagedbs/container.yaml"
updated_at: "2022-10-27 00:49:06.210138"
latest: "1.2.2--r41hdfd78af_1"
container_url: "https://biocontainers.pro/tools/bioconductor-bioimagedbs"
aliases:
 - ".bioconductor-bioimagedbs-post-link.sh"
 - ".bioconductor-bioimagedbs-pre-unlink.sh"
 - "SvtAv1DecApp"
 - "SvtAv1EncApp"
 - "asn1Coding"
 - "asn1Decoding"
 - "asn1Parser"
 - "p11-kit"
 - "p11tool"
 - "trust"
 - "x265"
versions:
 - "1.2.2--r41hdfd78af_1"
description: "shpc-registry automated BioContainers addition for bioconductor-bioimagedbs"
config: {"url": "https://biocontainers.pro/tools/bioconductor-bioimagedbs", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-bioimagedbs", "latest": {"1.2.2--r41hdfd78af_1": "sha256:a9068e787b853d2a626c9cd4f46942a7bbfc69be387a05b967397985fd8d8efe"}, "tags": {"1.2.2--r41hdfd78af_1": "sha256:a9068e787b853d2a626c9cd4f46942a7bbfc69be387a05b967397985fd8d8efe"}, "docker": "quay.io/biocontainers/bioconductor-bioimagedbs", "aliases": {".bioconductor-bioimagedbs-post-link.sh": "/usr/local/bin/.bioconductor-bioimagedbs-post-link.sh", ".bioconductor-bioimagedbs-pre-unlink.sh": "/usr/local/bin/.bioconductor-bioimagedbs-pre-unlink.sh", "SvtAv1DecApp": "/usr/local/bin/SvtAv1DecApp", "SvtAv1EncApp": "/usr/local/bin/SvtAv1EncApp", "asn1Coding": "/usr/local/bin/asn1Coding", "asn1Decoding": "/usr/local/bin/asn1Decoding", "asn1Parser": "/usr/local/bin/asn1Parser", "p11-kit": "/usr/local/bin/p11-kit", "p11tool": "/usr/local/bin/p11tool", "trust": "/usr/local/bin/trust", "x265": "/usr/local/bin/x265"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-bioimagedbs.
shpc-registry automated BioContainers addition for bioconductor-bioimagedbs
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-bioimagedbs
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-bioimagedbs:1.2.2--r41hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-bioimagedbs/1.2.2--r41hdfd78af_1
$ module help quay.io/biocontainers/bioconductor-bioimagedbs/1.2.2--r41hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-bioimagedbs-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioimagedbs-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-bioimagedbs-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-bioimagedbs-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-bioimagedbs-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-bioimagedbs-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### .bioconductor-bioimagedbs-post-link.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-bioimagedbs-post-link.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-bioimagedbs-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-bioimagedbs-post-link.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### .bioconductor-bioimagedbs-pre-unlink.sh

```bash
$ singularity exec <container> /usr/local/bin/.bioconductor-bioimagedbs-pre-unlink.sh
$ podman run --it --rm --entrypoint /usr/local/bin/.bioconductor-bioimagedbs-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/.bioconductor-bioimagedbs-pre-unlink.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SvtAv1DecApp

```bash
$ singularity exec <container> /usr/local/bin/SvtAv1DecApp
$ podman run --it --rm --entrypoint /usr/local/bin/SvtAv1DecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SvtAv1DecApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### SvtAv1EncApp

```bash
$ singularity exec <container> /usr/local/bin/SvtAv1EncApp
$ podman run --it --rm --entrypoint /usr/local/bin/SvtAv1EncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/SvtAv1EncApp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Coding

```bash
$ singularity exec <container> /usr/local/bin/asn1Coding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Coding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Decoding

```bash
$ singularity exec <container> /usr/local/bin/asn1Decoding
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Decoding   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### asn1Parser

```bash
$ singularity exec <container> /usr/local/bin/asn1Parser
$ podman run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/asn1Parser   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11-kit

```bash
$ singularity exec <container> /usr/local/bin/p11-kit
$ podman run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11-kit   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### p11tool

```bash
$ singularity exec <container> /usr/local/bin/p11tool
$ podman run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/p11tool   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### trust

```bash
$ singularity exec <container> /usr/local/bin/trust
$ podman run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/trust   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### x265

```bash
$ singularity exec <container> /usr/local/bin/x265
$ podman run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/x265   -v ${PWD} -w ${PWD} <container> -c " $@"
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