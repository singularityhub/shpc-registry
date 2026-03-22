---
layout: container
name:  "quay.io/biocontainers/esme_netcdf-c_psmpi_4_3_2"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/esme_netcdf-c_psmpi_4_3_2/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/esme_netcdf-c_psmpi_4_3_2/container.yaml"
updated_at: "2026-03-22 04:39:24.214817"
latest: "4.9.3--h6af5b14_0"
container_url: "https://biocontainers.pro/tools/esme_netcdf-c_psmpi_4_3_2"
aliases:
 - "nc4print"
 - "ocprint"
 - "chacl"
 - "getfacl"
 - "setfacl"
 - "cdfdiff"
 - "ncmpidiff"
 - "ncmpidump"
 - "ncmpigen"
 - "ncoffsets"
 - "ncvalidator"
 - "pnetcdf-config"
 - "pnetcdf_version"
 - "h5pcc"
 - "h5perf"
 - "h5pfc"
 - "ph5diff"
 - "attr"
 - "getfattr"
 - "setfattr"
 - "nc-config"
 - "nccopy"
 - "ncdump"
 - "ncgen"
 - "ncgen3"
versions:
 - "4.9.3--h6af5b14_0"
description: "singularity registry hpc automated addition for esme_netcdf-c_psmpi_4_3_2"
config: {"url": "https://biocontainers.pro/tools/esme_netcdf-c_psmpi_4_3_2", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for esme_netcdf-c_psmpi_4_3_2", "latest": {"4.9.3--h6af5b14_0": "sha256:175bc752187bd9c6dbc0e4094ced4dd2b410c8c013faf3876a4727214a2bbd4e"}, "tags": {"4.9.3--h6af5b14_0": "sha256:175bc752187bd9c6dbc0e4094ced4dd2b410c8c013faf3876a4727214a2bbd4e"}, "docker": "quay.io/biocontainers/esme_netcdf-c_psmpi_4_3_2", "aliases": {"nc4print": "/usr/local/bin/nc4print", "ocprint": "/usr/local/bin/ocprint", "chacl": "/usr/local/bin/chacl", "getfacl": "/usr/local/bin/getfacl", "setfacl": "/usr/local/bin/setfacl", "cdfdiff": "/usr/local/bin/cdfdiff", "ncmpidiff": "/usr/local/bin/ncmpidiff", "ncmpidump": "/usr/local/bin/ncmpidump", "ncmpigen": "/usr/local/bin/ncmpigen", "ncoffsets": "/usr/local/bin/ncoffsets", "ncvalidator": "/usr/local/bin/ncvalidator", "pnetcdf-config": "/usr/local/bin/pnetcdf-config", "pnetcdf_version": "/usr/local/bin/pnetcdf_version", "h5pcc": "/usr/local/bin/h5pcc", "h5perf": "/usr/local/bin/h5perf", "h5pfc": "/usr/local/bin/h5pfc", "ph5diff": "/usr/local/bin/ph5diff", "attr": "/usr/local/bin/attr", "getfattr": "/usr/local/bin/getfattr", "setfattr": "/usr/local/bin/setfattr", "nc-config": "/usr/local/bin/nc-config", "nccopy": "/usr/local/bin/nccopy", "ncdump": "/usr/local/bin/ncdump", "ncgen": "/usr/local/bin/ncgen", "ncgen3": "/usr/local/bin/ncgen3"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/esme_netcdf-c_psmpi_4_3_2.
singularity registry hpc automated addition for esme_netcdf-c_psmpi_4_3_2
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/esme_netcdf-c_psmpi_4_3_2
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/esme_netcdf-c_psmpi_4_3_2:4.9.3--h6af5b14_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/esme_netcdf-c_psmpi_4_3_2/4.9.3--h6af5b14_0
$ module help quay.io/biocontainers/esme_netcdf-c_psmpi_4_3_2/4.9.3--h6af5b14_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### esme_netcdf-c_psmpi_4_3_2-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### esme_netcdf-c_psmpi_4_3_2-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### esme_netcdf-c_psmpi_4_3_2-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### esme_netcdf-c_psmpi_4_3_2-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### esme_netcdf-c_psmpi_4_3_2-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### esme_netcdf-c_psmpi_4_3_2-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### nc4print

```bash
$ singularity exec <container> /usr/local/bin/nc4print
$ podman run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc4print   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ocprint

```bash
$ singularity exec <container> /usr/local/bin/ocprint
$ podman run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ocprint   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### chacl

```bash
$ singularity exec <container> /usr/local/bin/chacl
$ podman run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/chacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfacl

```bash
$ singularity exec <container> /usr/local/bin/getfacl
$ podman run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setfacl

```bash
$ singularity exec <container> /usr/local/bin/setfacl
$ podman run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setfacl   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### h5pcc

```bash
$ singularity exec <container> /usr/local/bin/h5pcc
$ podman run --it --rm --entrypoint /usr/local/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5pcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5perf

```bash
$ singularity exec <container> /usr/local/bin/h5perf
$ podman run --it --rm --entrypoint /usr/local/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5perf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### h5pfc

```bash
$ singularity exec <container> /usr/local/bin/h5pfc
$ podman run --it --rm --entrypoint /usr/local/bin/h5pfc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/h5pfc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ph5diff

```bash
$ singularity exec <container> /usr/local/bin/ph5diff
$ podman run --it --rm --entrypoint /usr/local/bin/ph5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ph5diff   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### attr

```bash
$ singularity exec <container> /usr/local/bin/attr
$ podman run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/attr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### getfattr

```bash
$ singularity exec <container> /usr/local/bin/getfattr
$ podman run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/getfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### setfattr

```bash
$ singularity exec <container> /usr/local/bin/setfattr
$ podman run --it --rm --entrypoint /usr/local/bin/setfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setfattr   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nc-config

```bash
$ singularity exec <container> /usr/local/bin/nc-config
$ podman run --it --rm --entrypoint /usr/local/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nc-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### nccopy

```bash
$ singularity exec <container> /usr/local/bin/nccopy
$ podman run --it --rm --entrypoint /usr/local/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/nccopy   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncdump

```bash
$ singularity exec <container> /usr/local/bin/ncdump
$ podman run --it --rm --entrypoint /usr/local/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncdump   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen

```bash
$ singularity exec <container> /usr/local/bin/ncgen
$ podman run --it --rm --entrypoint /usr/local/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncgen   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ncgen3

```bash
$ singularity exec <container> /usr/local/bin/ncgen3
$ podman run --it --rm --entrypoint /usr/local/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ncgen3   -v ${PWD} -w ${PWD} <container> -c " $@"
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