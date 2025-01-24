---
layout: container
name:  "quay.io/biocontainers/r-garnett"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-garnett/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-garnett/container.yaml"
updated_at: "2025-01-24 02:56:32.561128"
latest: "0.2.8--r44hdfd78af_6"
container_url: "https://biocontainers.pro/tools/r-garnett"
aliases:
 - "testepsg"
 - "gdal_create"
 - "pg_standby"
 - "gdal_viewshed"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "pg_verifybackup"
 - "pdfattach"
 - "applygeo"
 - "geotifcp"
versions:
 - "0.2.8--r41hdfd78af_3"
 - "0.2.8--r42hdfd78af_4"
 - "0.2.8--r43hdfd78af_5"
 - "0.2.8--r44hdfd78af_6"
description: "shpc-registry automated BioContainers addition for r-garnett"
config: {"url": "https://biocontainers.pro/tools/r-garnett", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-garnett", "latest": {"0.2.8--r44hdfd78af_6": "sha256:4ecae1e2708bebf87417b8658cce1b01424434883782d6553fba76edbe18979a"}, "tags": {"0.2.8--r41hdfd78af_3": "sha256:1fe0793cb78be331c1e4627a4f301e0a2ec795b64afc4fd134a4504f99fa8ed1", "0.2.8--r42hdfd78af_4": "sha256:6b8ac1ebb43706d01b8a898fc6b0551a2540198476f073165c0a493bd41bf1f9", "0.2.8--r43hdfd78af_5": "sha256:02868b17a3a4924fe24dd6adaa2c9023e88e483382cab1af6cb4e78f888ffc2d", "0.2.8--r44hdfd78af_6": "sha256:4ecae1e2708bebf87417b8658cce1b01424434883782d6553fba76edbe18979a"}, "docker": "quay.io/biocontainers/r-garnett", "aliases": {"testepsg": "/usr/local/bin/testepsg", "gdal_create": "/usr/local/bin/gdal_create", "pg_standby": "/usr/local/bin/pg_standby", "gdal_viewshed": "/usr/local/bin/gdal_viewshed", "gdalmdiminfo": "/usr/local/bin/gdalmdiminfo", "gdalmdimtranslate": "/usr/local/bin/gdalmdimtranslate", "pg_verifybackup": "/usr/local/bin/pg_verifybackup", "pdfattach": "/usr/local/bin/pdfattach", "applygeo": "/usr/local/bin/applygeo", "geotifcp": "/usr/local/bin/geotifcp"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-garnett.
shpc-registry automated BioContainers addition for r-garnett
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-garnett
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-garnett:0.2.8--r44hdfd78af_6
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-garnett/0.2.8--r44hdfd78af_6
$ module help quay.io/biocontainers/r-garnett/0.2.8--r44hdfd78af_6
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-garnett-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-garnett-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-garnett-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-garnett-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-garnett-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-garnett-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### testepsg

```bash
$ singularity exec <container> /usr/local/bin/testepsg
$ podman run --it --rm --entrypoint /usr/local/bin/testepsg   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/testepsg   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_create

```bash
$ singularity exec <container> /usr/local/bin/gdal_create
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### pg_verifybackup

```bash
$ singularity exec <container> /usr/local/bin/pg_verifybackup
$ podman run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_verifybackup   -v ${PWD} -w ${PWD} <container> -c " $@"
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