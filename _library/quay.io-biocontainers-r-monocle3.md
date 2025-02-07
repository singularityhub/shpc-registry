---
layout: container
name:  "quay.io/biocontainers/r-monocle3"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/r-monocle3/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/r-monocle3/container.yaml"
updated_at: "2025-02-07 03:18:21.250404"
latest: "1.3.1--r44h9948957_1"
container_url: "https://biocontainers.pro/tools/r-monocle3"
aliases:
 - "pg_amcheck"
 - "gdal_create"
 - "pdfsig"
 - "gdal_viewshed"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "pg_verifybackup"
 - "geosop"
 - "pdfattach"
 - "applygeo"
versions:
 - "1.0.0--r41h9f5acd7_2"
 - "1.0.0--r42h9f5acd7_3"
 - "1.0.0--r42h4ac6f70_4"
 - "1.0.0--r43h4ac6f70_5"
 - "1.3.1--r43h4ac6f70_0"
 - "1.3.1--r44h9948957_1"
description: "shpc-registry automated BioContainers addition for r-monocle3"
config: {"url": "https://biocontainers.pro/tools/r-monocle3", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for r-monocle3", "latest": {"1.3.1--r44h9948957_1": "sha256:7be7e053121827dcc93cc7e8fe9b4ea985498c855ce85ea9f5ce8e2157a9065e"}, "tags": {"1.0.0--r41h9f5acd7_2": "sha256:d4852b89fa06b6f62f4abd30679cc92368e8c49beea05a1ccaae664a3962152e", "1.0.0--r42h9f5acd7_3": "sha256:dea840f4cf6e2e1b09d2adebe2ce3490cf9c0611c45ebbdf111a9098ffdb96b7", "1.0.0--r42h4ac6f70_4": "sha256:4dc84bc551ba6481bccc4cd1685ba139d7d65fa2909107f7ce382bc5dd4d9410", "1.0.0--r43h4ac6f70_5": "sha256:aadf566fe5a339181d03b4eb815700b9377b6044d557ea4bbc34117265739e59", "1.3.1--r43h4ac6f70_0": "sha256:bae88ce0ddfc50996643550a2b0bf25034c6d84d8d316c5afacd220c521332f5", "1.3.1--r44h9948957_1": "sha256:7be7e053121827dcc93cc7e8fe9b4ea985498c855ce85ea9f5ce8e2157a9065e"}, "docker": "quay.io/biocontainers/r-monocle3", "aliases": {"pg_amcheck": "/usr/local/bin/pg_amcheck", "gdal_create": "/usr/local/bin/gdal_create", "pdfsig": "/usr/local/bin/pdfsig", "gdal_viewshed": "/usr/local/bin/gdal_viewshed", "gdalmdiminfo": "/usr/local/bin/gdalmdiminfo", "gdalmdimtranslate": "/usr/local/bin/gdalmdimtranslate", "pg_verifybackup": "/usr/local/bin/pg_verifybackup", "geosop": "/usr/local/bin/geosop", "pdfattach": "/usr/local/bin/pdfattach", "applygeo": "/usr/local/bin/applygeo"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/r-monocle3.
shpc-registry automated BioContainers addition for r-monocle3
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/r-monocle3
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/r-monocle3:1.3.1--r44h9948957_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/r-monocle3/1.3.1--r44h9948957_1
$ module help quay.io/biocontainers/r-monocle3/1.3.1--r44h9948957_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### r-monocle3-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### r-monocle3-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### r-monocle3-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### r-monocle3-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### r-monocle3-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### r-monocle3-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### pg_amcheck

```bash
$ singularity exec <container> /usr/local/bin/pg_amcheck
$ podman run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pg_amcheck   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gdal_create

```bash
$ singularity exec <container> /usr/local/bin/gdal_create
$ podman run --it --rm --entrypoint /usr/local/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gdal_create   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pdfsig

```bash
$ singularity exec <container> /usr/local/bin/pdfsig
$ podman run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### geosop

```bash
$ singularity exec <container> /usr/local/bin/geosop
$ podman run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/geosop   -v ${PWD} -w ${PWD} <container> -c " $@"
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