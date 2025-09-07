---
layout: container
name:  "quay.io/biocontainers/pgscatalog.match"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/pgscatalog.match/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/pgscatalog.match/container.yaml"
updated_at: "2025-09-07 03:35:33.169229"
latest: "0.4.0--pyhdfd78af_0"
container_url: "https://biocontainers.pro/tools/pgscatalog.match"
aliases:
 - "pgscatalog-combine"
 - "pgscatalog-download"
 - "pgscatalog-intersect"
 - "pgscatalog-match"
 - "pgscatalog-matchmerge"
 - "pgscatalog-relabel"
 - "protoc-25.3.0"
 - "genl-ctrl-list"
 - "idiag-socket-details"
 - "nf-ct-add"
 - "nf-ct-events"
 - "nf-ct-list"
 - "nf-exp-add"
 - "nf-exp-delete"
 - "nf-exp-list"
 - "nf-log"
 - "nf-monitor"
 - "nf-queue"
 - "nl-addr-add"
 - "nl-addr-delete"
 - "nl-addr-list"
 - "nl-class-add"
 - "nl-class-delete"
 - "nl-class-list"
 - "nl-classid-lookup"
 - "nl-cls-add"
 - "nl-cls-delete"
 - "nl-cls-list"
 - "nl-fib-lookup"
 - "nl-link-enslave"
 - "nl-link-ifindex2name"
 - "nl-link-list"
versions:
 - "0.2.2--pyhdfd78af_0"
 - "0.3.1--pyhdfd78af_0"
 - "0.2.3--pyhdfd78af_0"
 - "0.3.2--pyhdfd78af_0"
 - "0.3.3--pyhdfd78af_0"
 - "0.4.0--pyhdfd78af_0"
description: "singularity registry hpc automated addition for pgscatalog.match"
config: {"url": "https://biocontainers.pro/tools/pgscatalog.match", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for pgscatalog.match", "latest": {"0.4.0--pyhdfd78af_0": "sha256:14de4e49b3985b050d2ffae9dde16450f6a26702bb322931c6c34209da3a1fd5"}, "tags": {"0.2.2--pyhdfd78af_0": "sha256:edcc5e44678bbf9e27634f2462317712b24265d5ea57145c7f13522bd3d89b08", "0.3.1--pyhdfd78af_0": "sha256:5141053184bfa4506200bc9c734098720adf87bc6f8c61cf47398e338e3f5423", "0.2.3--pyhdfd78af_0": "sha256:556e2f425b22966c9d0edcc47c5fc39fee1bff8ae67762e91a4c105604cc3662", "0.3.2--pyhdfd78af_0": "sha256:ab6437a0facca0421bdca4d6658ef2499c7bea6d957d0fe53e149f5c0eeadf87", "0.3.3--pyhdfd78af_0": "sha256:4bb29dbabd9f81a628052209a1badd17d07bb7ccfb846d5cc53604dc3429a9de", "0.4.0--pyhdfd78af_0": "sha256:14de4e49b3985b050d2ffae9dde16450f6a26702bb322931c6c34209da3a1fd5"}, "docker": "quay.io/biocontainers/pgscatalog.match", "aliases": {"pgscatalog-combine": "/usr/local/bin/pgscatalog-combine", "pgscatalog-download": "/usr/local/bin/pgscatalog-download", "pgscatalog-intersect": "/usr/local/bin/pgscatalog-intersect", "pgscatalog-match": "/usr/local/bin/pgscatalog-match", "pgscatalog-matchmerge": "/usr/local/bin/pgscatalog-matchmerge", "pgscatalog-relabel": "/usr/local/bin/pgscatalog-relabel", "protoc-25.3.0": "/usr/local/bin/protoc-25.3.0", "genl-ctrl-list": "/usr/local/bin/genl-ctrl-list", "idiag-socket-details": "/usr/local/bin/idiag-socket-details", "nf-ct-add": "/usr/local/bin/nf-ct-add", "nf-ct-events": "/usr/local/bin/nf-ct-events", "nf-ct-list": "/usr/local/bin/nf-ct-list", "nf-exp-add": "/usr/local/bin/nf-exp-add", "nf-exp-delete": "/usr/local/bin/nf-exp-delete", "nf-exp-list": "/usr/local/bin/nf-exp-list", "nf-log": "/usr/local/bin/nf-log", "nf-monitor": "/usr/local/bin/nf-monitor", "nf-queue": "/usr/local/bin/nf-queue", "nl-addr-add": "/usr/local/bin/nl-addr-add", "nl-addr-delete": "/usr/local/bin/nl-addr-delete", "nl-addr-list": "/usr/local/bin/nl-addr-list", "nl-class-add": "/usr/local/bin/nl-class-add", "nl-class-delete": "/usr/local/bin/nl-class-delete", "nl-class-list": "/usr/local/bin/nl-class-list", "nl-classid-lookup": "/usr/local/bin/nl-classid-lookup", "nl-cls-add": "/usr/local/bin/nl-cls-add", "nl-cls-delete": "/usr/local/bin/nl-cls-delete", "nl-cls-list": "/usr/local/bin/nl-cls-list", "nl-fib-lookup": "/usr/local/bin/nl-fib-lookup", "nl-link-enslave": "/usr/local/bin/nl-link-enslave", "nl-link-ifindex2name": "/usr/local/bin/nl-link-ifindex2name", "nl-link-list": "/usr/local/bin/nl-link-list"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/pgscatalog.match.
singularity registry hpc automated addition for pgscatalog.match
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/pgscatalog.match
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/pgscatalog.match:0.4.0--pyhdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/pgscatalog.match/0.4.0--pyhdfd78af_0
$ module help quay.io/biocontainers/pgscatalog.match/0.4.0--pyhdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### pgscatalog.match-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### pgscatalog.match-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### pgscatalog.match-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### pgscatalog.match-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### pgscatalog.match-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### pgscatalog.match-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pgscatalog-combine

```bash
$ singularity exec <container> /usr/local/bin/pgscatalog-combine
$ podman run --it --rm --entrypoint /usr/local/bin/pgscatalog-combine   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgscatalog-combine   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgscatalog-download

```bash
$ singularity exec <container> /usr/local/bin/pgscatalog-download
$ podman run --it --rm --entrypoint /usr/local/bin/pgscatalog-download   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgscatalog-download   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgscatalog-intersect

```bash
$ singularity exec <container> /usr/local/bin/pgscatalog-intersect
$ podman run --it --rm --entrypoint /usr/local/bin/pgscatalog-intersect   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgscatalog-intersect   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgscatalog-match

```bash
$ singularity exec <container> /usr/local/bin/pgscatalog-match
$ podman run --it --rm --entrypoint /usr/local/bin/pgscatalog-match   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgscatalog-match   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgscatalog-matchmerge

```bash
$ singularity exec <container> /usr/local/bin/pgscatalog-matchmerge
$ podman run --it --rm --entrypoint /usr/local/bin/pgscatalog-matchmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgscatalog-matchmerge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pgscatalog-relabel

```bash
$ singularity exec <container> /usr/local/bin/pgscatalog-relabel
$ podman run --it --rm --entrypoint /usr/local/bin/pgscatalog-relabel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pgscatalog-relabel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-25.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-25.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-25.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### genl-ctrl-list

```bash
$ singularity exec <container> /usr/local/bin/genl-ctrl-list
$ podman run --it --rm --entrypoint /usr/local/bin/genl-ctrl-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/genl-ctrl-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### idiag-socket-details

```bash
$ singularity exec <container> /usr/local/bin/idiag-socket-details
$ podman run --it --rm --entrypoint /usr/local/bin/idiag-socket-details   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/idiag-socket-details   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-ct-add

```bash
$ singularity exec <container> /usr/local/bin/nf-ct-add
$ podman run --it --rm --entrypoint /usr/local/bin/nf-ct-add   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-ct-add   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-ct-events

```bash
$ singularity exec <container> /usr/local/bin/nf-ct-events
$ podman run --it --rm --entrypoint /usr/local/bin/nf-ct-events   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-ct-events   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-ct-list

```bash
$ singularity exec <container> /usr/local/bin/nf-ct-list
$ podman run --it --rm --entrypoint /usr/local/bin/nf-ct-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-ct-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-exp-add

```bash
$ singularity exec <container> /usr/local/bin/nf-exp-add
$ podman run --it --rm --entrypoint /usr/local/bin/nf-exp-add   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-exp-add   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-exp-delete

```bash
$ singularity exec <container> /usr/local/bin/nf-exp-delete
$ podman run --it --rm --entrypoint /usr/local/bin/nf-exp-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-exp-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-exp-list

```bash
$ singularity exec <container> /usr/local/bin/nf-exp-list
$ podman run --it --rm --entrypoint /usr/local/bin/nf-exp-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-exp-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-log

```bash
$ singularity exec <container> /usr/local/bin/nf-log
$ podman run --it --rm --entrypoint /usr/local/bin/nf-log   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-log   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-monitor

```bash
$ singularity exec <container> /usr/local/bin/nf-monitor
$ podman run --it --rm --entrypoint /usr/local/bin/nf-monitor   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-monitor   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nf-queue

```bash
$ singularity exec <container> /usr/local/bin/nf-queue
$ podman run --it --rm --entrypoint /usr/local/bin/nf-queue   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nf-queue   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-addr-add

```bash
$ singularity exec <container> /usr/local/bin/nl-addr-add
$ podman run --it --rm --entrypoint /usr/local/bin/nl-addr-add   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-addr-add   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-addr-delete

```bash
$ singularity exec <container> /usr/local/bin/nl-addr-delete
$ podman run --it --rm --entrypoint /usr/local/bin/nl-addr-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-addr-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-addr-list

```bash
$ singularity exec <container> /usr/local/bin/nl-addr-list
$ podman run --it --rm --entrypoint /usr/local/bin/nl-addr-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-addr-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-class-add

```bash
$ singularity exec <container> /usr/local/bin/nl-class-add
$ podman run --it --rm --entrypoint /usr/local/bin/nl-class-add   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-class-add   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-class-delete

```bash
$ singularity exec <container> /usr/local/bin/nl-class-delete
$ podman run --it --rm --entrypoint /usr/local/bin/nl-class-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-class-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-class-list

```bash
$ singularity exec <container> /usr/local/bin/nl-class-list
$ podman run --it --rm --entrypoint /usr/local/bin/nl-class-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-class-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-classid-lookup

```bash
$ singularity exec <container> /usr/local/bin/nl-classid-lookup
$ podman run --it --rm --entrypoint /usr/local/bin/nl-classid-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-classid-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-cls-add

```bash
$ singularity exec <container> /usr/local/bin/nl-cls-add
$ podman run --it --rm --entrypoint /usr/local/bin/nl-cls-add   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-cls-add   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-cls-delete

```bash
$ singularity exec <container> /usr/local/bin/nl-cls-delete
$ podman run --it --rm --entrypoint /usr/local/bin/nl-cls-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-cls-delete   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-cls-list

```bash
$ singularity exec <container> /usr/local/bin/nl-cls-list
$ podman run --it --rm --entrypoint /usr/local/bin/nl-cls-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-cls-list   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-fib-lookup

```bash
$ singularity exec <container> /usr/local/bin/nl-fib-lookup
$ podman run --it --rm --entrypoint /usr/local/bin/nl-fib-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-fib-lookup   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-link-enslave

```bash
$ singularity exec <container> /usr/local/bin/nl-link-enslave
$ podman run --it --rm --entrypoint /usr/local/bin/nl-link-enslave   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-link-enslave   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-link-ifindex2name

```bash
$ singularity exec <container> /usr/local/bin/nl-link-ifindex2name
$ podman run --it --rm --entrypoint /usr/local/bin/nl-link-ifindex2name   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-link-ifindex2name   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nl-link-list

```bash
$ singularity exec <container> /usr/local/bin/nl-link-list
$ podman run --it --rm --entrypoint /usr/local/bin/nl-link-list   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nl-link-list   -v ${PWD} -w ${PWD} <container> -c " $@"
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