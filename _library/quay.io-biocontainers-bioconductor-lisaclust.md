---
layout: container
name:  "quay.io/biocontainers/bioconductor-lisaclust"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bioconductor-lisaclust/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bioconductor-lisaclust/container.yaml"
updated_at: "2023-10-04 05:23:44.156662"
latest: "1.8.0--r43hdfd78af_0"
container_url: "https://biocontainers.pro/tools/bioconductor-lisaclust"
aliases:
 - "testepsg"
 - "gdal_create"
 - "pdfsig"
 - "pg_standby"
 - "gdal_viewshed"
 - "gdalmdiminfo"
 - "gdalmdimtranslate"
 - "pg_verifybackup"
 - "geosop"
 - "pdfattach"
versions:
 - "1.2.0--r41hdfd78af_0"
 - "1.6.0--r42hdfd78af_0"
 - "1.8.0--r43hdfd78af_0"
description: "shpc-registry automated BioContainers addition for bioconductor-lisaclust"
config: {"url": "https://biocontainers.pro/tools/bioconductor-lisaclust", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bioconductor-lisaclust", "latest": {"1.8.0--r43hdfd78af_0": "sha256:08d383aa67943ec7d601daf6c96172b81621be1f91d6cfe2fa3eb40b200c9548"}, "tags": {"1.2.0--r41hdfd78af_0": "sha256:7c47a796f7c3e36d7207cf87f87cdb180f87e8e22d9bc7ef4fb62644b37dca52", "1.6.0--r42hdfd78af_0": "sha256:b3bae946c7d27134c533527f2e4a89bb0522f90fccb2ceb94316ca283aa57dac", "1.8.0--r43hdfd78af_0": "sha256:08d383aa67943ec7d601daf6c96172b81621be1f91d6cfe2fa3eb40b200c9548"}, "docker": "quay.io/biocontainers/bioconductor-lisaclust", "aliases": {"testepsg": "/usr/local/bin/testepsg", "gdal_create": "/usr/local/bin/gdal_create", "pdfsig": "/usr/local/bin/pdfsig", "pg_standby": "/usr/local/bin/pg_standby", "gdal_viewshed": "/usr/local/bin/gdal_viewshed", "gdalmdiminfo": "/usr/local/bin/gdalmdiminfo", "gdalmdimtranslate": "/usr/local/bin/gdalmdimtranslate", "pg_verifybackup": "/usr/local/bin/pg_verifybackup", "geosop": "/usr/local/bin/geosop", "pdfattach": "/usr/local/bin/pdfattach"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bioconductor-lisaclust.
shpc-registry automated BioContainers addition for bioconductor-lisaclust
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bioconductor-lisaclust
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bioconductor-lisaclust:1.8.0--r43hdfd78af_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bioconductor-lisaclust/1.8.0--r43hdfd78af_0
$ module help quay.io/biocontainers/bioconductor-lisaclust/1.8.0--r43hdfd78af_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bioconductor-lisaclust-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lisaclust-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bioconductor-lisaclust-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bioconductor-lisaclust-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bioconductor-lisaclust-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bioconductor-lisaclust-inspect-deffile:

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


#### pdfsig

```bash
$ singularity exec <container> /usr/local/bin/pdfsig
$ podman run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pdfsig   -v ${PWD} -w ${PWD} <container> -c " $@"
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