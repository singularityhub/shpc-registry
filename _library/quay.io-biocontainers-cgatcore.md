---
layout: container
name:  "quay.io/biocontainers/cgatcore"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/cgatcore/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/cgatcore/container.yaml"
updated_at: "2023-08-02 02:57:33.471134"
latest: "0.6.15--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/cgatcore"
aliases:
 - "bq"
 - "docker-credential-gcloud"
 - "gcloud"
 - "time"
 - "gsutil"
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
 - "0.6.9--pyhdfd78af_0"
 - "0.6.14--pyhdfd78af_0"
 - "0.6.15--pyhdfd78af_0"
description: "shpc-registry automated BioContainers addition for cgatcore"
config: {"url": "https://biocontainers.pro/tools/cgatcore", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for cgatcore", "latest": {"0.6.15--pyhdfd78af_0": "sha256:919ea5f0ee4efaca6a8786c768f01f2aec2dadd44323a24eb3eb3c108dab68cc"}, "tags": {"0.6.9--pyhdfd78af_0": "sha256:baa5e4618d6c36e5a7764593addd1c5fc1aca45e8537f4dae7b67430492aafb4", "0.6.14--pyhdfd78af_0": "sha256:4198d405701371b67dfcdf43091c1d7ca88ac2fe68bd64823930496a116369bc", "0.6.15--pyhdfd78af_0": "sha256:919ea5f0ee4efaca6a8786c768f01f2aec2dadd44323a24eb3eb3c108dab68cc"}, "docker": "quay.io/biocontainers/cgatcore", "aliases": {"bq": "/usr/local/bin/bq", "docker-credential-gcloud": "/usr/local/bin/docker-credential-gcloud", "gcloud": "/usr/local/bin/gcloud", "time": "/usr/local/bin/time", "gsutil": "/usr/local/bin/gsutil", "basenc": "/usr/local/bin/basenc", "b2sum": "/usr/local/bin/b2sum", "base32": "/usr/local/bin/base32", "base64": "/usr/local/bin/base64", "basename": "/usr/local/bin/basename", "cat": "/usr/local/bin/cat", "chcon": "/usr/local/bin/chcon", "chgrp": "/usr/local/bin/chgrp", "chmod": "/usr/local/bin/chmod"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/cgatcore.
shpc-registry automated BioContainers addition for cgatcore
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/cgatcore
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/cgatcore:0.6.15--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/cgatcore/0.6.15--pyhdfd78af_0
$ module help quay.io/biocontainers/cgatcore/0.6.15--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### cgatcore-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### cgatcore-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### cgatcore-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### cgatcore-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### cgatcore-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### cgatcore-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bq

```bash
$ singularity exec <container> /usr/local/bin/bq
$ podman run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bq   -v ${PWD} -w ${PWD} <container> -c " $@"
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