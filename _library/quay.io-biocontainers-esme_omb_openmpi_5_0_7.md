---
layout: container
name:  "quay.io/biocontainers/esme_omb_openmpi_5_0_7"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_omb_openmpi_5_0_7/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_omb_openmpi_5_0_7/container.yaml"
updated_at: "2025-05-22 03:31:02.021376"
latest: "7.5--h6f4ca90_0"
container_url: "https://biocontainers.pro/tools/esme_omb_openmpi_5_0_7"
aliases:
 - "prte"
 - "prte_info"
 - "prted"
 - "prterun"
 - "pterm"
 - "ucc_info"
 - "prun"
 - "ucx_perftest_daemon"
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
versions:
 - "7.5--h6f4ca90_0"
description: "singularity registry hpc automated addition for esme_omb_openmpi_5_0_7"
config: {"url": "https://biocontainers.pro/tools/esme_omb_openmpi_5_0_7", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_omb_openmpi_5_0_7", "latest": {"7.5--h6f4ca90_0": "sha256:0789e8c6a88e95c3b5b4c1c90990c9d32af3395fa576e56c080f21d64e1243cb"}, "tags": {"7.5--h6f4ca90_0": "sha256:0789e8c6a88e95c3b5b4c1c90990c9d32af3395fa576e56c080f21d64e1243cb"}, "docker": "quay.io/biocontainers/esme_omb_openmpi_5_0_7", "aliases": {"prte": "/usr/local/bin/prte", "prte_info": "/usr/local/bin/prte_info", "prted": "/usr/local/bin/prted", "prterun": "/usr/local/bin/prterun", "pterm": "/usr/local/bin/pterm", "ucc_info": "/usr/local/bin/ucc_info", "prun": "/usr/local/bin/prun", "ucx_perftest_daemon": "/usr/local/bin/ucx_perftest_daemon", "genl-ctrl-list": "/usr/local/bin/genl-ctrl-list", "idiag-socket-details": "/usr/local/bin/idiag-socket-details", "nf-ct-add": "/usr/local/bin/nf-ct-add", "nf-ct-events": "/usr/local/bin/nf-ct-events", "nf-ct-list": "/usr/local/bin/nf-ct-list", "nf-exp-add": "/usr/local/bin/nf-exp-add", "nf-exp-delete": "/usr/local/bin/nf-exp-delete", "nf-exp-list": "/usr/local/bin/nf-exp-list", "nf-log": "/usr/local/bin/nf-log", "nf-monitor": "/usr/local/bin/nf-monitor", "nf-queue": "/usr/local/bin/nf-queue", "nl-addr-add": "/usr/local/bin/nl-addr-add", "nl-addr-delete": "/usr/local/bin/nl-addr-delete", "nl-addr-list": "/usr/local/bin/nl-addr-list", "nl-class-add": "/usr/local/bin/nl-class-add", "nl-class-delete": "/usr/local/bin/nl-class-delete", "nl-class-list": "/usr/local/bin/nl-class-list", "nl-classid-lookup": "/usr/local/bin/nl-classid-lookup", "nl-cls-add": "/usr/local/bin/nl-cls-add", "nl-cls-delete": "/usr/local/bin/nl-cls-delete", "nl-cls-list": "/usr/local/bin/nl-cls-list", "nl-fib-lookup": "/usr/local/bin/nl-fib-lookup", "nl-link-enslave": "/usr/local/bin/nl-link-enslave"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_omb_openmpi_5_0_7.
singularity registry hpc automated addition for esme_omb_openmpi_5_0_7
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_omb_openmpi_5_0_7
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_omb_openmpi_5_0_7:7.5--h6f4ca90_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_omb_openmpi_5_0_7/7.5--h6f4ca90_0
$ module help quay.io/biocontainers/esme_omb_openmpi_5_0_7/7.5--h6f4ca90_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_omb_openmpi_5_0_7-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_omb_openmpi_5_0_7-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_omb_openmpi_5_0_7-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_omb_openmpi_5_0_7-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_omb_openmpi_5_0_7-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_omb_openmpi_5_0_7-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### prte

```bash
$ singularity exec <container> /usr/local/bin/prte
$ podman run --it --rm --entrypoint /usr/local/bin/prte   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prte   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prte_info

```bash
$ singularity exec <container> /usr/local/bin/prte_info
$ podman run --it --rm --entrypoint /usr/local/bin/prte_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prte_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prted

```bash
$ singularity exec <container> /usr/local/bin/prted
$ podman run --it --rm --entrypoint /usr/local/bin/prted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prted   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prterun

```bash
$ singularity exec <container> /usr/local/bin/prterun
$ podman run --it --rm --entrypoint /usr/local/bin/prterun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prterun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pterm

```bash
$ singularity exec <container> /usr/local/bin/pterm
$ podman run --it --rm --entrypoint /usr/local/bin/pterm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pterm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucc_info

```bash
$ singularity exec <container> /usr/local/bin/ucc_info
$ podman run --it --rm --entrypoint /usr/local/bin/ucc_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucc_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### prun

```bash
$ singularity exec <container> /usr/local/bin/prun
$ podman run --it --rm --entrypoint /usr/local/bin/prun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/prun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_perftest_daemon

```bash
$ singularity exec <container> /usr/local/bin/ucx_perftest_daemon
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_perftest_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_perftest_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
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