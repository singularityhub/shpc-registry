---
layout: container
name:  "quay.io/biocontainers/cgat-apps"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgat-apps/container.yaml"
config_url: "https://raw.githubusercontent.com//singularityhub/shpc-registry/main/quay.io/biocontainers/cgat-apps/container.yaml"
updated_at: "2022-10-29 05:30:17.068464"
latest: "0.6.5--py37h179cca4_2"
container_url: "https://biocontainers.pro/tools/cgat-apps"
aliases:
 - "cgat"
 - "docker-credential-gcloud"
 - "2to3-3.7"
 - "annotateBed"
 - "b2sum"
 - "bamToBed"
 - "bamToFastq"
 - "base32"
 - "base64"
 - "basename"
 - "basenc"
 - "bed12ToBed6"
versions:
 - "0.6.5--py37h179cca4_2"
description: "shpc-registry automated BioContainers addition for cgat-apps"
config: {"url": "https://biocontainers.pro/tools/cgat-apps", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cgat-apps", "latest": {"0.6.5--py37h179cca4_2": "sha256:d4c82e87ed915c5e18ad15801a0d6c999fcf204c37ded62a20bcb72036ae980b"}, "tags": {"0.6.5--py37h179cca4_2": "sha256:d4c82e87ed915c5e18ad15801a0d6c999fcf204c37ded62a20bcb72036ae980b"}, "docker": "quay.io/biocontainers/cgat-apps", "aliases": {"cgat": "/usr/local/bin/cgat", "docker-credential-gcloud": "/usr/local/bin/docker-credential-gcloud", "2to3-3.7": "/usr/local/bin/2to3-3.7", "annotateBed": "/usr/local/bin/annotateBed", "b2sum": "/usr/local/bin/b2sum", "bamToBed": "/usr/local/bin/bamToBed", "bamToFastq": "/usr/local/bin/bamToFastq", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "basenc": "/usr/local/bin/basenc", "bed12ToBed6": "/usr/local/bin/bed12ToBed6"}}
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


#### 2to3-3.7

```bash
$ singularity exec <container> /usr/local/bin/2to3-3.7
$ podman run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/2to3-3.7   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### annotateBed

```bash
$ singularity exec <container> /usr/local/bin/annotateBed
$ podman run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotateBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### b2sum

```bash
$ singularity exec <container> /usr/local/bin/b2sum
$ podman run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/b2sum   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToBed

```bash
$ singularity exec <container> /usr/local/bin/bamToBed
$ podman run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToBed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bamToFastq

```bash
$ singularity exec <container> /usr/local/bin/bamToFastq
$ podman run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bamToFastq   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### basenc

```bash
$ singularity exec <container> /usr/local/bin/basenc
$ podman run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/basenc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bed12ToBed6

```bash
$ singularity exec <container> /usr/local/bin/bed12ToBed6
$ podman run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bed12ToBed6   -v ${PWD} -w ${PWD} <container> -c " $@"
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