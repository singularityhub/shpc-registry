---
layout: container
name:  "quay.io/biocontainers/muat"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/muat/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/muat/container.yaml"
updated_at: "2026-01-09 03:57:50.187357"
latest: "0.1.12--pyh7e72e81_0"
container_url: "https://biocontainers.pro/tools/muat"
aliases:
 - "annotate_mutations_with_bed.sh"
 - "muat"
 - "protoc-28.3.0"
 - "swalign"
 - "torchfrtrace"
 - "pybind11-config"
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
 - "bam2bed_sge-megarow"
 - "bam2bed_sge-typical"
 - "bam2bed_slurm"
 - "bam2bed_slurm-float128"
 - "bam2bed_slurm-megarow"
 - "bam2bed_slurm-typical"
 - "bam2starch"
 - "bam2starch-float128"
 - "bam2starch-megarow"
 - "bam2starch-typical"
 - "bam2starch_gnuParallel"
 - "bam2starch_gnuParallel-float128"
 - "bam2starch_gnuParallel-megarow"
 - "bam2starch_gnuParallel-typical"
versions:
 - "0.1.6--pyh7e72e81_0"
 - "0.1.11--pyh7e72e81_0"
 - "0.1.12--pyh7e72e81_0"
description: "singularity registry hpc automated addition for muat"
config: {"url": "https://biocontainers.pro/tools/muat", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for muat", "latest": {"0.1.12--pyh7e72e81_0": "sha256:1f446ff0babb3d02b0fe2eb58584de841e4611c5a164f9a73677ab3d2f41046b"}, "tags": {"0.1.6--pyh7e72e81_0": "sha256:dbf2c063d273170de56511c77d1dd70cf18985ee5ab627c349731b92967cfc6f", "0.1.11--pyh7e72e81_0": "sha256:00b6227cb41dccca5c4d88e085d71342971cfc97d94e0eb30191e32aa9fe97b2", "0.1.12--pyh7e72e81_0": "sha256:1f446ff0babb3d02b0fe2eb58584de841e4611c5a164f9a73677ab3d2f41046b"}, "docker": "quay.io/biocontainers/muat", "aliases": {"annotate_mutations_with_bed.sh": "/usr/local/bin/annotate_mutations_with_bed.sh", "muat": "/usr/local/bin/muat", "protoc-28.3.0": "/usr/local/bin/protoc-28.3.0", "swalign": "/usr/local/bin/swalign", "torchfrtrace": "/usr/local/bin/torchfrtrace", "pybind11-config": "/usr/local/bin/pybind11-config", "bam2bed": "/usr/local/bin/bam2bed", "bam2bed-float128": "/usr/local/bin/bam2bed-float128", "bam2bed-megarow": "/usr/local/bin/bam2bed-megarow", "bam2bed-typical": "/usr/local/bin/bam2bed-typical", "bam2bed_gnuParallel": "/usr/local/bin/bam2bed_gnuParallel", "bam2bed_gnuParallel-float128": "/usr/local/bin/bam2bed_gnuParallel-float128", "bam2bed_gnuParallel-megarow": "/usr/local/bin/bam2bed_gnuParallel-megarow", "bam2bed_gnuParallel-typical": "/usr/local/bin/bam2bed_gnuParallel-typical", "bam2bed_sge": "/usr/local/bin/bam2bed_sge", "bam2bed_sge-float128": "/usr/local/bin/bam2bed_sge-float128", "bam2bed_sge-megarow": "/usr/local/bin/bam2bed_sge-megarow", "bam2bed_sge-typical": "/usr/local/bin/bam2bed_sge-typical", "bam2bed_slurm": "/usr/local/bin/bam2bed_slurm", "bam2bed_slurm-float128": "/usr/local/bin/bam2bed_slurm-float128", "bam2bed_slurm-megarow": "/usr/local/bin/bam2bed_slurm-megarow", "bam2bed_slurm-typical": "/usr/local/bin/bam2bed_slurm-typical", "bam2starch": "/usr/local/bin/bam2starch", "bam2starch-float128": "/usr/local/bin/bam2starch-float128", "bam2starch-megarow": "/usr/local/bin/bam2starch-megarow", "bam2starch-typical": "/usr/local/bin/bam2starch-typical", "bam2starch_gnuParallel": "/usr/local/bin/bam2starch_gnuParallel", "bam2starch_gnuParallel-float128": "/usr/local/bin/bam2starch_gnuParallel-float128", "bam2starch_gnuParallel-megarow": "/usr/local/bin/bam2starch_gnuParallel-megarow", "bam2starch_gnuParallel-typical": "/usr/local/bin/bam2starch_gnuParallel-typical"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/muat.
singularity registry hpc automated addition for muat
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/muat
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/muat:0.1.12--pyh7e72e81_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/muat/0.1.12--pyh7e72e81_0
$ module help quay.io/biocontainers/muat/0.1.12--pyh7e72e81_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### muat-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### muat-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### muat-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### muat-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### muat-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### muat-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### annotate_mutations_with_bed.sh

```bash
$ singularity exec <container> /usr/local/bin/annotate_mutations_with_bed.sh
$ podman run --it --rm --entrypoint /usr/local/bin/annotate_mutations_with_bed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/annotate_mutations_with_bed.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### muat

```bash
$ singularity exec <container> /usr/local/bin/muat
$ podman run --it --rm --entrypoint /usr/local/bin/muat   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/muat   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### protoc-28.3.0

```bash
$ singularity exec <container> /usr/local/bin/protoc-28.3.0
$ podman run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/protoc-28.3.0   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### swalign

```bash
$ singularity exec <container> /usr/local/bin/swalign
$ podman run --it --rm --entrypoint /usr/local/bin/swalign   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/swalign   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### torchfrtrace

```bash
$ singularity exec <container> /usr/local/bin/torchfrtrace
$ podman run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/torchfrtrace   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### pybind11-config

```bash
$ singularity exec <container> /usr/local/bin/pybind11-config
$ podman run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/pybind11-config   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### bam2bed_sge-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_sge-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_sge-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_sge-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_slurm

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_slurm
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_slurm-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_slurm-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_slurm-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_slurm-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2bed_slurm-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2bed_slurm-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2bed_slurm-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch

```bash
$ singularity exec <container> /usr/local/bin/bam2starch
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2starch-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2starch-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2starch-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_gnuParallel

```bash
$ singularity exec <container> /usr/local/bin/bam2starch_gnuParallel
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_gnuParallel-float128

```bash
$ singularity exec <container> /usr/local/bin/bam2starch_gnuParallel-float128
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel-float128   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_gnuParallel-megarow

```bash
$ singularity exec <container> /usr/local/bin/bam2starch_gnuParallel-megarow
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel-megarow   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### bam2starch_gnuParallel-typical

```bash
$ singularity exec <container> /usr/local/bin/bam2starch_gnuParallel-typical
$ podman run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/bam2starch_gnuParallel-typical   -v ${PWD} -w ${PWD} <container> -c " $@"
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