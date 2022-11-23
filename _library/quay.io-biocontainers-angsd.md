---
layout: container
name:  "quay.io/biocontainers/angsd"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/angsd/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/angsd/container.yaml"
updated_at: "2022-11-23 00:55:44.682479"
latest: "0.940--h470d46e_0"
container_url: "https://biocontainers.pro/tools/angsd"
aliases:
 - "NGSadmix"
 - "angsd"
 - "contamination"
 - "contamination2"
 - "haploToPlink"
 - "ibs"
 - "msHOT2glf"
 - "msToGlf"
 - "ngsPSMC"
 - "printIcounts"
 - "realSFS"
 - "scounts"
 - "smartCount"
 - "splitgl"
 - "supersim"
 - "thetaStat"
 - "htsfile"
 - "bgzip"
 - "tabix"
versions:
 - "0.939--h470d46e_1"
 - "0.940--h470d46e_0"
description: "shpc-registry automated BioContainers addition for angsd"
config: {"url": "https://biocontainers.pro/tools/angsd", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for angsd", "latest": {"0.940--h470d46e_0": "sha256:8c66bcd4193150fe945d585c42b6510a11b301b4152b84be734d739366ee8714"}, "tags": {"0.939--h470d46e_1": "sha256:969d28663c9479680380e8ced285063d51eb7056f0db8b2ed3ebed66497297d3", "0.940--h470d46e_0": "sha256:8c66bcd4193150fe945d585c42b6510a11b301b4152b84be734d739366ee8714"}, "docker": "quay.io/biocontainers/angsd", "aliases": {"NGSadmix": "/usr/local/bin/NGSadmix", "angsd": "/usr/local/bin/angsd", "contamination": "/usr/local/bin/contamination", "contamination2": "/usr/local/bin/contamination2", "haploToPlink": "/usr/local/bin/haploToPlink", "ibs": "/usr/local/bin/ibs", "msHOT2glf": "/usr/local/bin/msHOT2glf", "msToGlf": "/usr/local/bin/msToGlf", "ngsPSMC": "/usr/local/bin/ngsPSMC", "printIcounts": "/usr/local/bin/printIcounts", "realSFS": "/usr/local/bin/realSFS", "scounts": "/usr/local/bin/scounts", "smartCount": "/usr/local/bin/smartCount", "splitgl": "/usr/local/bin/splitgl", "supersim": "/usr/local/bin/supersim", "thetaStat": "/usr/local/bin/thetaStat", "htsfile": "/usr/local/bin/htsfile", "bgzip": "/usr/local/bin/bgzip", "tabix": "/usr/local/bin/tabix"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/angsd.
shpc-registry automated BioContainers addition for angsd
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/angsd
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/angsd:0.940--h470d46e_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/angsd/0.940--h470d46e_0
$ module help quay.io/biocontainers/angsd/0.940--h470d46e_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### angsd-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### angsd-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### angsd-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### angsd-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### angsd-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### angsd-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### NGSadmix

```bash
$ singularity exec <container> /usr/local/bin/NGSadmix
$ podman run --it --rm --entrypoint /usr/local/bin/NGSadmix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/NGSadmix   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### angsd

```bash
$ singularity exec <container> /usr/local/bin/angsd
$ podman run --it --rm --entrypoint /usr/local/bin/angsd   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/angsd   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contamination

```bash
$ singularity exec <container> /usr/local/bin/contamination
$ podman run --it --rm --entrypoint /usr/local/bin/contamination   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contamination   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contamination2

```bash
$ singularity exec <container> /usr/local/bin/contamination2
$ podman run --it --rm --entrypoint /usr/local/bin/contamination2   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contamination2   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### haploToPlink

```bash
$ singularity exec <container> /usr/local/bin/haploToPlink
$ podman run --it --rm --entrypoint /usr/local/bin/haploToPlink   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/haploToPlink   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ibs

```bash
$ singularity exec <container> /usr/local/bin/ibs
$ podman run --it --rm --entrypoint /usr/local/bin/ibs   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ibs   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msHOT2glf

```bash
$ singularity exec <container> /usr/local/bin/msHOT2glf
$ podman run --it --rm --entrypoint /usr/local/bin/msHOT2glf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msHOT2glf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### msToGlf

```bash
$ singularity exec <container> /usr/local/bin/msToGlf
$ podman run --it --rm --entrypoint /usr/local/bin/msToGlf   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/msToGlf   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ngsPSMC

```bash
$ singularity exec <container> /usr/local/bin/ngsPSMC
$ podman run --it --rm --entrypoint /usr/local/bin/ngsPSMC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ngsPSMC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### printIcounts

```bash
$ singularity exec <container> /usr/local/bin/printIcounts
$ podman run --it --rm --entrypoint /usr/local/bin/printIcounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/printIcounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### realSFS

```bash
$ singularity exec <container> /usr/local/bin/realSFS
$ podman run --it --rm --entrypoint /usr/local/bin/realSFS   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/realSFS   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### scounts

```bash
$ singularity exec <container> /usr/local/bin/scounts
$ podman run --it --rm --entrypoint /usr/local/bin/scounts   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/scounts   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### smartCount

```bash
$ singularity exec <container> /usr/local/bin/smartCount
$ podman run --it --rm --entrypoint /usr/local/bin/smartCount   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/smartCount   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### splitgl

```bash
$ singularity exec <container> /usr/local/bin/splitgl
$ podman run --it --rm --entrypoint /usr/local/bin/splitgl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/splitgl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### supersim

```bash
$ singularity exec <container> /usr/local/bin/supersim
$ podman run --it --rm --entrypoint /usr/local/bin/supersim   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/supersim   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### thetaStat

```bash
$ singularity exec <container> /usr/local/bin/thetaStat
$ podman run --it --rm --entrypoint /usr/local/bin/thetaStat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/thetaStat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### htsfile

```bash
$ singularity exec <container> /usr/local/bin/htsfile
$ podman run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/htsfile   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bgzip

```bash
$ singularity exec <container> /usr/local/bin/bgzip
$ podman run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bgzip   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### tabix

```bash
$ singularity exec <container> /usr/local/bin/tabix
$ podman run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/tabix   -v ${PWD} -w ${PWD} <container> -c " $@"
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