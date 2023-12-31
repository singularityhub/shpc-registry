---
layout: container
name:  "quay.io/biocontainers/svsolver"
maintainer: "@vsoch"
github: "https://github.com/singularityhub/shpc-registry/blob/main/quay.io/biocontainers/svsolver/container.yaml"
config_url: "https://raw.githubusercontent.com/singularityhub/shpc-registry/main/quay.io/biocontainers/svsolver/container.yaml"
updated_at: "2023-12-31 03:05:20.418693"
latest: "2022.07.20--mpich_h7252990_0"
container_url: "https://biocontainers.pro/tools/svsolver"
aliases:
 - "setup-symlinks.sh"
 - "svpost"
 - "svpost.bin"
 - "svpre"
 - "svpre.bin"
 - "svsolver"
 - "svsolver.bin"
 - "vtkEncodeString-8.1"
 - "vtkHashSource-8.1"
 - "vtkParseJava-8.1"
 - "vtkWrapHierarchy-8.1"
 - "vtkWrapJava-8.1"
 - "vtkWrapPython-8.1"
 - "vtkWrapPythonInit-8.1"
 - "vtkWrapTcl-8.1"
 - "vtkWrapTclInit-8.1"
 - "vtkpython"
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
 - "ortecc"
 - "orted"
versions:
 - "2022.07.20--openmpi_hde70e8a_0"
 - "2022.07.20--mpich_h7252990_0"
description: "singularity registry hpc automated addition for svsolver"
config: {"url": "https://biocontainers.pro/tools/svsolver", "maintainer": "@vsoch", "description": "singularity registry hpc automated addition for svsolver", "latest": {"2022.07.20--mpich_h7252990_0": "sha256:a918d5abb142548940b29f912f95ea84d15884c393aa2f71b6fec4ead34a1a02"}, "tags": {"2022.07.20--openmpi_hde70e8a_0": "sha256:fe68f43369ad874ca0cf74c1e57212d9e104c04a7b77fb1ea70225f26454bc94", "2022.07.20--mpich_h7252990_0": "sha256:a918d5abb142548940b29f912f95ea84d15884c393aa2f71b6fec4ead34a1a02"}, "docker": "quay.io/biocontainers/svsolver", "aliases": {"setup-symlinks.sh": "/usr/local/bin/setup-symlinks.sh", "svpost": "/usr/local/bin/svpost", "svpost.bin": "/usr/local/bin/svpost.bin", "svpre": "/usr/local/bin/svpre", "svpre.bin": "/usr/local/bin/svpre.bin", "svsolver": "/usr/local/bin/svsolver", "svsolver.bin": "/usr/local/bin/svsolver.bin", "vtkEncodeString-8.1": "/usr/local/bin/vtkEncodeString-8.1", "vtkHashSource-8.1": "/usr/local/bin/vtkHashSource-8.1", "vtkParseJava-8.1": "/usr/local/bin/vtkParseJava-8.1", "vtkWrapHierarchy-8.1": "/usr/local/bin/vtkWrapHierarchy-8.1", "vtkWrapJava-8.1": "/usr/local/bin/vtkWrapJava-8.1", "vtkWrapPython-8.1": "/usr/local/bin/vtkWrapPython-8.1", "vtkWrapPythonInit-8.1": "/usr/local/bin/vtkWrapPythonInit-8.1", "vtkWrapTcl-8.1": "/usr/local/bin/vtkWrapTcl-8.1", "vtkWrapTclInit-8.1": "/usr/local/bin/vtkWrapTclInit-8.1", "vtkpython": "/usr/local/bin/vtkpython", "oshCC": "/usr/local/bin/oshCC", "oshc++": "/usr/local/bin/oshc++", "oshcxx": "/usr/local/bin/oshcxx", "shmemCC": "/usr/local/bin/shmemCC", "shmemc++": "/usr/local/bin/shmemc++", "shmemcxx": "/usr/local/bin/shmemcxx", "oshcc": "/usr/local/bin/oshcc", "oshfort": "/usr/local/bin/oshfort", "oshmem_info": "/usr/local/bin/oshmem_info", "oshrun": "/usr/local/bin/oshrun", "shmemcc": "/usr/local/bin/shmemcc", "shmemfort": "/usr/local/bin/shmemfort", "shmemrun": "/usr/local/bin/shmemrun", "aggregate_profile.pl": "/usr/local/bin/aggregate_profile.pl", "profile2mat.pl": "/usr/local/bin/profile2mat.pl", "mpiCC": "/usr/local/bin/mpiCC", "ompi-clean": "/usr/local/bin/ompi-clean", "ompi-server": "/usr/local/bin/ompi-server", "ompi_info": "/usr/local/bin/ompi_info", "opal_wrapper": "/usr/local/bin/opal_wrapper", "orte-clean": "/usr/local/bin/orte-clean", "orte-info": "/usr/local/bin/orte-info", "orte-server": "/usr/local/bin/orte-server", "ortecc": "/usr/local/bin/ortecc", "orted": "/usr/local/bin/orted"}}
---

This module is a singularity container wrapper for quay.io/biocontainers/svsolver.
singularity registry hpc automated addition for svsolver
After [installing shpc](#install) you will want to install this container module:


```bash
$ shpc install quay.io/biocontainers/svsolver
```

Or a specific version:

```bash
$ shpc install quay.io/biocontainers/svsolver:2022.07.20--mpich_h7252990_0
```

And then you can tell lmod about your modules folder:

```bash
$ module use ./modules
```

And load the module, and ask for help, or similar.

```bash
$ module load quay.io/biocontainers/svsolver/2022.07.20--mpich_h7252990_0
$ module help quay.io/biocontainers/svsolver/2022.07.20--mpich_h7252990_0
```

You can use tab for auto-completion of module names or commands that are provided.

<br>

### Commands

When you install this module, you will be able to load it to make the following commands accessible.
Examples for both Singularity, Podman, and Docker (container technologies supported) are included.

#### svsolver-run:

```bash
$ singularity run <container>
$ podman run --rm  -v ${PWD} -w ${PWD} <container>
$ docker run --rm  -v ${PWD} -w ${PWD} <container>
```

#### svsolver-shell:

```bash
$ singularity shell -s /bin/sh <container>
$ podman run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
$ docker run --it --rm --entrypoint /bin/sh  -v ${PWD} -w ${PWD} <container>
```

#### svsolver-exec:

```bash
$ singularity exec <container> "$@"
$ podman run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
$ docker run --it --rm --entrypoint ""  -v ${PWD} -w ${PWD} <container> "$@"
```

#### svsolver-inspect:

Podman and Docker only have one inspect type.

```bash
$ podman inspect <container>
$ docker inspect <container>
```

#### svsolver-inspect-runscript:

```bash
$ singularity inspect -r <container>
```

#### svsolver-inspect-deffile:

```bash
$ singularity inspect -d <container>
```


#### setup-symlinks.sh

```bash
$ singularity exec <container> /usr/local/bin/setup-symlinks.sh
$ podman run --it --rm --entrypoint /usr/local/bin/setup-symlinks.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/setup-symlinks.sh   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svpost

```bash
$ singularity exec <container> /usr/local/bin/svpost
$ podman run --it --rm --entrypoint /usr/local/bin/svpost   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svpost   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svpost.bin

```bash
$ singularity exec <container> /usr/local/bin/svpost.bin
$ podman run --it --rm --entrypoint /usr/local/bin/svpost.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svpost.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svpre

```bash
$ singularity exec <container> /usr/local/bin/svpre
$ podman run --it --rm --entrypoint /usr/local/bin/svpre   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svpre   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svpre.bin

```bash
$ singularity exec <container> /usr/local/bin/svpre.bin
$ podman run --it --rm --entrypoint /usr/local/bin/svpre.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svpre.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svsolver

```bash
$ singularity exec <container> /usr/local/bin/svsolver
$ podman run --it --rm --entrypoint /usr/local/bin/svsolver   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svsolver   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### svsolver.bin

```bash
$ singularity exec <container> /usr/local/bin/svsolver.bin
$ podman run --it --rm --entrypoint /usr/local/bin/svsolver.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/svsolver.bin   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkEncodeString-8.1

```bash
$ singularity exec <container> /usr/local/bin/vtkEncodeString-8.1
$ podman run --it --rm --entrypoint /usr/local/bin/vtkEncodeString-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkEncodeString-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkHashSource-8.1

```bash
$ singularity exec <container> /usr/local/bin/vtkHashSource-8.1
$ podman run --it --rm --entrypoint /usr/local/bin/vtkHashSource-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkHashSource-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkParseJava-8.1

```bash
$ singularity exec <container> /usr/local/bin/vtkParseJava-8.1
$ podman run --it --rm --entrypoint /usr/local/bin/vtkParseJava-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkParseJava-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkWrapHierarchy-8.1

```bash
$ singularity exec <container> /usr/local/bin/vtkWrapHierarchy-8.1
$ podman run --it --rm --entrypoint /usr/local/bin/vtkWrapHierarchy-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkWrapHierarchy-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkWrapJava-8.1

```bash
$ singularity exec <container> /usr/local/bin/vtkWrapJava-8.1
$ podman run --it --rm --entrypoint /usr/local/bin/vtkWrapJava-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkWrapJava-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkWrapPython-8.1

```bash
$ singularity exec <container> /usr/local/bin/vtkWrapPython-8.1
$ podman run --it --rm --entrypoint /usr/local/bin/vtkWrapPython-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkWrapPython-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkWrapPythonInit-8.1

```bash
$ singularity exec <container> /usr/local/bin/vtkWrapPythonInit-8.1
$ podman run --it --rm --entrypoint /usr/local/bin/vtkWrapPythonInit-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkWrapPythonInit-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkWrapTcl-8.1

```bash
$ singularity exec <container> /usr/local/bin/vtkWrapTcl-8.1
$ podman run --it --rm --entrypoint /usr/local/bin/vtkWrapTcl-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkWrapTcl-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkWrapTclInit-8.1

```bash
$ singularity exec <container> /usr/local/bin/vtkWrapTclInit-8.1
$ podman run --it --rm --entrypoint /usr/local/bin/vtkWrapTclInit-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkWrapTclInit-8.1   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### vtkpython

```bash
$ singularity exec <container> /usr/local/bin/vtkpython
$ podman run --it --rm --entrypoint /usr/local/bin/vtkpython   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/vtkpython   -v ${PWD} -w ${PWD} <container> -c " $@"
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


#### ortecc

```bash
$ singularity exec <container> /usr/local/bin/ortecc
$ podman run --it --rm --entrypoint /usr/local/bin/ortecc   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/ortecc   -v ${PWD} -w ${PWD} <container> -c " $@"
```


#### orted

```bash
$ singularity exec <container> /usr/local/bin/orted
$ podman run --it --rm --entrypoint /usr/local/bin/orted   -v ${PWD} -w ${PWD} <container> -c " $@"
$ docker run --it --rm --entrypoint /usr/local/bin/orted   -v ${PWD} -w ${PWD} <container> -c " $@"
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