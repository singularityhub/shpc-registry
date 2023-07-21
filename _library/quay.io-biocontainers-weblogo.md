---
layout: container
name:  "quay.io/biocontainers/weblogo"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/weblogo/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/weblogo/container.yaml"
updated_at: "2023-07-21 03:28:44.077719"
latest: "3.7.9--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/weblogo"
aliases:
 - "weblogo"
 - "transformseq"
 - "dvipdf"
 - "eps2eps"
 - "gs"
 - "gsbj"
 - "gsdj"
 - "gsdj500"
 - "gslj"
 - "gslp"
 - "gsnd"
versions:
 - "3.7.9--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for weblogo"
config: {"url": "https://biocontainers.pro/tools/weblogo", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for weblogo", "latest": {"3.7.9--pyhdfd78af_0": "sha256:0a19729ee0a95b8d566c76b36e42a13c390fe0e3b46bcb5d8ce7f8d1608d3546"}, "tags": {"3.7.9--pyhdfd78af_0": "sha256:0a19729ee0a95b8d566c76b36e42a13c390fe0e3b46bcb5d8ce7f8d1608d3546"}, "docker": "quay.io/biocontainers/weblogo", "aliases": {"weblogo": "/usr/local/bin/weblogo", "transformseq": "/usr/local/bin/transformseq", "dvipdf": "/usr/local/bin/dvipdf", "eps2eps": "/usr/local/bin/eps2eps", "gs": "/usr/local/bin/gs", "gsbj": "/usr/local/bin/gsbj", "gsdj": "/usr/local/bin/gsdj", "gsdj500": "/usr/local/bin/gsdj500", "gslj": "/usr/local/bin/gslj", "gslp": "/usr/local/bin/gslp", "gsnd": "/usr/local/bin/gsnd"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/weblogo.
shpc-registry automated BioContainers addition for weblogo
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/weblogo
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/weblogo:3.7.9--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/weblogo/3.7.9--pyhdfd78af_0
$ module help quay.io/biocontainers/weblogo/3.7.9--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### weblogo-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### weblogo-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### weblogo-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### weblogo-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### weblogo-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### weblogo-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### weblogo

```bash
$ singularity exec <container> /usr/local/bin/weblogo
$ podman run --it --rm --entrypoint /usr/local/bin/weblogo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/weblogo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### transformseq

```bash
$ singularity exec <container> /usr/local/bin/transformseq
$ podman run --it --rm --entrypoint /usr/local/bin/transformseq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/transformseq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### dvipdf

```bash
$ singularity exec <container> /usr/local/bin/dvipdf
$ podman run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/dvipdf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### eps2eps

```bash
$ singularity exec <container> /usr/local/bin/eps2eps
$ podman run --it --rm --entrypoint /usr/local/bin/eps2eps   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/eps2eps   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gs

```bash
$ singularity exec <container> /usr/local/bin/gs
$ podman run --it --rm --entrypoint /usr/local/bin/gs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsbj

```bash
$ singularity exec <container> /usr/local/bin/gsbj
$ podman run --it --rm --entrypoint /usr/local/bin/gsbj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsbj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsdj

```bash
$ singularity exec <container> /usr/local/bin/gsdj
$ podman run --it --rm --entrypoint /usr/local/bin/gsdj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsdj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsdj500

```bash
$ singularity exec <container> /usr/local/bin/gsdj500
$ podman run --it --rm --entrypoint /usr/local/bin/gsdj500   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsdj500   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gslj

```bash
$ singularity exec <container> /usr/local/bin/gslj
$ podman run --it --rm --entrypoint /usr/local/bin/gslj   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gslj   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gslp

```bash
$ singularity exec <container> /usr/local/bin/gslp
$ podman run --it --rm --entrypoint /usr/local/bin/gslp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gslp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsnd

```bash
$ singularity exec <container> /usr/local/bin/gsnd
$ podman run --it --rm --entrypoint /usr/local/bin/gsnd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsnd   -v ${PWD} -w ${PWD} <container> -c " $@"
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