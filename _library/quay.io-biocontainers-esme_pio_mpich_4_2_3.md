---
layout: container
name:  "quay.io/biocontainers/esme_pio_mpich_4_2_3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_pio_mpich_4_2_3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_pio_mpich_4_2_3/container.yaml"
updated_at: "2025-06-08 04:05:22.728968"
latest: "2.6.2--h900047d_0"
container_url: "https://biocontainers.pro/tools/esme_pio_mpich_4_2_3"
aliases:
 - "mpiexec.gforker"
 - "ucx_perftest_daemon"
 - "mpichversion"
 - "mpivars"
 - "parkill"
 - "hydra_nameserver"
 - "hydra_persist"
 - "hydra_pmi_proxy"
 - "mpiexec.hydra"
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
versions:
 - "2.6.2--h900047d_0"
description: "singularity registry hpc automated addition for esme_pio_mpich_4_2_3"
config: {"url": "https://biocontainers.pro/tools/esme_pio_mpich_4_2_3", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_pio_mpich_4_2_3", "latest": {"2.6.2--h900047d_0": "sha256:fd0f279357e73592e68f5b2b1b73bf3d37a4d4586464a140d553828c6593b0df"}, "tags": {"2.6.2--h900047d_0": "sha256:fd0f279357e73592e68f5b2b1b73bf3d37a4d4586464a140d553828c6593b0df"}, "docker": "quay.io/biocontainers/esme_pio_mpich_4_2_3", "aliases": {"mpiexec.gforker": "/usr/local/bin/mpiexec.gforker", "ucx_perftest_daemon": "/usr/local/bin/ucx_perftest_daemon", "mpichversion": "/usr/local/bin/mpichversion", "mpivars": "/usr/local/bin/mpivars", "parkill": "/usr/local/bin/parkill", "hydra_nameserver": "/usr/local/bin/hydra_nameserver", "hydra_persist": "/usr/local/bin/hydra_persist", "hydra_pmi_proxy": "/usr/local/bin/hydra_pmi_proxy", "mpiexec.hydra": "/usr/local/bin/mpiexec.hydra", "genl-ctrl-list": "/usr/local/bin/genl-ctrl-list", "idiag-socket-details": "/usr/local/bin/idiag-socket-details", "nf-ct-add": "/usr/local/bin/nf-ct-add", "nf-ct-events": "/usr/local/bin/nf-ct-events", "nf-ct-list": "/usr/local/bin/nf-ct-list", "nf-exp-add": "/usr/local/bin/nf-exp-add", "nf-exp-delete": "/usr/local/bin/nf-exp-delete", "nf-exp-list": "/usr/local/bin/nf-exp-list", "nf-log": "/usr/local/bin/nf-log", "nf-monitor": "/usr/local/bin/nf-monitor", "nf-queue": "/usr/local/bin/nf-queue", "nl-addr-add": "/usr/local/bin/nl-addr-add", "nl-addr-delete": "/usr/local/bin/nl-addr-delete", "nl-addr-list": "/usr/local/bin/nl-addr-list", "nl-class-add": "/usr/local/bin/nl-class-add", "nl-class-delete": "/usr/local/bin/nl-class-delete", "nl-class-list": "/usr/local/bin/nl-class-list"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_pio_mpich_4_2_3.
singularity registry hpc automated addition for esme_pio_mpich_4_2_3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_pio_mpich_4_2_3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_pio_mpich_4_2_3:2.6.2--h900047d_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_pio_mpich_4_2_3/2.6.2--h900047d_0
$ module help quay.io/biocontainers/esme_pio_mpich_4_2_3/2.6.2--h900047d_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_pio_mpich_4_2_3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_pio_mpich_4_2_3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_pio_mpich_4_2_3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_pio_mpich_4_2_3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_pio_mpich_4_2_3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_pio_mpich_4_2_3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mpiexec.gforker

```bash
$ singularity exec <container> /usr/local/bin/mpiexec.gforker
$ podman run --it --rm --entrypoint /usr/local/bin/mpiexec.gforker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiexec.gforker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_perftest_daemon

```bash
$ singularity exec <container> /usr/local/bin/ucx_perftest_daemon
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_perftest_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_perftest_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpichversion

```bash
$ singularity exec <container> /usr/local/bin/mpichversion
$ podman run --it --rm --entrypoint /usr/local/bin/mpichversion   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpichversion   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpivars

```bash
$ singularity exec <container> /usr/local/bin/mpivars
$ podman run --it --rm --entrypoint /usr/local/bin/mpivars   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpivars   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### parkill

```bash
$ singularity exec <container> /usr/local/bin/parkill
$ podman run --it --rm --entrypoint /usr/local/bin/parkill   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/parkill   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_nameserver

```bash
$ singularity exec <container> /usr/local/bin/hydra_nameserver
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_nameserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_persist

```bash
$ singularity exec <container> /usr/local/bin/hydra_persist
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_persist   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### hydra_pmi_proxy

```bash
$ singularity exec <container> /usr/local/bin/hydra_pmi_proxy
$ podman run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/hydra_pmi_proxy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiexec.hydra

```bash
$ singularity exec <container> /usr/local/bin/mpiexec.hydra
$ podman run --it --rm --entrypoint /usr/local/bin/mpiexec.hydra   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiexec.hydra   -v ${PWD} -w ${PWD} <container> -c " $@"
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