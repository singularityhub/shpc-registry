---
layout: container
name:  "quay.io/biocontainers/contatester"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/contatester/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/contatester/container.yaml"
updated_at: "2025-08-07 04:35:56.143867"
latest: "1.0.0--py311r44he3b539c_4"
container_url: "https://biocontainers.pro/tools/contatester"
aliases:
 - "calculAllelicBalance.sh"
 - "checkContaminant.sh"
 - "contaReport.R"
 - "contatester"
 - "depth_estim_from_vcf.sh"
 - "recupConta.sh"
 - "oshCC"
 - "oshc++"
 - "oshcxx"
 - "shmemCC"
 - "shmemc++"
 - "shmemcxx"
 - "oshcc"
 - "oshfort"
 - "oshmem_info"
 - "oshrun"
 - "shmemcc"
 - "shmemfort"
 - "shmemrun"
 - "flask"
 - "gff2gff.py"
 - "aggregate_profile.pl"
 - "profile2mat.pl"
 - "mpiCC"
 - "ompi-clean"
 - "ompi-server"
 - "ompi_info"
 - "opal_wrapper"
 - "orte-clean"
 - "orte-info"
 - "orte-server"
versions:
 - "1.0.0--py39r41h9a9d1d7_0"
 - "1.0.0--py310r42h2f90316_1"
 - "1.0.0--py39r42h235072b_2"
 - "1.0.0--py38r42h4ef9e6b_2"
 - "1.0.0--py311r43h1a4d1c9_3"
 - "1.0.0--py38r43h598b33d_3"
 - "1.0.0--py311r44he3b539c_4"
description: "singularity registry hpc automated addition for contatester"
config: {"url": "https://biocontainers.pro/tools/contatester", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for contatester", "latest": {"1.0.0--py311r44he3b539c_4": "sha256:08d2a8a50b31d978fcae0da976b036df48fda9b4aa39ea43b283255925c33ec1"}, "tags": {"1.0.0--py39r41h9a9d1d7_0": "sha256:0b48556965af45e1c5bb53c91e8607be8c9d6620334224602fd87d4413ae0cb4", "1.0.0--py310r42h2f90316_1": "sha256:63846ddb7efb9010d20e75f5b63f8ad671bfb00bc6d9a057c1fb35c418cb7455", "1.0.0--py39r42h235072b_2": "sha256:ce8bc5d6f163b7548583474672f5f24e0b863d950fcdb54071f40053ea972eea", "1.0.0--py38r42h4ef9e6b_2": "sha256:e756cdebc02d2a807d257ce29ebab2967f3f118d47251bf276db432c36b3dfea", "1.0.0--py311r43h1a4d1c9_3": "sha256:7d54b7199aca380c81e060904ac4d6c63c29a376fd93c23911d20572f4ee8e50", "1.0.0--py38r43h598b33d_3": "sha256:1cf66d55a83f0fd6705a86ec8254181745d4be28d8f9da697ef1eeb82fd8ef05", "1.0.0--py311r44he3b539c_4": "sha256:08d2a8a50b31d978fcae0da976b036df48fda9b4aa39ea43b283255925c33ec1"}, "docker": "quay.io/biocontainers/contatester", "aliases": {"calculAllelicBalance.sh": "/usr/local/bin/calculAllelicBalance.sh", "checkContaminant.sh": "/usr/local/bin/checkContaminant.sh", "contaReport.R": "/usr/local/bin/contaReport.R", "contatester": "/usr/local/bin/contatester", "depth_estim_from_vcf.sh": "/usr/local/bin/depth_estim_from_vcf.sh", "recupConta.sh": "/usr/local/bin/recupConta.sh", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun", "shmemcc": "/usr/local/bin/shmemcc", "shmemfort": "/usr/local/bin/shmemfort", "shmemrun": "/usr/local/bin/shmemrun", "flask": "/usr/local/bin/flask", "gff2gff.py": "/usr/local/bin/gff2gff.py", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "mpiCC": "/usr/local/bin/mpiCC", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "ompi_info": "/usr/local/bin/ompi_info", "opal_wrapper": "/usr/local/bin/opal_wrapper", "orte-clean": "/usr/local/bin/orte-clean", "orte-info": "/usr/local/bin/orte-info", "orte-server": "/usr/local/bin/orte-server"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/contatester.
singularity registry hpc automated addition for contatester
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/contatester
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/contatester:1.0.0--py311r44he3b539c_4
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/contatester/1.0.0--py311r44he3b539c_4
$ module help quay.io/biocontainers/contatester/1.0.0--py311r44he3b539c_4
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### contatester-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### contatester-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### contatester-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### contatester-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### contatester-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### contatester-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### calculAllelicBalance.sh

```bash
$ singularity exec <container> /usr/local/bin/calculAllelicBalance.sh
$ podman run --it --rm --entrypoint /usr/local/bin/calculAllelicBalance.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/calculAllelicBalance.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### checkContaminant.sh

```bash
$ singularity exec <container> /usr/local/bin/checkContaminant.sh
$ podman run --it --rm --entrypoint /usr/local/bin/checkContaminant.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/checkContaminant.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contaReport.R

```bash
$ singularity exec <container> /usr/local/bin/contaReport.R
$ podman run --it --rm --entrypoint /usr/local/bin/contaReport.R   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contaReport.R   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### contatester

```bash
$ singularity exec <container> /usr/local/bin/contatester
$ podman run --it --rm --entrypoint /usr/local/bin/contatester   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/contatester   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### depth_estim_from_vcf.sh

```bash
$ singularity exec <container> /usr/local/bin/depth_estim_from_vcf.sh
$ podman run --it --rm --entrypoint /usr/local/bin/depth_estim_from_vcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/depth_estim_from_vcf.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### recupConta.sh

```bash
$ singularity exec <container> /usr/local/bin/recupConta.sh
$ podman run --it --rm --entrypoint /usr/local/bin/recupConta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/recupConta.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshCC

```bash
$ singularity exec <container> /usr/local/bin/oshCC
$ podman run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshc++

```bash
$ singularity exec <container> /usr/local/bin/oshc++
$ podman run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcxx

```bash
$ singularity exec <container> /usr/local/bin/oshcxx
$ podman run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemCC

```bash
$ singularity exec <container> /usr/local/bin/shmemCC
$ podman run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemc++

```bash
$ singularity exec <container> /usr/local/bin/shmemc++
$ podman run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemc++   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcxx

```bash
$ singularity exec <container> /usr/local/bin/shmemcxx
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcxx   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshcc

```bash
$ singularity exec <container> /usr/local/bin/oshcc
$ podman run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshfort

```bash
$ singularity exec <container> /usr/local/bin/oshfort
$ podman run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshfort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshmem_info

```bash
$ singularity exec <container> /usr/local/bin/oshmem_info
$ podman run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshmem_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### oshrun

```bash
$ singularity exec <container> /usr/local/bin/oshrun
$ podman run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/oshrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemcc

```bash
$ singularity exec <container> /usr/local/bin/shmemcc
$ podman run --it --rm --entrypoint /usr/local/bin/shmemcc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemcc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemfort

```bash
$ singularity exec <container> /usr/local/bin/shmemfort
$ podman run --it --rm --entrypoint /usr/local/bin/shmemfort   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemfort   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### shmemrun

```bash
$ singularity exec <container> /usr/local/bin/shmemrun
$ podman run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/shmemrun   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### flask

```bash
$ singularity exec <container> /usr/local/bin/flask
$ podman run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/flask   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### gff2gff.py

```bash
$ singularity exec <container> /usr/local/bin/gff2gff.py
$ podman run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/gff2gff.py   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### aggregate_profile.pl

```bash
$ singularity exec <container> /usr/local/bin/aggregate_profile.pl
$ podman run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/aggregate_profile.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### profile2mat.pl

```bash
$ singularity exec <container> /usr/local/bin/profile2mat.pl
$ podman run --it --rm --entrypoint /usr/local/bin/profile2mat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/profile2mat.pl   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### mpiCC

```bash
$ singularity exec <container> /usr/local/bin/mpiCC
$ podman run --it --rm --entrypoint /usr/local/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/mpiCC   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-clean

```bash
$ singularity exec <container> /usr/local/bin/ompi-clean
$ podman run --it --rm --entrypoint /usr/local/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi-server

```bash
$ singularity exec <container> /usr/local/bin/ompi-server
$ podman run --it --rm --entrypoint /usr/local/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi-server   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### ompi_info

```bash
$ singularity exec <container> /usr/local/bin/ompi_info
$ podman run --it --rm --entrypoint /usr/local/bin/ompi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ompi_info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### opal_wrapper

```bash
$ singularity exec <container> /usr/local/bin/opal_wrapper
$ podman run --it --rm --entrypoint /usr/local/bin/opal_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/opal_wrapper   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-clean

```bash
$ singularity exec <container> /usr/local/bin/orte-clean
$ podman run --it --rm --entrypoint /usr/local/bin/orte-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-clean   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-info

```bash
$ singularity exec <container> /usr/local/bin/orte-info
$ podman run --it --rm --entrypoint /usr/local/bin/orte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-info   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orte-server

```bash
$ singularity exec <container> /usr/local/bin/orte-server
$ podman run --it --rm --entrypoint /usr/local/bin/orte-server   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orte-server   -v ${PWD} -w ${PWD} <container> -c " $@"
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