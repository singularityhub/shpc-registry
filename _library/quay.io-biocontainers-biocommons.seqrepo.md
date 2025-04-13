---
layout: container
name:  "quay.io/biocontainers/biocommons.seqrepo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/biocommons.seqrepo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/biocommons.seqrepo/container.yaml"
updated_at: "2025-04-13 04:13:22.402481"
latest: "0.6.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/biocommons.seqrepo"
aliases:
 - "pyppeteer-install"
 - "seqrepo"
 - "sqlformat"
 - "yoyo"
 - "yoyo-migrate"
 - "coloredlogs"
 - "humanfriendly"
 - "tabulate"
 - "normalizer"
 - "tqdm"
 - "xslt-config"
 - "xsltproc"
 - "2to3-3.9"
 - "idle3.9"
 - "pydoc3.9"
versions:
 - "0.6.5--pyhdfd78af_0"
 - "0.6.6--pyhdfd78af_0"
 - "0.6.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for biocommons.seqrepo"
config: {"url": "https://biocontainers.pro/tools/biocommons.seqrepo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for biocommons.seqrepo", "latest": {"0.6.9--pyhdfd78af_0": "sha256:20b5af7a2defae3f50c627e5873b45dca552b12e57d57b5e60dbb0969e77afe3"}, "tags": {"0.6.5--pyhdfd78af_0": "sha256:0d81c542e2264b4b8773759139a07a8bc824ff6755d4a813dc588604e70c1f6b", "0.6.6--pyhdfd78af_0": "sha256:e38f8fbbb3fe72712c004ecfb6c9fa8a1399c02259b90774788b3db9998217fb", "0.6.9--pyhdfd78af_0": "sha256:20b5af7a2defae3f50c627e5873b45dca552b12e57d57b5e60dbb0969e77afe3"}, "docker": "quay.io/biocontainers/biocommons.seqrepo", "aliases": {"pyppeteer-install": "/usr/local/bin/pyppeteer-install", "seqrepo": "/usr/local/bin/seqrepo", "sqlformat": "/usr/local/bin/sqlformat", "yoyo": "/usr/local/bin/yoyo", "yoyo-migrate": "/usr/local/bin/yoyo-migrate", "coloredlogs": "/usr/local/bin/coloredlogs", "humanfriendly": "/usr/local/bin/humanfriendly", "tabulate": "/usr/local/bin/tabulate", "normalizer": "/usr/local/bin/normalizer", "tqdm": "/usr/local/bin/tqdm", "xslt-config": "/usr/local/bin/xslt-config", "xsltproc": "/usr/local/bin/xsltproc", "2to3-3.9": "/usr/local/bin/2to3-3.9", "idle3.9": "/usr/local/bin/idle3.9", "pydoc3.9": "/usr/local/bin/pydoc3.9"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/biocommons.seqrepo.
shpc-registry automated BioContainers addition for biocommons.seqrepo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/biocommons.seqrepo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/biocommons.seqrepo:0.6.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/biocommons.seqrepo/0.6.9--pyhdfd78af_0
$ module help quay.io/biocontainers/biocommons.seqrepo/0.6.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### biocommons.seqrepo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### biocommons.seqrepo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### biocommons.seqrepo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### biocommons.seqrepo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### biocommons.seqrepo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### biocommons.seqrepo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pyppeteer-install

```bash
$ singularity exec <container> /usr/local/bin/pyppeteer-install
$ podman run --it --rm --entrypoint /usr/local/bin/pyppeteer-install   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pyppeteer-install   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### seqrepo

```bash
$ singularity exec <container> /usr/local/bin/seqrepo
$ podman run --it --rm --entrypoint /usr/local/bin/seqrepo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/seqrepo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### sqlformat

```bash
$ singularity exec <container> /usr/local/bin/sqlformat
$ podman run --it --rm --entrypoint /usr/local/bin/sqlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/sqlformat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yoyo

```bash
$ singularity exec <container> /usr/local/bin/yoyo
$ podman run --it --rm --entrypoint /usr/local/bin/yoyo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yoyo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### yoyo-migrate

```bash
$ singularity exec <container> /usr/local/bin/yoyo-migrate
$ podman run --it --rm --entrypoint /usr/local/bin/yoyo-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/yoyo-migrate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### coloredlogs

```bash
$ singularity exec <container> /usr/local/bin/coloredlogs
$ podman run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/coloredlogs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### humanfriendly

```bash
$ singularity exec <container> /usr/local/bin/humanfriendly
$ podman run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/humanfriendly   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabulate

```bash
$ singularity exec <container> /usr/local/bin/tabulate
$ podman run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabulate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### normalizer

```bash
$ singularity exec <container> /usr/local/bin/normalizer
$ podman run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/normalizer   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tqdm

```bash
$ singularity exec <container> /usr/local/bin/tqdm
$ podman run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tqdm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xslt-config

```bash
$ singularity exec <container> /usr/local/bin/xslt-config
$ podman run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xslt-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### xsltproc

```bash
$ singularity exec <container> /usr/local/bin/xsltproc
$ podman run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/xsltproc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### 2to3-3.9

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.9
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idle3.9

```bash
$ singularity exec <container> /usr/local/bin/idle3.9
$ podman run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idle3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pydoc3.9

```bash
$ singularity exec <container> /usr/local/bin/pydoc3.9
$ podman run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pydoc3.9   -v ${PWD} -w ${PWD} <container> -c " $@"
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