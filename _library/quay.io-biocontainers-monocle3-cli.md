---
layout: container
name:  "quay.io/biocontainers/monocle3-cli"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/monocle3-cli/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/monocle3-cli/container.yaml"
updated_at: "2025-05-27 12:33:34.717794"
latest: "0.0.9--r36_1"
container_url: "https://biocontainers.pro/tools/monocle3-cli"
aliases:
 - "gdalserver"
 - "monocle3"
 - "testepsg"
 - "pg_standby"
 - "gdal_viewshed"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "pdfattach"
 - "applygeo"
 - "geotifcp"
 - "gnmanalyse"
 - "gnmmanage"
versions:
 - "0.0.9--r36_1"
description: "shpc-registry automated BioContainers addition for monocle3-cli"
config: {"url": "https://biocontainers.pro/tools/monocle3-cli", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for monocle3-cli", "latest": {"0.0.9--r36_1": "sha256:8eaa00d56865a20cb15feb62efac28324355ba7bc3a5dfdf1e9a21a837ac5ea6"}, "tags": {"0.0.9--r36_1": "sha256:8eaa00d56865a20cb15feb62efac28324355ba7bc3a5dfdf1e9a21a837ac5ea6"}, "docker": "quay.io/biocontainers/monocle3-cli", "aliases": {"gdalserver": "/usr/local/bin/gdalserver", "monocle3": "/usr/local/bin/monocle3", "testepsg": "/usr/local/bin/testepsg", "pg_standby": "/usr/local/bin/pg_standby", "gdal_viewshed": "/usr/local/bin/gdal_viewshed", "gdalmdiminfo": "/usr/local/bin/gdalmdiminfo", "gdalmdimtranslate": "/usr/local/bin/gdalmdimtranslate", "pdfattach": "/usr/local/bin/pdfattach", "applygeo": "/usr/local/bin/applygeo", "geotifcp": "/usr/local/bin/geotifcp", "gnmanalyse": "/usr/local/bin/gnmanalyse", "gnmmanage": "/usr/local/bin/gnmmanage"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/monocle3-cli.
shpc-registry automated BioContainers addition for monocle3-cli
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/monocle3-cli
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/monocle3-cli:0.0.9--r36_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/monocle3-cli/0.0.9--r36_1
$ module help quay.io/biocontainers/monocle3-cli/0.0.9--r36_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### monocle3-cli-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### monocle3-cli-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### monocle3-cli-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### monocle3-cli-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### monocle3-cli-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### monocle3-cli-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### gdalserver

```bash
$ singularity exec <container> /usr/local/bin/gdalserver
$ podman run --it --rm --entrypoint /usr/local/bin/gdalserver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalserver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### monocle3

```bash
$ singularity exec <container> /usr/local/bin/monocle3
$ podman run --it --rm --entrypoint /usr/local/bin/monocle3   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/monocle3   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### gdal_viewshed

```bash
$ singularity exec <container> /usr/local/bin/gdal_viewshed
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_viewshed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_viewshed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalmdiminfo

```bash
$ singularity exec <container> /usr/local/bin/gdalmdiminfo
$ podman run --it --rm --entrypoint /usr/local/bin/gdalmdiminfo   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalmdiminfo   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdalmdimtranslate

```bash
$ singularity exec <container> /usr/local/bin/gdalmdimtranslate
$ podman run --it --rm --entrypoint /usr/local/bin/gdalmdimtranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdalmdimtranslate   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfattach

```bash
$ singularity exec <container> /usr/local/bin/pdfattach
$ podman run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfattach   -v ${PWD} -w ${PWD} <container> -c " $@"
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