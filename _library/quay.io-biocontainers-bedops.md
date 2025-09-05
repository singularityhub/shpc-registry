---
layout: container
name:  "quay.io/biocontainers/bedops"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/bedops/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/bedops/container.yaml"
updated_at: "2025-09-05 03:50:13.833092"
latest: "2.4.42--hd6d6fdc_1"
container_url: "https://biocontainers.pro/tools/bedops"
aliases:
 - "bedops"
 - "bedops-float128"
 - "bedops-megarow"
 - "bedops-typical"
 - "switch-BEDOPS-binary-type"
 - "bam2bed"
 - "bam2bed-float128"
 - "bam2bed-megarow"
 - "bam2bed-typical"
 - "bam2bed_gnuParallel"
 - "bam2bed_gnuParallel-float128"
 - "bam2bed_gnuParallel-megarow"
 - "bam2bed_gnuParallel-typical"
 - "bam2bed_sge"
 - "bam2bed_sge-float128"
versions:
 - "2.4.23--0"
 - "2.4.41--h9f5acd7_0"
 - "2.4.41--h4ac6f70_1"
 - "2.4.41--h4ac6f70_2"
 - "2.4.41--h9948957_3"
 - "2.4.42--h9948957_0"
 - "2.4.42--hd6d6fdc_1"
description: "shpc-registry automated BioContainers addition for bedops"
config: {"url": "https://biocontainers.pro/tools/bedops", "maintainer": "@vsoch", "description": "shpc-registry automated BioContainers addition for bedops", "latest": {"2.4.42--hd6d6fdc_1": "sha256:7595db230f8f575c96b655fefba008ac041f350830c9a1c0a19bd4e3b2cb6e5c"}, "tags": {"2.4.23--0": "sha256:338c6d81e4fc2f29f3a6b76a29ab628f13a28442ba1a05b98775fd8062b9cde1", "2.4.41--h9f5acd7_0": "sha256:74852791f3dea1ae1fa2326949d2ed2667e6e2c05f90da571a81405d46638a2c", "2.4.41--h4ac6f70_1": "sha256:7ae4013363289b9d8f5a308a8b28c804338795ecbac10815ab974fc12d1b580b", "2.4.41--h4ac6f70_2": "sha256:642826a74cb1378355da319056f29a69028ab6947fb9e97344bbb3bdea797742", "2.4.41--h9948957_3": "sha256:6a0e38089cd0e79ac2c4ef482c198b9ec20986d6a4440eaa17ba1602d8f710cd", "2.4.42--h9948957_0": "sha256:300a14638783c9a862303a46a610f92d8bb376ed925caab7e991eec39c859b1b", "2.4.42--hd6d6fdc_1": "sha256:7595db230f8f575c96b655fefba008ac041f350830c9a1c0a19bd4e3b2cb6e5c"}, "docker": "quay.io/biocontainers/bedops", "aliases": {"bedops": "/usr/local/bin/bedops", "bedops-float128": "/usr/local/bin/bedops-float128", "bedops-megarow": "/usr/local/bin/bedops-megarow", "bedops-typical": "/usr/local/bin/bedops-typical", "switch-BEDOPS-binary-type": "/usr/local/bin/switch-BEDOPS-binary-type", "bam2bed": "/usr/local/bin/bam2bed", "bam2bed-float128": "/usr/local/bin/bam2bed-float128", "bam2bed-megarow": "/usr/local/bin/bam2bed-megarow", "bam2bed-typical": "/usr/local/bin/bam2bed-typical", "bam2bed_gnuParallel": "/usr/local/bin/bam2bed_gnuParallel", "bam2bed_gnuParallel-float128": "/usr/local/bin/bam2bed_gnuParallel-float128", "bam2bed_gnuParallel-megarow": "/usr/local/bin/bam2bed_gnuParallel-megarow", "bam2bed_gnuParallel-typical": "/usr/local/bin/bam2bed_gnuParallel-typical", "bam2bed_sge": "/usr/local/bin/bam2bed_sge", "bam2bed_sge-float128": "/usr/local/bin/bam2bed_sge-float128"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/bedops.
shpc-registry automated BioContainers addition for bedops
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/bedops
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/bedops:2.4.42--hd6d6fdc_1
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/bedops/2.4.42--hd6d6fdc_1
$ module help quay.io/biocontainers/bedops/2.4.42--hd6d6fdc_1
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### bedops-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### bedops-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### bedops-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### bedops-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### bedops-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### bedops-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### bedops

```bash
$ singularity exec <container> /usr/local/bin/bedops
$ podman run --it --rm --entrypoint /usr/local/bin/bedops   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedops   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedops-float128

```bash
$ singularity exec <container> /usr/local/bin/bedops-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bedops-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedops-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedops-megarow

```bash
$ singularity exec <container> /usr/local/bin/bedops-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bedops-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedops-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bedops-typical

```bash
$ singularity exec <container> /usr/local/bin/bedops-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bedops-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bedops-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### switch-BEDOPS-binary-type

```bash
$ singularity exec <container> /usr/local/bin/switch-BEDOPS-binary-type
$ podman run --it --rm --entrypoint /usr/local/bin/switch-BEDOPS-binary-type   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/switch-BEDOPS-binary-type   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed

```bash
$ singularity exec <container> /usr/local/bin/bam2bed
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_gnuParallel-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_gnuParallel-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
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