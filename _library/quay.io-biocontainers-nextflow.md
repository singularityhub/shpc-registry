---
layout: container
name:  "quay.io/biocontainers/nextflow"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/nextflow/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/nextflow/container.yaml"
updated_at: "2024-01-08 03:20:35.456284"
latest: "23.10.0--hdfd78af_0"
container_url: "https://biocontainers.pro/tools/nextflow"
aliases:
 - "nextflow"
 - "nextflow.bak"
 - "jpackage"
 - "basenc"
 - "b2sum"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
 - "chcon"
 - "chgrp"
 - "chmod"
versions:
 - "22.10.0--h4a94de4_0"
 - "22.10.1--h4a94de4_0"
 - "22.10.4--h4a94de4_0"
 - "22.10.6--h4a94de4_0"
 - "23.04.1--h4a94de4_2"
 - "23.04.1--h2a3209d_3"
 - "23.04.3--h2a3209d_0"
 - "23.04.4--h2a3209d_0"
 - "23.10.0--hdfd78af_0"
description: "shpc-registry automated BioContainers addition for nextflow"
config: {"url": "https://biocontainers.pro/tools/nextflow", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for nextflow", "latest": {"23.10.0--hdfd78af_0": "sha256:f935a5a5cc26b1256cc6c4e2edcd24fd655e8c1e3093ec39d8b663a8f79dd38d"}, "tags": {"22.10.0--h4a94de4_0": "sha256:c04ca8aca1b35ce4a912acbe5df5b795179d28440da9b27cc87198a8ea1ea859", "22.10.1--h4a94de4_0": "sha256:0e58fcbbf77e6fc6e3d77507ff624d81bcc9c436026093a8cda5b5deb72f048c", "22.10.4--h4a94de4_0": "sha256:096fee76e53ec0f5a252d86b4b681310c2c523961e26ef3af12db86351250268", "22.10.6--h4a94de4_0": "sha256:7cee9ef519fae6ce9bee24693c5914a6a7ffde5d196823805114cfc9aac53105", "23.04.1--h4a94de4_2": "sha256:f052db0d37c285d7fd60079e594d50404a094a711b9f7deb92b7b96b6b2a67f1", "23.04.1--h2a3209d_3": "sha256:b49e1aa6497556c0ac06f21778308456a8318658a8fdd44c309ecd661f3114d7", "23.04.3--h2a3209d_0": "sha256:cfdb67b18b14145a693d15413ee8819c299e67ddaeab55a19f405a1485a59c43", "23.04.4--h2a3209d_0": "sha256:1510bc07ac54026c9587267f5f7c6e29dfe2949fd945e4932c9b2ed01a2df7f6", "23.10.0--hdfd78af_0": "sha256:f935a5a5cc26b1256cc6c4e2edcd24fd655e8c1e3093ec39d8b663a8f79dd38d"}, "docker": "quay.io/biocontainers/nextflow", "aliases": {"nextflow": "/usr/local/bin/nextflow", "nextflow.bak": "/usr/local/bin/nextflow.bak", "jpackage": "/usr/local/bin/jpackage", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/nextflow.
shpc-registry automated BioContainers addition for nextflow
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/nextflow
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/nextflow:23.10.0--hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/nextflow/23.10.0--hdfd78af_0
$ module help quay.io/biocontainers/nextflow/23.10.0--hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### nextflow-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### nextflow-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### nextflow-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### nextflow-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### nextflow-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### nextflow-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nextflow

```bash
$ singularity exec <container> /usr/local/bin/nextflow
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nextflow.bak

```bash
$ singularity exec <container> /usr/local/bin/nextflow.bak
$ podman run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nextflow.bak   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### jpackage

```bash
$ singularity exec <container> /usr/local/bin/jpackage
$ podman run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/jpackage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base32

```bash
$ singularity exec <container> /usr/local/bin/base32
$ podman run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base32   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### base64

```bash
$ singularity exec <container> /usr/local/bin/base64
$ podman run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/base64   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### basename

```bash
$ singularity exec <container> /usr/local/bin/basename
$ podman run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basename   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cat

```bash
$ singularity exec <container> /usr/local/bin/cat
$ podman run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chcon

```bash
$ singularity exec <container> /usr/local/bin/chcon
$ podman run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chcon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chgrp

```bash
$ singularity exec <container> /usr/local/bin/chgrp
$ podman run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chgrp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chmod

```bash
$ singularity exec <container> /usr/local/bin/chmod
$ podman run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chmod   -v ${PWD} -w ${PWD} <container> -c " $@"
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