---
layout: container
name:  "quay.io/biocontainers/proteomiqon-peptidedb"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/proteomiqon-peptidedb/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/proteomiqon-peptidedb/container.yaml"
updated_at: "2023-05-31 03:12:07.793625"
latest: "0.0.7--hdfd78af_1"
container_url: "https://biocontainers.pro/tools/proteomiqon-peptidedb"
aliases:
 - "lttng-gen-tp"
 - "proteomiqon-peptidedb"
versions:
 - "0.0.7--hdfd78af_1"
description: "shpc-registry automated BioContainers addition for proteomiqon-peptidedb"
config: {"url": "https://biocontainers.pro/tools/proteomiqon-peptidedb", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for proteomiqon-peptidedb", "latest": {"0.0.7--hdfd78af_1": "sha256:da279ca28078e058e9aa61885a5d7471fa8c051e74fae4f903a9fdce702efe4e"}, "tags": {"0.0.7--hdfd78af_1": "sha256:da279ca28078e058e9aa61885a5d7471fa8c051e74fae4f903a9fdce702efe4e"}, "docker": "quay.io/biocontainers/proteomiqon-peptidedb", "aliases": {"lttng-gen-tp": "/usr/local/bin/lttng-gen-tp", "proteomiqon-peptidedb": "/usr/local/bin/proteomiqon-peptidedb"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/proteomiqon-peptidedb.
shpc-registry automated BioContainers addition for proteomiqon-peptidedb
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/proteomiqon-peptidedb
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/proteomiqon-peptidedb:0.0.7--hdfd78af_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/proteomiqon-peptidedb/0.0.7--hdfd78af_1
$ module help quay.io/biocontainers/proteomiqon-peptidedb/0.0.7--hdfd78af_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### proteomiqon-peptidedb-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-peptidedb-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### proteomiqon-peptidedb-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### proteomiqon-peptidedb-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### proteomiqon-peptidedb-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### proteomiqon-peptidedb-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### lttng-gen-tp

```bash
$ singularity exec <container> /usr/local/bin/lttng-gen-tp
$ podman run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/lttng-gen-tp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### proteomiqon-peptidedb

```bash
$ singularity exec <container> /usr/local/bin/proteomiqon-peptidedb
$ podman run --it --rm --entrypoint /usr/local/bin/proteomiqon-peptidedb   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/proteomiqon-peptidedb   -v ${PWD} -w ${PWD} <container> -c " $@"
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