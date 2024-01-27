---
layout: container
name:  "quay.io/biocontainers/cgat-apps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgat-apps/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cgat-apps/container.yaml"
updated_at: "2024-01-27 02:57:47.084260"
latest: "0.6.5--py37h179cca4_2"
container_url: "https://biocontainers.pro/tools/cgat-apps"
aliases:
 - "bq"
 - "cgat"
 - "docker-credential-gcloud"
 - "gcloud"
 - "time"
 - "gsutil"
 - "egrep"
 - "fgrep"
 - "grep"
 - "wigToBigWig"
 - "bedGraphToBigWig"
 - "bedToBigBed"
 - "basenc"
 - "b2sum"
 - "base32"
versions:
 - "0.6.5--py37h179cca4_2"
description: "shpc-registry automated BioContainers addition for cgat-apps"
config: {"url": "https://biocontainers.pro/tools/cgat-apps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cgat-apps", "latest": {"0.6.5--py37h179cca4_2": "sha256:d4c82e87ed915c5e18ad15801a0d6c999fcf204c37ded62a20bcb72036ae980b"}, "tags": {"0.6.5--py37h179cca4_2": "sha256:d4c82e87ed915c5e18ad15801a0d6c999fcf204c37ded62a20bcb72036ae980b"}, "docker": "quay.io/biocontainers/cgat-apps", "aliases": {"bq": "/usr/local/bin/bq", "cgat": "/usr/local/bin/cgat", "docker-credential-gcloud": "/usr/local/bin/docker-credential-gcloud", "gcloud": "/usr/local/bin/gcloud", "time": "/usr/local/bin/time", "gsutil": "/usr/local/bin/gsutil", "egrep": "/usr/local/bin/egrep", "fgrep": "/usr/local/bin/fgrep", "grep": "/usr/local/bin/grep", "wigToBigWig": "/usr/local/bin/wigToBigWig", "bedGraphToBigWig": "/usr/local/bin/bedGraphToBigWig", "bedToBigBed": "/usr/local/bin/bedToBigBed", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cgat-apps.
shpc-registry automated BioContainers addition for cgat-apps
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cgat-apps
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cgat-apps:0.6.5--py37h179cca4_2
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cgat-apps/0.6.5--py37h179cca4_2
$ module help quay.io/biocontainers/cgat-apps/0.6.5--py37h179cca4_2
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cgat-apps-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cgat-apps-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cgat-apps-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cgat-apps-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cgat-apps-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cgat-apps-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bq

```bash
$ singularity exec <container> /usr/local/bin/bq
$ podman run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cgat

```bash
$ singularity exec <container> /usr/local/bin/cgat
$ podman run --it --rm --entrypoint /usr/local/bin/cgat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cgat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### docker-credential-gcloud

```bash
$ singularity exec <container> /usr/local/bin/docker-credential-gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/docker-credential-gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gcloud

```bash
$ singularity exec <container> /usr/local/bin/gcloud
$ podman run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gcloud   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### time

```bash
$ singularity exec <container> /usr/local/bin/time
$ podman run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/time   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gsutil

```bash
$ singularity exec <container> /usr/local/bin/gsutil
$ podman run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gsutil   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### egrep

```bash
$ singularity exec <container> /usr/local/bin/egrep
$ podman run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/egrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### fgrep

```bash
$ singularity exec <container> /usr/local/bin/fgrep
$ podman run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/fgrep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### grep

```bash
$ singularity exec <container> /usr/local/bin/grep
$ podman run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/grep   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### wigToBigWig

```bash
$ singularity exec <container> /usr/local/bin/wigToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/wigToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedGraphToBigWig

```bash
$ singularity exec <container> /usr/local/bin/bedGraphToBigWig
$ podman run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedGraphToBigWig   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedToBigBed

```bash
$ singularity exec <container> /usr/local/bin/bedToBigBed
$ podman run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedToBigBed   -v ${PWD} -w ${PWD} <container> -c " $@"
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