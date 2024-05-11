---
layout: container
name:  "quay.io/biocontainers/arcas-hla"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/arcas-hla/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/arcas-hla/container.yaml"
updated_at: "2024-05-11 02:54:22.429925"
latest: "0.6.0--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/arcas-hla"
aliases:
 - "arcasHLA"
 - "git-lfs"
 - "kallisto"
 - "basenc"
 - "b2sum"
 - "base32"
 - "base64"
 - "basename"
 - "cat"
 - "chcon"
 - "chgrp"
 - "chmod"
 - "chown"
versions:
 - "0.5.0--hdfd78af_0"
 - "0.5.0--hdfd78af_1"
 - "0.5.0--hdfd78af_3"
 - "0.6.0--hdfd78af_0"
 - "0.6.0--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for arcas-hla"
config: {"url": "https://biocontainers.pro/tools/arcas-hla", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for arcas-hla", "latest": {"0.6.0--hdfd78af_1": "sha256:767d83d802595005d791526ec068159df152ae073c473f9a53f3b5e2d7960eee"}, "tags": {"0.5.0--hdfd78af_0": "sha256:85af348c01828a4f10da7f658b999e442413650c4fc3df5c07bb714c8d22868c", "0.5.0--hdfd78af_1": "sha256:86a9c3acb45a03533678049cc2054cd2a57d445dad190a09859d7c30ba46dc27", "0.5.0--hdfd78af_3": "sha256:646b240269d8f6928c8b0acbd2a9abcc455eafd62b5d67eea20b7e1a76b6188e", "0.6.0--hdfd78af_0": "sha256:82caf94fd5ffd3994a441d8368b55dce4c27ea968ff85e0d0365223ecf4322a7", "0.6.0--hdfd78af_1": "sha256:767d83d802595005d791526ec068159df152ae073c473f9a53f3b5e2d7960eee"}, "docker": "quay.io/biocontainers/arcas-hla", "aliases": {"arcasHLA": "/usr/local/bin/arcasHLA", "git-lfs": "/usr/local/bin/git-lfs", "kallisto": "/usr/local/bin/kallisto", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod", "chown": "/usr/local/bin/chown"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/arcas-hla.
shpc-registry automated BioContainers addition for arcas-hla
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/arcas-hla
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/arcas-hla:0.6.0--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/arcas-hla/0.6.0--hdfd78af_1
$ module help quay.io/biocontainers/arcas-hla/0.6.0--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### arcas-hla-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### arcas-hla-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### arcas-hla-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### arcas-hla-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### arcas-hla-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### arcas-hla-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### arcasHLA

```bash
$ singularity exec <container> /usr/local/bin/arcasHLA
$ podman run --it --rm --entrypoint /usr/local/bin/arcasHLA   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/arcasHLA   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### git-lfs

```bash
$ singularity exec <container> /usr/local/bin/git-lfs
$ podman run --it --rm --entrypoint /usr/local/bin/git-lfs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/git-lfs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kallisto

```bash
$ singularity exec <container> /usr/local/bin/kallisto
$ podman run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kallisto   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### chown

```bash
$ singularity exec <container> /usr/local/bin/chown
$ podman run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chown   -v ${PWD} -w ${PWD} <container> -c " $@"
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