---
layout: container
name:  "quay.io/biocontainers/r-stampp"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-stampp/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-stampp/container.yaml"
updated_at: "2023-12-10 02:35:03.057014"
latest: "1.5.1--r40h6115d3f_5"
container_url: "https://biocontainers.pro/tools/r-stampp"
aliases:
 - "gdalserver"
 - "testepsg"
 - "pg_standby"
 - "applygeo"
 - "geotifcp"
 - "gnmanalyse"
 - "gnmmanage"
 - "kea-config"
 - "listgeo"
 - "makegeo"
 - "pg_checksums"
versions:
 - "1.5.1--r40h6115d3f_5"
description: "shpc-registry automated BioContainers addition for r-stampp"
config: {"url": "https://biocontainers.pro/tools/r-stampp", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-stampp", "latest": {"1.5.1--r40h6115d3f_5": "sha256:59bb9b56482eebfc1125d2325b341f43a33247534d5b01f8eabf87f65fb27da4"}, "tags": {"1.5.1--r40h6115d3f_5": "sha256:59bb9b56482eebfc1125d2325b341f43a33247534d5b01f8eabf87f65fb27da4"}, "docker": "quay.io/biocontainers/r-stampp", "aliases": {"gdalserver": "/usr/local/bin/gdalserver", "testepsg": "/usr/local/bin/testepsg", "pg_standby": "/usr/local/bin/pg_standby", "applygeo": "/usr/local/bin/applygeo", "geotifcp": "/usr/local/bin/geotifcp", "gnmanalyse": "/usr/local/bin/gnmanalyse", "gnmmanage": "/usr/local/bin/gnmmanage", "kea-config": "/usr/local/bin/kea-config", "listgeo": "/usr/local/bin/listgeo", "makegeo": "/usr/local/bin/makegeo", "pg_checksums": "/usr/local/bin/pg_checksums"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-stampp.
shpc-registry automated BioContainers addition for r-stampp
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-stampp
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-stampp:1.5.1--r40h6115d3f_5
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-stampp/1.5.1--r40h6115d3f_5
$ module help quay.io/biocontainers/r-stampp/1.5.1--r40h6115d3f_5
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-stampp-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-stampp-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-stampp-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-stampp-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-stampp-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-stampp-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gdalserver

```bash
$ singularity exec <container> /usr/local/bin/gdalserver
$ podman run --it --rm --entrypoint /usr/local/bin/gdalserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### testepsg

```bash
$ singularity exec <container> /usr/local/bin/testepsg
$ podman run --it --rm --entrypoint /usr/local/bin/testepsg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testepsg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_standby

```bash
$ singularity exec <container> /usr/local/bin/pg_standby
$ podman run --it --rm --entrypoint /usr/local/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_standby   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### applygeo

```bash
$ singularity exec <container> /usr/local/bin/applygeo
$ podman run --it --rm --entrypoint /usr/local/bin/applygeo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/applygeo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### geotifcp

```bash
$ singularity exec <container> /usr/local/bin/geotifcp
$ podman run --it --rm --entrypoint /usr/local/bin/geotifcp   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geotifcp   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnmanalyse

```bash
$ singularity exec <container> /usr/local/bin/gnmanalyse
$ podman run --it --rm --entrypoint /usr/local/bin/gnmanalyse   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnmanalyse   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gnmmanage

```bash
$ singularity exec <container> /usr/local/bin/gnmmanage
$ podman run --it --rm --entrypoint /usr/local/bin/gnmmanage   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gnmmanage   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### kea-config

```bash
$ singularity exec <container> /usr/local/bin/kea-config
$ podman run --it --rm --entrypoint /usr/local/bin/kea-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/kea-config   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### listgeo

```bash
$ singularity exec <container> /usr/local/bin/listgeo
$ podman run --it --rm --entrypoint /usr/local/bin/listgeo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/listgeo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### makegeo

```bash
$ singularity exec <container> /usr/local/bin/makegeo
$ podman run --it --rm --entrypoint /usr/local/bin/makegeo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/makegeo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pg_checksums

```bash
$ singularity exec <container> /usr/local/bin/pg_checksums
$ podman run --it --rm --entrypoint /usr/local/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_checksums   -v ${PWD} -w ${PWD} <container> -c " $@"
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