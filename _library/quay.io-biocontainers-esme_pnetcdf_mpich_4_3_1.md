---
layout: container
name:  "quay.io/biocontainers/esme_pnetcdf_mpich_4_3_1"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_pnetcdf_mpich_4_3_1/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_pnetcdf_mpich_4_3_1/container.yaml"
updated_at: "2025-11-15 03:45:36.688610"
latest: "1.14.1--h1bacafc_0"
container_url: "https://biocontainers.pro/tools/esme_pnetcdf_mpich_4_3_1"
aliases:
 - "mpiexec.gforker"
 - "cdfdiff"
 - "ncmpidiff"
 - "ncmpidump"
 - "ncmpigen"
 - "ncoffsets"
 - "ncvalidator"
 - "pnetcdf-config"
 - "pnetcdf_version"
 - "ucx_perftest_daemon"
 - "parkill"
 - "hydra_nameserver"
 - "hydra_persist"
 - "hydra_pmi_proxy"
 - "mpiexec.hydra"
 - "mpichversion"
 - "mpivars"
 - "genl-ctrl-list"
 - "idiag-socket-details"
 - "nf-ct-add"
 - "nf-ct-events"
 - "nf-ct-list"
 - "nf-exp-add"
 - "nf-exp-delete"
 - "nf-exp-list"
versions:
 - "1.14.1--h1bacafc_0"
description: "singularity registry hpc automated addition for esme_pnetcdf_mpich_4_3_1"
config: {"url": "https://biocontainers.pro/tools/esme_pnetcdf_mpich_4_3_1", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_pnetcdf_mpich_4_3_1", "latest": {"1.14.1--h1bacafc_0": "sha256:8c8c4570a987f665f9db02db715a4938543dda9a4a8dd0dae8d685c314ea742e"}, "tags": {"1.14.1--h1bacafc_0": "sha256:8c8c4570a987f665f9db02db715a4938543dda9a4a8dd0dae8d685c314ea742e"}, "docker": "quay.io/biocontainers/esme_pnetcdf_mpich_4_3_1", "aliases": {"mpiexec.gforker": "/usr/local/bin/mpiexec.gforker", "cdfdiff": "/usr/local/bin/cdfdiff", "ncmpidiff": "/usr/local/bin/ncmpidiff", "ncmpidump": "/usr/local/bin/ncmpidump", "ncmpigen": "/usr/local/bin/ncmpigen", "ncoffsets": "/usr/local/bin/ncoffsets", "ncvalidator": "/usr/local/bin/ncvalidator", "pnetcdf-config": "/usr/local/bin/pnetcdf-config", "pnetcdf_version": "/usr/local/bin/pnetcdf_version", "ucx_perftest_daemon": "/usr/local/bin/ucx_perftest_daemon", "parkill": "/usr/local/bin/parkill", "hydra_nameserver": "/usr/local/bin/hydra_nameserver", "hydra_persist": "/usr/local/bin/hydra_persist", "hydra_pmi_proxy": "/usr/local/bin/hydra_pmi_proxy", "mpiexec.hydra": "/usr/local/bin/mpiexec.hydra", "mpichversion": "/usr/local/bin/mpichversion", "mpivars": "/usr/local/bin/mpivars", "genl-ctrl-list": "/usr/local/bin/genl-ctrl-list", "idiag-socket-details": "/usr/local/bin/idiag-socket-details", "nf-ct-add": "/usr/local/bin/nf-ct-add", "nf-ct-events": "/usr/local/bin/nf-ct-events", "nf-ct-list": "/usr/local/bin/nf-ct-list", "nf-exp-add": "/usr/local/bin/nf-exp-add", "nf-exp-delete": "/usr/local/bin/nf-exp-delete", "nf-exp-list": "/usr/local/bin/nf-exp-list"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_pnetcdf_mpich_4_3_1.
singularity registry hpc automated addition for esme_pnetcdf_mpich_4_3_1
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_pnetcdf_mpich_4_3_1
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_pnetcdf_mpich_4_3_1:1.14.1--h1bacafc_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_pnetcdf_mpich_4_3_1/1.14.1--h1bacafc_0
$ module help quay.io/biocontainers/esme_pnetcdf_mpich_4_3_1/1.14.1--h1bacafc_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_pnetcdf_mpich_4_3_1-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_pnetcdf_mpich_4_3_1-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_pnetcdf_mpich_4_3_1-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_pnetcdf_mpich_4_3_1-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_pnetcdf_mpich_4_3_1-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_pnetcdf_mpich_4_3_1-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### mpiexec.gforker

```bash
$ singularity exec <container> /usr/local/bin/mpiexec.gforker
$ podman run --it --rm --entrypoint /usr/local/bin/mpiexec.gforker   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiexec.gforker   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### cdfdiff

```bash
$ singularity exec <container> /usr/local/bin/cdfdiff
$ podman run --it --rm --entrypoint /usr/local/bin/cdfdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/cdfdiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpidiff

```bash
$ singularity exec <container> /usr/local/bin/ncmpidiff
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpidiff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpidiff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpidump

```bash
$ singularity exec <container> /usr/local/bin/ncmpidump
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpidump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpidump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncmpigen

```bash
$ singularity exec <container> /usr/local/bin/ncmpigen
$ podman run --it --rm --entrypoint /usr/local/bin/ncmpigen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncmpigen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncoffsets

```bash
$ singularity exec <container> /usr/local/bin/ncoffsets
$ podman run --it --rm --entrypoint /usr/local/bin/ncoffsets   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncoffsets   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncvalidator

```bash
$ singularity exec <container> /usr/local/bin/ncvalidator
$ podman run --it --rm --entrypoint /usr/local/bin/ncvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncvalidator   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pnetcdf-config

```bash
$ singularity exec <container> /usr/local/bin/pnetcdf-config
$ podman run --it --rm --entrypoint /usr/local/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pnetcdf-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pnetcdf_version

```bash
$ singularity exec <container> /usr/local/bin/pnetcdf_version
$ podman run --it --rm --entrypoint /usr/local/bin/pnetcdf_version   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pnetcdf_version   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ucx_perftest_daemon

```bash
$ singularity exec <container> /usr/local/bin/ucx_perftest_daemon
$ podman run --it --rm --entrypoint /usr/local/bin/ucx_perftest_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ucx_perftest_daemon   -v ${PWD} -w ${PWD} <container> -c " $@"
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